from PIL import Image

def Text_to_bits( text ):
    bits_list = []
    for i in text:
        for bit in bin(ord(i))[2:].zfill(8):
            bits_list.append( bit )
    for i in range( 8 ):
        bits_list.append( 1 )
    return bits_list

def Change_last_bit( byte, bit ):
    return int(bin(byte)[2:].zfill(8)[:-1] + str(bit) )

def Hide( path_image, path_out_image, text ):
    image = Image.open( path_image )
    size = image.size
    pixels = image.load()

    bits_list = Text_to_bits( text )
    ctn = 0

    for x in range( size[0] ):
        for y in range(size[1]):
            red = pixels[x,y][0]
            green = pixels[x,y][1]
            blue = pixels[x,y][2]
            if ctn < len(bits_list):
                red = int(bin(red)[2:].zfill(8)[:-1] + str(bits_list[ctn]),2 )
                ctn += 1
            if ctn < len(bits_list):
                green = int(bin(green)[2:].zfill(8)[:-1] + str(bits_list[ctn]),2 )
                ctn += 1
            if ctn < len(bits_list):
                blue = int(bin(blue)[2:].zfill(8)[:-1] + str(bits_list[ctn]),2 )
                ctn += 1

            pixels[x,y] = (red ,green,blue)

            if ctn == len(bits_list):
                image.save(path_out_image)
                return True
