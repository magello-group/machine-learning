# Machine Learning
Machine Learning - Meetup

In this tutorial we will use the following development tools:
 * Python 2.7.x
 * Numpy 1.x
 * OpenCV 2.x

## Installation

### Windows

 1. If you have any existing versions of Python installed, please do not use any of these. Particularly if you have set Windows environment variables such as PYTHON_HOME or PATH 
    to work with Python globally, you might need to remove these to avoid conflicts with existing Python versions. The bits are also important - due to the Fortran compiled libs of 
    scipy, the 32 bit version of Anaconda is very unlikely to work on a 64 bit machine.     
 2. Install Anaconda (contains numpy, scipy and scikit): https://www.continuum.io/downloads/
 2. Verify installion by executing "python --version", the answer should contain the string "Anaconda x.x.x"
 3. From now on, you  need to use the python.exe provided by anaconda. You can choose between calling anacondas python.exe directly with parameters from its folder,or set <PathToAnacondaRoot> and <PathToAnacondaRoot>/Scripts to the global Windows PATH variable. 
    Troubleshooting note:  If working globally does not work, and working from the Anaconda root does, the problem is likely to depend on the environment variables.  
 3. Download and install the latest OpenCV distribution from here: http://opencv.org/downloads.html
 4. Manually copy the file opencv\build\python\2.7\xNN\cv2.pyd to the Lib\site-packages\ directory of your Python installation (where xXX is x86 or x64)
 5. Verify the installation (instructions below)
 
### Mac

We recommend installing Python and OpenCV using homebrew.

#### Known Issues (Read before you continue!!)
If you have updated OSX there is an issue with brew. 

The OS takes ownership of some folders that brew uses if you have updated Mac OSX after installing brew.

To check this please write `ls -la /usr/local | grep -E "include|share"`

If they are owned by: "root   wheel" please take owenership of them by typing `sudo chown -R $USER:admin /usr/local/include` and  `sudo chown -R $USER:admin /usr/local/share` respectivly.


#### Procedure

 1. Install homebrew from: http://brew.sh/
 2. Install python: `brew install python`
 3. Open a new shell (to upgrade the path and environment)
 4. Type: `which python`
 5. Make sure that the response is: 'usr/local/bin/python', otherwise retry...
 6. Upgrade pip `pip install --upgrade pip`
 7. Install science tap in homebrew: `brew tap homebrew/science/`
 8. Install OpenCV: `brew install opencv`
 9. Install OpenCV python extensions: `echo /usr/local/opt/opencv/lib/python2.7/site-packages >> /usr/local/lib/python2.7/site-packages/opencv.pth`
10. `pip install scipy`
11. `pip install scikit-learn` 
12. `pip install matplotlib`
13. Verify the installation (instructions below)

## Verify your installation

 * Run in terminal: `python`
 * Type: `import cv2`
 * Type: `cv2.__version__`
 * The result should be the version of OpenCV currently installed (2.x)
 * Verify scipy installation by typing: `import scipy`
 * Verify scikit-learn installation by typing: `import sklearn`
 * Verify matplot: `import matplotlib`
If it doesn't work, try opening a new shell to make sure that the right defaults have been loaded!

If it still doesn't work, please contact us so we can help!
