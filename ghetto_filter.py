from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
import argparse

# takes PIL image, memes image, and returns new image
def memeImage(inImg, sharpness_factor = 15, contrast_factor = 1.25, color_factor = 1.25):
	# split this into 3 lines so that it's easie to report where something goes wrong
	tempImg = ImageEnhance.Color(inImg).enhance(color_factor)
	tempImg = ImageEnhance.Contrast(tempImg).enhance(contrast_factor)
	tempImg = ImageEnhance.Sharpness(tempImg).enhance(sharpness_factor)
	return tempImg
	
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
							default = 15.0,
							help = "Default: 15.0; Sharpness for the image")
							
	argParser.add_argument("-co", "--contrast",
							metavar = "float",
							type = float,
							default = 1.25,
							help = "Default: 1.25; Contrast for the image")
							
	argParser.add_argument("-cf", "--color-factor",
							metavar = "float",
							type = float,
							default = 1.25,
							help = "Default: 1.25; 0.0 represents black and white; 1.0 represents full, original color; and going further increases the vibrance of the color.")
							
	argParser.add_argument("-q", "--quality",
							metavar = "int",
							type = int,
							default = 65,
							help = "Default: 65; Quality of output jpeg from 0 to 100")
							
	argParser.add_argument("-r", "--repetitions",
							metavar = "int",
							type = int,
							default = 1,
							help = "Default: 1; How many times you want to apply the specified settings to the image.")
							
	argParser.add_argument("output",
							metavar = "output",
							type = str)
	
	args = argParser.parse_args()
	
	img = Image.open(args.input)
	
	for i in range(args.repetitions):
		img = memeImage(img, args.sharpness, args.contrast, args.color_factor)
	
	img.save(args.output, format = "JPEG", quality = args.quality)
	
if __name__ == "__main__":
	main()