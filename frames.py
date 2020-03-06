import cv2
import sys

#Desenvolvedor: Iago Oliveira

#tempo_frame significa em quanto em quanto tempo um frame será capturado (variável numérica)
#video significa o nome do video (variável do tipo string)
#nome_frame significa o nome que o frame será salvo

tempo_frame = sys.argv[1:]
nome_video = sys.argv[2:]
nome_frame = sys.argv[3:]

tempo_frame = int(tempo_frame[0])
nome_video = str(nome_video[0])
nome_frame = str(nome_frame[0])

def gerar_frames(tempo_frame, nome_video, nome_frame):
   tempo = tempo_frame * 1000
   captura = cv2.VideoCapture(nome_video)
   indice_frame = 0
   while captura.isOpened():
      captura.set(cv2.CAP_PROP_POS_MSEC,(indice_frame*tempo))
      res, frame = captura.read()
      nome_do_frame = nome_frame + "_" + str(indice_frame) + ".jpg"
      cv2.imwrite(nome_do_frame, frame)
      indice_frame = indice_frame + 1

   captura.release()

gerar_frames(tempo_frame, nome_video, nome_frame)
