'''Base agent for SimSpark, it implements the sense-think-act loop
'''

import socket
import struct
from threading import Thread
from math import pi, atan2, asin, cos, sin
from sexpr import str2sexpr
import numpy as np

DEG_TO_RAD = pi / 180

HINGE_JOINT_PERCEPTOR = "HJ"
UNIVERSAL_JOINT_PERCEPTOR = "UJ"
TOUCH_PERCEPTOR = "TCH"
FORCE_RESISTANCE_PERCEPTOR = "FRP"
ACCELEROMETER_PERCEPTOR = "ACC"
GYRO_RATE_PERCEPTOR = "GYR"
GAME_STATE_PERCEPTOR = "GS"
GPS_PERCEPTOR = "GPS"
BAT_PERCEPTOR = "BAT"

VISION_PERCEPTOR = "See"
VISION_PERCEPTOR_TRUE_BALL = "ballpos"
VISION_PERCEPTOR_TRUE_POS = "mypos"
VISION_PERCEPTOR_BALL = "B"
VISION_PERCEPTOR_LINE = "L"
VISION_PERCEPTOR_TOP_RIGHT_FIELD_CORNER = "F1R"
VISION_PERCEPTOR_BOTTOM_RIGHT_FIELD_CORNER = "F2R"
VISION_PERCEPTOR_TOP_LEFT_FIELD_CORNER = "F1L"
VISION_PERCEPTOR_BOTTOM_LEFT_FIELD_CORNER = "F2L"
VISION_PERCEPTOR_TOP_RIGHT_GOAL_POST = "G1R"
VISION_PERCEPTOR_BOTTOM_RIGHT_GOAL_POST = "G2R"
VISION_PERCEPTOR_TOP_LEFT_GOAL_POST = "G1L"
VISION_PERCEPTOR_BOTTOM_LEFT_GOAL_POST = "G2L"
VISION_PERCEPTOR_AGENT = "P"
VISION_PERCEPTOR_HEAD = "head"
VISION_PERCEPTOR_RIGHT_LOWER_ARM = "rlowerarm"
VISION_PERCEPTOR_LEFT_LOWER_ARM = "llowerarm"
VISION_PERCEPTOR_RIGHT_FOOT = "rfoot"
VISION_PERCEPTOR_LEFT_FOOT = "lfoot"
BOTTOM_CAMERA = 'BottomCamera'
TOP_CAMERA = 'TopCamera'


JOINT_SENSOR_NAMES = {"hj1": 'HeadYaw',
                      "hj2": 'HeadPitch',
                      "laj1": 'LShoulderPitch',
                      "laj2": 'LShoulderRoll',
                      "laj3": 'LElbowYaw',
                      "laj4": 'LElbowRoll',
                      "llj1": 'LHipYawPitch',
                      "llj2": 'LHipRoll',
                      "llj3": 'LHipPitch',
                      "llj4": 'LKneePitch',
                      "llj5": 'LAnklePitch',
                      "llj6": 'LAnkleRoll',
                      "raj1": 'RShoulderPitch',
                      "raj2": 'RShoulderRoll',
                      "raj3": 'RElbowYaw',
                      "raj4": 'RElbowRoll',
                      "rlj1": 'RHipYawPitch',
                      "rlj2": 'RHipRoll',
                      "rlj3": 'RHipPitch',
                      "rlj4": 'RKneePitch',
                      "rlj5": 'RAnklePitch',
                      "rlj6": 'RAnkleRoll'}

JOINT_CMD_NAMES = {'HeadYaw': "he1",
                   'HeadPitch': "he2",
                   'LShoulderPitch': "lae1",
                   'LShoulderRoll': "lae2",
                   'LElbowYaw': "lae3",
                   'LElbowRoll': "lae4",
                   'LHipYawPitch': "lle1",
                   'LHipRoll': "lle2",
                   'LHipPitch': "lle3",
                   'LKneePitch': "lle4",
                   'LAnklePitch': "lle5",
                   'LAnkleRoll': "lle6",
                   'RShoulderPitch': "rae1",
                   'RShoulderRoll': "rae2",
                   'RElbowYaw': "rae3",
                   'RElbowRoll': "rae4",
                   'RHipYawPitch': "rle1",
                   'RHipRoll': "rle2",
                   'RHipPitch': "rle3",
                   'RKneePitch': "rle4",
                   'RAnklePitch': "rle5",
                   'RAnkleRoll': "rle6"}


# some joints are inverted in simspark compared with real NAO
INVERSED_JOINTS = ['HeadPitch',
                   'LShoulderPitch',
                   'RShoulderPitch',
                   'LHipPitch',
                   'RHipPitch',
                   'LKneePitch',
                   'RKneePitch',
                   'LAnklePitch',
                   'RAnklePitch']


class GameState:
    def __init__(self):
        self.time = 0
        self.play_mode = 'unknown'
        self.unum = 0
        self.team = 'unknown'

    def update(self, sexp):
        for s in sexp:
            name = s[0]
            if name == 't':
                self.time = float(s[1])
            elif name == 'pm':
                self.play_mode = s[1]
            elif name == 'unum':
                self.unum = int(s[1])
            elif name == 'team':
                self.team = s[1]


