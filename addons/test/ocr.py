
import cv2
import pytesseract




def ocr_core(contrat):
    text = pytesseract.image_to_string(contrat)
    return text

contrat = cv2.imread('contrat2.jpg')


# obtenir une image en niveaux de gris
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)


# Le seuillage d'image
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


contrat = get_grayscale(contrat)
contrat = thresholding(contrat)
contrat = remove_noise(contrat)

print(ocr_core(contrat))


