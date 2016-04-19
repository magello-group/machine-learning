# machine-learning
Machine Learning Meetup

In this tutorial we will use the following development tools:

 * Python 2.7.x
 * Numpy 1.x
 * OpenCV 3.x

## installation

### Windows

 1. Download the latest Python 2.7 Windows installer from https://www.python.org/downloads/release/python-2711/
 2. Install numpy: 'pip install numpy'
 3. Download and install the latest OpenCV distribution from here: http://opencv.org/downloads.html
 4. Manually copy the file opencv\build\python\2.7\xNN\cv2.pyd to the Lib\site-packages\ directory of your Python installation (where xXX is x86 or x64)
 5. Verify the installation (instructions below)
 
### Mac

We recommend installing Python and OpenCV using homebrew.

 1. Install homebrew from: http://brew.sh/
 2. Install python: 'brew install python'
 3. Open a new shell (to upgrade the path and environment)
 4. Type: 'which python'
 5. Make sure that the response is: 'usr/local/bin/python', otherwise retry...
 6. Upgrade pip 'pip install --upgrade pip'
 7. Install science tap in homebrew: 'brew tap homebrew/science/'
 8. Install OpenCV: 'brew install opencv3'
 9. Install OpenCV python extensions: 'echo /usr/local/opt/opencv3/lib/python2.7/site-packages >> /usr/local/lib/python2.7/site-packages/opencv3.pth'
 10. Verify the installation (instructions below)

## Verify installation

 * Run: 'python'
 * Type: 'import cv2'
 * Type: 'cv2.\_\_version\_\_'
 * The result should be the version of OpenCV currently installed (3.x)

If it doesn't work, try opening a new shell to make sure that the right defaults have been loaded!

If it still doesn't work, please contact us so we can help!
