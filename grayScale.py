import cv2

# Görseli oku
resim = cv2.imread("images/cilek.jpg")  # images klasörüne koyduğun görseli okur

# Siyah-beyaz (grayscale) yap
gri_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

# Gri resmi kaydet
cv2.imwrite("images/cilek_gri.jpg", gri_resim)

# Görselleri göster
cv2.imshow("Orijinal", resim)
cv2.imshow("Siyah-Beyaz", gri_resim)

cv2.waitKey(0)            # pencereyi açık tut
cv2.destroyAllWindows()   # tüm pencereleri kapat
