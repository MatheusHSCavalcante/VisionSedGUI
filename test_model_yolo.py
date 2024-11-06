from ultralytics import YOLO

model_path = "C:/Users/matheus/PycharmProjects/ConverterImagen/GUI/runs/segment/train3/weights/best.pt"
model_custom = YOLO(model_path)

result = model_custom(source = "C:/Users/matheus/PycharmProjects/ConverterImagen/GUI/sphere_road_detect-10/valid/images", conf = 0.80, save=True)
