import barcode
from barcode.writer import ImageWriter

data = "https://benax.rw"

barcode_type = "code128"
barcode_class = barcode.get_barcode_class(barcode_type)
barcode_instance = barcode_class(data, writer=ImageWriter())

output_filename = "barcode"
barcode_instance.save(output_filename)

print(f"barcode saved as {output_filename}.png")