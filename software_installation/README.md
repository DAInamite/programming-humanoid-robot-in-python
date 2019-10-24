# 1: software installation

## Python
First you have to [setup python](http://learnpythonthehardway.org/book/ex0.html), then install python libraries.
The recommended way to install python libraries is using [pip](https://pip.pypa.io/en/stable/).

#### Ubuntu

```
sudo apt-get install python-pip
pip install numpy matplotlib ipython jupyter
```
#### Windows
1. download and install python: https://www.python.org/download/windows/
2. install pip: https://pip.pypa.io/en/latest/installing.html
3. install numpy and matplotlib

```
python -m pip install numpy matplotlib ipython jupyter
```

##  Learn Python
If you are new to python, you can follow [Introduction to Python](http://introtopython.org/). If you want a little more depth, [Python Tutorial](http://docs.python.org/2/tutorial/) is a great place to start, We also recommend to [Learn Python the Hard Way](http://learnpythonthehardway.org/book/).

You can try ipython notebooks that I used in the lecture by starting ```ipython notebook``` in this folder or [open in Colab]((https://colab.research.google.com/notebooks/welcome.ipynb).

* [python_basic.ipynb](./python_basic.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DAInamite/programming-humanoid-robot-in-python/blob/master/software_installation/python_basic.ipynb)
* [numpy_baisc.ipynb](./numpy_baisc.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DAInamite/programming-humanoid-robot-in-python/blob/master/software_installation/numpy_baisc.ipynb)
* [matplotlib_basic.ipynb](./matplotlib_basic.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DAInamite/programming-humanoid-robot-in-python/blob/master/software_installation/matplotlib_basic.ipynb)


## SimSpark

[SimSpark](http://simspark.sourceforge.net/) is a generic simulator for various multiagent simulations. It supports developing physical simulations for AI and robotics research with an open-source application framework. We use [customized version](https://github.com/xuyuan/SimSpark-SPL) which has NAO V4.

#### Linux
1. download [simspark.AppImage](https://github.com/BerlinUnited/SimSpark-SPL/releases/)
2. [Make it executable and double-click it](https://github.com/AppImage/AppImageKit/wiki#-what-is-an-appimage)

#### Windows
1. download [zip package](https://github.com/BerlinUnited/SimSpark-SPL/releases/)
2. extract the zip package
3. execute *rcssserver3d.exe* to start simspark

#### From source code (Other operation systems)
1. download source code from https://github.com/xuyuan/SimSpark-SPL
2. follow the instruction in https://gitlab.com/robocup-sim/SimSpark/wikis/home


### Try out sample agent
#### start sample agent
1. start simspark
	* [learn how to use simspark](http://simspark.sourceforge.net/wiki/index.php/Monitor)

2. start a console (cmd in windows)
3. go to the *software_installtion* source code folder
```
cd software_installtion
```

4. start sample agent:
```
python spark_agent.py
```

Now, the spark_agent is connected to simspark, and you can see a robot in the simulation, we are ready to program it.




