# machine-learning
Machine Learning Meetup

In this tutorial we will use the following development tools:

 * Python 2.7.x
 * Numpy 1.x
 * OpenCV 3.x

## installation

### Windows

 1. Download the latest Python 2.7 Windows installer from https://www.python.org/downloads/release/python-2711/
 2. To be continued...
 
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

## Test installation

 * Run: 'python'
 * Type: 'import cv2'
 * Type: 'cv2.__version__'
 * The result should be the version of OpenCV currently installed (3.x)

If it doesn't work, try opening a new shell to make sure that the right defaults have been loaded!

If it still doesn't work, please contact us so we can help!
