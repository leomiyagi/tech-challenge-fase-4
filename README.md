# FIAP - 1IADT - Tech Challenge fase 4 - Análise de Vídeo
## Grupo 19
- Humberto Alexandre Maia Vieira
- Luiz Fernando Vilas Fonseca
- Luiz Henriques Gonçalves Carneiro de Albuquerque
- Rafael Pivetta Balbuena
- Leonardo Sunao Miyagi

# Detecção de Faces

Foram testadas algumas libs:
### Face Recognition
As faces são encontradas, porém sem muita precisão. Além disso muitos objectos que não são faces também são detectados.

### Open CV + haar cascade models
Utilizando-se DeepFace ou o open cv com alguns modelos pré-treinados de haar cascade ou mesmo uma combinação de vários haar cascade, as falsas detecções foram reduzidas, porém várias faces deixam de ser detectadas.

### InsightFace
O Insight Face, apesar de exigir um tempo maior de processamento, se mostrou bastante preciso na detecção de faces. Foi a única opção que detectou algumas faces mais difíceis do vídeo como por exemplo a mulher com ataduras no rosto ou o retrato de uma pessoa bem desfocada ao fundo.

# Identificação de Indivíduos e Emoções Predominantes

A estratégia adotada para identificar e agrupar os diferentes rostos que aparecem no vídeo e respectivamente a emoção predominante em cada um deles foi:
- Identificar cada face, salvando uma imagem
- Para cada face, salvar em um excel qual foi a emoção predominante

**(Fonseca) Explicar Tecnicamente**
  

# Detecção de Movimentos Corporais

Devido a característica do vídeo e também após experimentar várias bibliotecas de detecção de movimento corporal (Open Pose, Mediapipe, YoLo, Deepsort), concluímos que para esse Tech Challenge, nos concentraríamos em alguns movimentos pré-determinados e nos propomos a tentar detectá-los.

## Mãos levadas a face

## Aperto de mão (YOLOv11 + Roboflow)

- YOLOv11 (You Only Look Once) - Fine-Tune Aperto de Mão
- Dataset handshae https://universe.roboflow.com/meerab-z/handshake/dataset/2
