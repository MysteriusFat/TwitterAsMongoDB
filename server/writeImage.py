from PIL import Image

def Text_to_bits( text ):
    bits_list = []
    for i in text:
        for bit in bin(ord(i))[2:].zfill(8):
            bits_list.append( bit )
    bits_list.append( 0xff )
    return bits_list

def Change_last_bit( byte, bit ):
    return int(bin(byte)[2:].zfill(8)[:-1] + str(bit))

def Hide( path_image, text ):
    image = Image.open( path_image )
    pixels = image.load()
    size = image.size

    bits_list = Text_to_bits( text )
    x = y = 0

    for i in range(0 , len(bits_list), 3):
        if i < len(bits_list  ):
            red = pixels[x,y][0], bits_list[i]
        if i+1 < len(bits_list  ):
            green = pixels[x,y][1], bits_list[i+1]
        if i+2 < len(bits_list  ):
            blue = pixels[x,y][2], bits_list[i+2]

        x += 1
        if x == size[0]:
            x = 0
            y += 1
            if y == size[1]:
                y = 0

    image.save('salida.jpg')
    return True

Hide('./test.jpg',"MENSAJE DE PRUEBA")
