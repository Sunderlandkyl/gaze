printcursor.py and dll_usage_test.py are meant to be using together with the GazePointer software which can be downloaded here (https://sourceforge.net/projects/gazepointer/).

After running GazePointer you would first calibrate then select 'Control Mouse Cursor'. Then run printcursor to continuously print out the cardinal location of your gaze. dll_usage_test will merely print out one instance/set of cardinal coordinates, collected when it was run.

Note: you will need to import 'win32gui' to have the script work.

