import cv2

# Inicializar capturas de vídeo para as duas câmeras
cap1 = cv2.VideoCapture('http://192.168.31.68:8080/video')  # Câmera IP
cap2 = cv2.VideoCapture(0)  # Câmera local

# Definir a resolução desejada para exibição
display_width, display_height = 500, 500

# Configurar propriedades das câmeras
width1 = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
height1 = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps1 = int(cap1.get(cv2.CAP_PROP_FPS)) if int(cap1.get(cv2.CAP_PROP_FPS)) > 0 else 20

width2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
height2 = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps2 = int(cap2.get(cv2.CAP_PROP_FPS)) if int(cap2.get(cv2.CAP_PROP_FPS)) > 0 else 20

fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Variáveis de controle
is_recording = False  # Controla gravação temporária com 'r'
frames_cam1 = []  # Armazena quadros da câmera 1 enquanto grava
frames_cam2 = []  # Armazena quadros da câmera 2 enquanto grava
all_frames_cam1 = []  # Armazena todos os quadros da câmera 1 desde o início
all_frames_cam2 = []  # Armazena todos os quadros da câmera 2 desde o início
record_count = 1  # Contador para nomear arquivos de vídeo

while True:
    # Ler cada quadro das câmeras
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        print("Erro ao capturar vídeo das câmeras")
        break

    # Redimensionar quadros para exibição
    frame1_resized = cv2.resize(frame1, (display_width, display_height))
    frame2_resized = cv2.resize(frame2, (display_width, display_height))

    # Exibir quadros em janelas separadas
    cv2.imshow('Camera 1', frame1_resized)
    cv2.imshow('Camera 2', frame2_resized)

    # Capturar tecla pressionada
    key = cv2.waitKey(1) & 0xFF

    if key == ord('r'):
        if is_recording:
            # Parar a gravação e salvar o vídeo
            print("Parando gravação e salvando o vídeo...")

            # Configurar VideoWriter com nome único para cada gravação
            out1 = cv2.VideoWriter(f'camera1_output_ip.avi', fourcc, fps1, (width1, height1))
            out2 = cv2.VideoWriter(f'camera2_output_0.avi', fourcc, fps2, (width2, height2))

            # Salvar todos os quadros capturados enquanto estava gravando
            for f in frames_cam1:
                out1.write(f)
            for f in frames_cam2:
                out2.write(f)

            # Liberar recursos dos arquivos de vídeo
            out1.release()
            out2.release()

            # Limpar listas de quadros e incrementar o contador
            frames_cam1.clear()
            frames_cam2.clear()
            record_count += 1
            is_recording = False
        else:
            # Iniciar a gravação
            print("Iniciando gravação...")
            is_recording = True

    elif key == ord('q'):
        print("Encerrando o programa e salvando vídeos desde o início...")

        # Configurar VideoWriter para salvar todos os quadros capturados desde o início
        out1 = cv2.VideoWriter(f'camera1_output_full_ip.avi', fourcc, fps1, (width1, height1))
        out2 = cv2.VideoWriter(f'camera2_output_full_0.avi', fourcc, fps2, (width2, height2))

        # Salvar todos os quadros armazenados desde o início
        for f in all_frames_cam1:
            out1.write(f)
        for f in all_frames_cam2:
            out2.write(f)

        # Liberar recursos dos arquivos de vídeo
        out1.release()
        out2.release()

        # Liberar recursos das câmeras e sair do loop
        cap1.release()
        cap2.release()
        cv2.destroyAllWindows()
        break

    # Armazenar quadros enquanto a gravação temporária está ativa
    if is_recording:
        frames_cam1.append(frame1)
        frames_cam2.append(frame2)

    # Armazenar todos os quadros desde o início para salvar ao pressionar 'q'
    all_frames_cam1.append(frame1)
    all_frames_cam2.append(frame2)

# Se o programa foi encerrado com 'q', liberar recursos das câmeras
cap1.release()
cap2.release()
cv2.destroyAllWindows()
