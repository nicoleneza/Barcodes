import cv2
from pyzbar.pyzbar import decode

# Load the image containing the PDF417 barcode
image_path = "new_pdf417.png"  # Change this to your barcode image file
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print(f"Error: Could not load image at {image_path}. Check the file path!")
    exit()

# Decode the barcode
barcodes = decode(image)

if not barcodes:
    print("No PDF417 barcode detected!")
else:
    for barcode in barcodes:
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type
        print(f"Detected {barcode_type} barcode: {barcode_data}")

        # Draw a rectangle around the barcode
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show the image with the barcode highlighted (optional)
    cv2.imshow("PDF417 Barcode", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
