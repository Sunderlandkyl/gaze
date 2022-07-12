import clr # pip install pythonnet
import pyigtl # pip install pyigtl
import time
import logging
import numpy as np
import pathlib
path = str(pathlib.Path(__file__).parent.resolve())
clr.AddReference(f"{path}/GazePointer.dll")
import GazePointer

gazeFlowAPI = GazePointer.CGazeFlowAPI()

gazePointerAddress = "127.0.0.1"
gazePointerPort    = 43333
gazePointerAppKey  = "AppKeyDemo"

noRegionId = "None"
regions = {
    "LeftHalf" : [0, 0, 959, 1080],
    "RightHalf" : [960, 0, 1920, 1080],
}

igtlServerPort = 18944
server = pyigtl.OpenIGTLinkServer(port=igtlServerPort)

if not gazeFlowAPI.Connect(gazePointerAddress, gazePointerPort, gazePointerAppKey):
    logging.error("Connection fail")
    exit()

while True:
    if not server.is_connected():
        # No clients are connected over OpenIGTLink
        time.sleep(0.5)
        continue

    gazeData = gazeFlowAPI.ReciveGazeDataSyn()
    if gazeData:

        screenToGazePositionMatrix = np.eye(4, dtype=np.float32)
        screenToGazePositionMatrix[0,3] = gazeData.GazeX
        screenToGazePositionMatrix[1,3] = gazeData.GazeY
        gaze_message = pyigtl.TransformMessage(screenToGazePositionMatrix, device_name="Gaze_Position")
        server.send_message(gaze_message, wait=True)

        currentRegionId = noRegionId
        for regionId, regionExtent in regions.items():
            if (regionExtent[0] <= gazeData.GazeX and
                regionExtent[2] >= gazeData.GazeX and
                regionExtent[1] <= gazeData.GazeY and
                regionExtent[3] >= gazeData.GazeY):
                # Gaze is within current region
                currentRegionId = regionId
                break
        region_message = pyigtl.StringMessage(f"{currentRegionId}", device_name="Gaze_Region")
        server.send_message(region_message, wait=True)

    else:
        logging.info("Disconected, reconnecting")
        if not gazeFlowAPI.Connect(gazePointerAddress, gazePointerPort, gazePointerAppKey):
            logging.error("Could not reconnect")
            break
