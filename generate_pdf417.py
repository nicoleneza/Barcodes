import pdf417gen as pdf417

data = "this is a pdf417 barcode example."

codes = pdf417.encode(data, columns=5)
pdf417_image = pdf417.render_image(codes, scale=3)
pdf417_image.save("pdf417_code.png")
print("PDF417 code saved as pdf417_code.png")

pdf417_image.show()