class Perception:
    def __init__(self):
        self.time = 0
        self.joint = {}
        self.joint_temperature = {}
        self.fsr = {}
        self.see = [{}, {}]
        self.game_state = GameState()
        self.gps = {}
        self.imu = [0, 0] # [AngleX, AngleY]

    def update(self, sexp):
        for s in sexp:
            name = s[0]
            if name == 'time':
                self.time = float(s[1][1])
            elif name == GAME_STATE_PERCEPTOR:
                self.game_state.update(s[1:])
            elif name == GYRO_RATE_PERCEPTOR:
                self.gyr = [float(v) for v in s[2][1:]]
            elif name == ACCELEROMETER_PERCEPTOR:
                self.acc = [float(v) for v in s[2][1:]]
            elif name == HINGE_JOINT_PERCEPTOR:
                jointv = {}
                for i in s[1:]:
                    jointv[i[0]] = i[1]
                name = JOINT_SENSOR_NAMES[jointv['n']]
                if 'ax' in jointv:
                    self.joint[name] = float(jointv['ax']) * DEG_TO_RAD * (-1 if name in INVERSED_JOINTS else 1)
                if 'tp' in jointv:
                    self.joint_temperature[name] = float(jointv['tp'])
            elif name == VISION_PERCEPTOR or name == TOP_CAMERA:
                self.see[0] = self._parse_vision(s[1:])
            elif name == BOTTOM_CAMERA:
                self.see[1] = self._parse_vision(s[1:])
            elif name == FORCE_RESISTANCE_PERCEPTOR:
                self.fsr[s[1][1]] = {s[2][0]: [float(v) for v in s[2][1:]],
                                     s[3][0]: [float(v) for v in s[3][1:]]}
            elif name == GPS_PERCEPTOR:
                self.gps[s[1][1]] = [float(v) for v in s[2][1:]]
            elif name == BAT_PERCEPTOR:
                self.bat = float(s[1])
            else:
                raise RuntimeError('unknown perception: ' + str(s))

        if 'torso' in self.gps:
            data = self.gps['torso']
            angX = atan2(data[9], data[10])
            angY = asin(-data[8])
            # convert angle range: angY in [-pi, pi], angX in [-pi/2, pi/2]
            if (abs(angX) > pi / 2):
                angX = pi + angX
                angX = atan2(sin(angX), cos(angX))  # normalize
                angY = pi - angY
                angY = atan2(sin(angY), cos(angY))  # normalize
            self.imu = [angX, angY]

    def _parse_vision(self, sexp):
        see = {}
        see[VISION_PERCEPTOR_LINE] = []
        see[VISION_PERCEPTOR_AGENT] = []

        for i in sexp:
            if i[0] == VISION_PERCEPTOR_LINE or i[0] == VISION_PERCEPTOR_AGENT:
                see[i[0]].append(i[1:])
            else:
                see[i[0]] = i[1:]
        return see


class Action(object):
    def __init__(self):
        self.stiffness = {}
        self.speed = {}

    def to_commands(self):
        speed = ['(%s %.2f)' % (JOINT_CMD_NAMES[k], v * (-1 if k in INVERSED_JOINTS else 1)) for k, v in self.speed.iteritems()]
        stiffness = ['(%ss %.2f)' % (JOINT_CMD_NAMES[k], v) for k, v in self.stiffness.iteritems()]
        return ''.join(speed + stiffness)


class SparkAgent(object):
    def __init__(self, simspark_ip='localhost',
                 simspark_port=3100,
                 teamname='DAInamite',
                 player_id=0,
                 sync_mode=True):
        # connect to simspark, get palyer_id
        self.sync_mode = sync_mode
        self.connect(simspark_ip, simspark_port)
        self.perception = Perception()

        self.send_command('(scene rsg/agent/naov4/nao.rsg)')
        self.sense()  # only need to get msg from simspark
        init_cmd = ('(init (unum ' + str(player_id) + ')(teamname ' + teamname + '))')
        self.send_command(init_cmd)
        self.thread = None

        while player_id == 0:
            self.sense()
            self.send_command('')
            player_id = self.perception.game_state.unum
        self.player_id = player_id

    def act(self, action):
        commands = action.to_commands()
        self.send_command(commands)

    def send_command(self, commands):
        if self.sync_mode:
            commands += '(syn)'
        self.socket.sendall(struct.pack("!I", len(commands)) + commands)

    def connect(self, simspark_ip, simspark_port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((simspark_ip, simspark_port))

    def sense(self):
        length = ''
        while(len(length) < 4):
            length += self.socket.recv(4 - len(length))
        length = struct.unpack("!I", length)[0]
        msg = ''
        while len(msg) < length:
            msg += self.socket.recv(length - len(msg))

        sexp = str2sexpr(msg)
        self.perception.update(sexp)
        return self.perception

    def think(self, perception):
        action = Action()
        return action

    def sense_think_act(self):
        perception = self.sense()
        action = self.think(perception)
        self.act(action)

    def run(self):
        while True:
            self.sense_think_act()

    def start(self):
        if self.thread is None:
            self.thread = Thread(target=self.run)
            self.thread.daemon = True
            self.thread.start()


if '__main__' == __name__:
    agent = SparkAgent()
    agent.run()
