from PIL import Image

def Bits_to_text( bits ):
    pass

def Get_last_bit( x ):
    pass

def Show( path_image ):
    image = Image.open( path_image )
    pixels = image.load()
    size = image.size
