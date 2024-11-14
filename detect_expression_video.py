import cv2
from deepface import DeepFace
import os
from tqdm import tqdm

from insightface.app import FaceAnalysis

def detect_emotions(video_path, output_path):
    # Capturar vídeo do arquivo especificado
    cap = cv2.VideoCapture(video_path)

    # Verificar se o vídeo foi aberto corretamente
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return

    # Obter propriedades do vídeo
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Definir o codec e criar o objeto VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec para MP4
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    app = FaceAnalysis()
    app.prepare(ctx_id=0)  # Use ctx_id=-1 for CPU

    # Loop para processar cada frame do vídeo
    for _ in tqdm(range(total_frames), desc="Processando vídeo"):
        # Ler um frame do vídeo
        ret, frame = cap.read()

        # Se não conseguiu ler o frame (final do vídeo), sair do loop
        if not ret:
            break

        rgb_frame = frame[:, :, ::-1]

        faces = app.get(rgb_frame)

        for face in faces:
            box = face.bbox.astype(int)

            cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (255, 0, 0), 2)

            face_roi = rgb_frame[box[1]:box[3], box[0]:box[2]]

            try:

                analysis = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)

                if isinstance(analysis, list) and len(analysis) > 0:
                    dominant_emotion = analysis[0]['dominant_emotion']
                else:
                    dominant_emotion = "Unknown"

            except Exception as e:
                dominant_emotion = "Error"
                print(f"Error analyzing emotion: {e}")

            cv2.putText(frame, dominant_emotion, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

        # Escrever o frame processado no arquivo de vídeo de saída   
        out.write(frame)

    # Liberar a captura de vídeo e fechar todas as janelas
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Caminho para o arquivo de vídeo na mesma pasta do script
script_dir = os.path.dirname(os.path.abspath(__file__))
input_video_path = os.path.join(script_dir, 'video.mp4')
output_video_path = os.path.join(script_dir, 'output_video_11.mp4')  # Nome do vídeo de saída

# Chamar a função para detectar emoções no vídeo e salvar o vídeo processado
detect_emotions(input_video_path, output_video_path)