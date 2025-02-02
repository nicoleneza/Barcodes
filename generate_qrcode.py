import qrcode

# Data to encode in the QR code
data = "https://benax.rw"  # Change this to any URL or text you want

# Generate the QR code
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
    box_size=10,  # Size of each box in pixels
    border=4,  # Border thickness
)

qr.add_data(data)
qr.make(fit=True)

# Create and save the QR code image
img = qr.make_image(fill="black", back_color="white")
img.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png' 🎉")
