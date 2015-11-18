from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
from io import BytesIO
import argparse

#Takes PIL image, memes image, and returns new image
def memeImage(img, sharpness_factor = 5, contrast_factor = 3, color_factor = 0.7):
	return ImageEnhance.Sharpness(ImageEnhance.Contrast(ImageEnhance.Color(img).enhance(color_factor)).enhance(contrast_factor)).enhance(sharpness_factor)
	
def main():
	argParser = argparse.ArgumentParser(description = "Ghetto Filter for image")
	
	argParser.add_argument("-i", "--input",
							metavar = "file",
							help = "Input file (Required)",
							required = True,
							type = str)
	
	argParser.add_argument("-sh", "--sharpness",
							metavar = "float",
							type = float,
							default = 5.0,
							help = "Default: 5.0; Sharpness for the image")
							
	argParser.add_argument("-co", "--contrast",
							metavar = "float",
							type = float,
							default = 3.0,
							help = "Default: 3.0; Contrast for the image")
							
	argParser.add_argument("-cf", "--color-factor",
							metavar = "float",
							type = float,
							default = 0.7,
							help = "Default: 0.7; 0.0 represents black and white; 1.0 represents full, original color; and going further increases the vibrance of the color.")
							
	argParser.add_argument("-q", "--quality",
							metavar = "int",
							type = int,
							default = 15,
							help = "Default: 15; Quality of output jpeg from 0 to 100")
							
	argParser.add_argument("output",
							metavar = "output",
							type = str)
	
	args = argParser.parse_args()
		
	memeImage(Image.open(args.input), args.sharpness, args.contrast, args.color_factor).save(args.output, format = "JPEG", quality = args.quality)
	
if __name__ == "__main__":
	main()