from PIL import Image

def Bits_to_text( byte ):
    return chr(int( byte, 2))

def Get_last_bit( byte ):

    return bin(byte)[2:].zfill(8)[7]

def Show( path_image ):
    image = Image.open( path_image )
    pixels = image.load()
    size = image.size

    text = ""
    byte = ""

    for x in range( size[0] ):
        for y in range( size[1] ):
            byte += Get_last_bit( pixels[x,y][0] )
            if byte == '11111111':
                return text
            elif len(byte) == 8:
                text += Bits_to_text(byte)
                byte = ""
            byte += Get_last_bit( pixels[x,y][1] )
            if byte == '11111111':
                return text
            elif len(byte) == 8:
                text += Bits_to_text(byte)
                byte = ""
            byte += Get_last_bit( pixels[x,y][2] )
            if byte == '11111111':
                return text
            elif len(byte) == 8:
                text += Bits_to_text(byte)
                byte = ""
