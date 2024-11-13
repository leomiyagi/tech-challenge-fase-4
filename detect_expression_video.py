import cv2
from deepface import DeepFace
import os
import numpy as np
from tqdm import tqdm
import face_recognition


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

    # Loop para processar cada frame do vídeo
    for _ in tqdm(range(total_frames), desc="Processando vídeo"):
        # Ler um frame do vídeo
        ret, frame = cap.read()

        # Se não conseguiu ler o frame (final do vídeo), sair do loop
        if not ret:
            break

        rgb_frame = frame[:, :, ::-1]

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        profile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')
            
        faces = face_cascade.detectMultiScale(rgb_frame, scaleFactor=1.1, minNeighbors=5)
        profile_faces = profile_cascade.detectMultiScale(rgb_frame, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:


            face_roi = rgb_frame[y:y+h, x:x+w]

            # Verify if the detected face is actually a face using face_recognition
            face_locations = face_recognition.face_locations(face_roi)

            if face_locations:
                # If face_recognition confirms the face, draw a rectangle around it
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

                try:

                    analysis = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)

                    if isinstance(analysis, list) and len(analysis) > 0:
                        dominant_emotion = analysis[0]['dominant_emotion']
                    else:
                        dominant_emotion = "Unknown"

                except Exception as e:
                    dominant_emotion = "Error"
                    print(f"Error analyzing emotion: {e}")

                cv2.putText(frame, dominant_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

        for (x, y, w, h) in profile_faces:

            face_roi = rgb_frame[y:y+h, x:x+w]

            # Verify if the detected face is actually a face using face_recognition
            face_locations = face_recognition.face_locations(face_roi)

            if face_locations:
                # If face_recognition confirms the face, draw a rectangle around it
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

                try:

                    analysis = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)

                    if isinstance(analysis, list) and len(analysis) > 0:
                        dominant_emotion = analysis[0]['dominant_emotion']
                    else:
                        dominant_emotion = "Unknown"

                except Exception as e:
                    dominant_emotion = "Error"
                    print(f"Error analyzing emotion: {e}")

                cv2.putText(frame, dominant_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
           
        out.write(frame)

    # Liberar a captura de vídeo e fechar todas as janelas
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Caminho para o arquivo de vídeo na mesma pasta do script
script_dir = os.path.dirname(os.path.abspath(__file__))
input_video_path = os.path.join(script_dir, 'video.mp4')  # Substitua 'meu_video.mp4' pelo nome do seu vídeo
output_video_path = os.path.join(script_dir, 'output_video.mp4')  # Nome do vídeo de saída

# Chamar a função para detectar emoções no vídeo e salvar o vídeo processado
detect_emotions(input_video_path, output_video_path)