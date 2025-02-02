from pylibdmtx.pylibdmtx import decode
import cv2

# Read image in grayscale
image = cv2.imread("new_qrcode.png", cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded properly
if image is None:
    print("Error: Unable to load image. Check the file path.")
else:
    # Decode the Data Matrix barcode
    decoded_objects = decode(image)

    # Iterate through decoded objects
    for obj in decoded_objects:
        data = obj.data.decode("utf-8")
        print("Decoded Data:", data)

    # Save the annotated image
    output_file = "decoded_datamatrix.png"
    cv2.imwrite(output_file, image)
    print(f"Annotated image saved as {output_file}")

    # Display the image with annotations
    cv2.imshow("Barcode with Annotation", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
