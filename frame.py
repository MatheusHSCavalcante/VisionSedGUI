import cv2
import os


# Função para extrair frames de um vídeo
def extract_frames(video_path, output_folder):
    # Verifica se o diretório de saída existe, se não, cria o diretório
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Carregar o vídeo
    video = cv2.VideoCapture(video_path)

    # Verifica se o vídeo foi aberto com sucesso
    if not video.isOpened():
        print("Erro ao abrir o vídeo!")
        return

    frame_count = 0
    success, frame = video.read()

    # Loop para capturar os frames
    while success:
        # Salva cada frame como uma imagem
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)

        # Lê o próximo frame
        success, frame = video.read()
        frame_count += 1

    video.release()
    print(f"Extração de frames concluída. Total de frames extraídos: {frame_count}")


# Exemplo de uso
video_path = 'C:/Users/matheus/PycharmProjects/ConverterImagen/GUI/runs/segment/predict/videoexample.avi'
output_folder = 'C:/Users/matheus/Downloads/frames'
extract_frames(video_path, output_folder)