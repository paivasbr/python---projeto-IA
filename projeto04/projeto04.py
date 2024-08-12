import cv2
from cvzone.HandTrackingModule import HandDetector

webcam = cv2.VideoCapture(0)
rastreador = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    sucesso, imagem = webcam.read()
    coordenadas, hands_image = rastreador.findHands(imagem)

    print(coordenadas)

    cv2.imshow("python - projeto_IA", imagem)

    if cv2.waitKey(1) != -1:
        break

webcam.release()
cv2.destroyAllWindows()