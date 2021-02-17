import clr
clr.AddReference("C:\\Capstone\\GazePointer.dll")
from System import String
import GazePointer

yeet = GazePointer.CGazeFlowAPI
gazeFlowAPI = GazePointer.CGazeFlowAPI()

AppKey = String("Dronecontrolusingeye-graze1-Non-Commercial-Use")
#print(AppKey)
# Remember to run GazePointer seperately at this point
#print (gazeFlowAPI.Connect(String("127.0.0.1"), 43333, AppKey))

if (gazeFlowAPI.Connect(String("127.0.0.1"), 43333, AppKey)):
    while (True):
        GazeData = gazeFlowAPI.ReciveGazeDataSyn()
        if (GazeData):
            print("Gaze: {0} , {1}", GazeData.GazeX, GazeData.GazeY)
            print("Head: {0} , {1}, {2}", GazeData.HeadX, GazeData.HeadY, GazeData.HeadZ)
            print("Head rot : {0} , {1}, {2}", GazeData.HeadYaw, GazeData.HeadPitch, GazeData.HeadRoll)

        else:
             print("Disconected, no gazedata recieved")
else:
    print("Connection fail")