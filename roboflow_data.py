from roboflow import Roboflow

rf = Roboflow(api_key = "pr5TPfTD7SdWLfmBv2Ki")
project = rf.workspace("sphereroad-iouse").project("fan-mfdqi")
version = project.version(1)
dataset = version.download("yolov8")



