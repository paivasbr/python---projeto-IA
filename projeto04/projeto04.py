import cv2
from cvzone.HandTrackingModule import HandDetector

webcam = cv2.VideoCapture(0)
rastreador = HandDetector(detectionCon=0.8)

while True:
    sucesso, imagem = webcam.read()
    cv2.imshow("python - projeto_IA", imagem)

    if cv2.waitKey(1) != -1:
        break

webcam.release()
cv2.destroyAllWindows()