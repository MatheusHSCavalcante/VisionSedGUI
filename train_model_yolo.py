from ultralytics import YOLO

model = YOLO("yolov8n-seg.pt")

if __name__ == '__main__':
    results = model.train(data="C:/Users/matheus/PycharmProjects/ConverterImagen/GUI/Fan-1/data.yaml", epochs=300, imgsz=640)