from PIL import Image, ImageFont, ImageDraw

image = Image.open('MODULO02/DIA05/encanto.jpg')
print(image.size)
print(image.format)
print(image.mode)

# convertir a blanco y negro y mostrar 
image_black_white = image.convert('L')
#image_black_white.show()

# redimensionar
width, height = image.size

print(f'ancho : {width}' )
print(f'alto : {height}' )

new_width = width//5 
new_height = height//5

print(f'nuevo ancho : {new_width}' )
print(f'nuevo alto : {new_height}' )

image_short = image.resize((new_width, new_height))
#image_short.show()

draw = ImageDraw.Draw(image)
font = ImageFont.truetype('MODULO02/DIA05/Roboto-Bold.ttf', 100)
draw.text(
    (10, 0),
    "ROSITA EN ENCANTO",
    (255, 0, 0),  # color rojo
    font
)

image.show()