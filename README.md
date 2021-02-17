printcursor.py and GazePointerdll_Usage.py are meant to be using together with the GazePointer software which can be downloaded here (https://sourceforge.net/projects/gazepointer/).

After running GazePointer you would first calibrate then select 'Control Mouse Cursor'. Then run printcursor to continuously print out the cardinal location of your gaze. GazePointerdll_Usage.py will print out eye coordinates in whatever python IDE used. It uses GazePointer.dll

Note: you will need to import 'win32gui' to have the script work.

