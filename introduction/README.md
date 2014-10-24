# Week 1: software installation and sample agent
## software installation
### SimSpark

#### Ubuntu
1. add PPA and install
```
sudo add-apt-repository ppa:xu-informatik/simspark-spl
sudo apt-get update
sudo apt-get install rcssserver3d-spl
```

2. start simspark in console:

```
simspark
```

#### Windows
1. download zip package from https://db.tt/ymRTwNcT
2. extract the zip package
3. execute *rcssserver3d.exe* to start simspark

#### From source code (Other operation systems)
1. download source code from https://github.com/xuyuan/SimSpark-SPL
2. follow the instruction in http://simspark.sourceforge.net/wiki/index.php/Main_Page

### Python
First you have to [setup python](http://learnpythonthehardway.org/book/ex0.html), then install python libraries.
The recommended way to install python libraries is using *pip*.

#### Ubuntu

```
sudo apt-get install pip
sudo pip install numpy matplotlib
```
#### Windows
1. download and install python: https://www.python.org/download/windows/
2. install pip: https://pip.pypa.io/en/latest/installing.html
3. install numpy and matplotlib

```
python -m pip install numpy matplotlib
```

## Try out python
If you are new to python, you can [try it out online](http://www.codecademy.com/en/tracks/python), and follow [Introduction to Python](http://introtopython.org/). If you want a little more depth, [Python Tutorial](http://docs.python.org/2/tutorial/) is a great place to start, We also recommend to [Learn Python the Hard Way](http://learnpythonthehardway.org/book/).

## Try out sample agent
### start sample agent
1. start simspark
	* [learn how to use simspark](http://simspark.sourceforge.net/wiki/index.php/Monitor)

2. start a console (cmd in windows)
3. go to the *introduction* source code folder
```
cd introduction
```

4. start sample agent:
```
python spark_agent.py
```

Now, the spark_agent is connected to simspark, and you can see a robot in the simulation, but it does nothing. Let's program it.


### programming exercise
Open the following python files, write code follow comments in files.

* [get_sensor_values.py](./get_sensor_values.py)
* [set_joint_commands.py](./set_joint_commands.py)




