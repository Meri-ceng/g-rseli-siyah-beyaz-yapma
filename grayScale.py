import cv2

resim = cv2.imread("images/cilek.jpg")  

gri_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

cv2.imwrite("images/cilek_gri.jpg", gri_resim) #yeni ve gri resmimi kaydettim

cv2.imshow("Orijinal", resim)
cv2.imshow("Siyah-Beyaz", gri_resim)

cv2.waitKey(0)           
cv2.destroyAllWindows() 
