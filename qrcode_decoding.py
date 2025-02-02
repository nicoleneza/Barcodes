import cv2

detector = cv2.QRCodeDetector()
image = cv2.imread("new_qrcode.png")
data,points, _ = detector.detectAndDecode(image)
 
if data:
    print(f"QR Dode data: {data}")
    cv2.polylines(image, [points.astype(int)],True,(0,255,0),2)
else:
    print("No QR code detected")
    
cv2.imshow("QR Code", image)
cv2.waitKey(0)
cv2.destroyAllWindows()