from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
import argparse
import io

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
							help = "Default: 15.0; Sharpness for the image")
							
	argParser.add_argument("-co", "--contrast",
							metavar = "float",
							type = float,
							help = "Default: 1.25; Contrast for the image")
							
	argParser.add_argument("-cf", "--color-factor",
							metavar = "float",
							type = float,
							help = "Default: 1.25; 0.0 represents black and white; 1.0 represents full, original color; and going further increases the vibrance of the color.")
							
	argParser.add_argument("-q", "--quality",
							metavar = "int",
							type = int,
							help = "Default: 65; Quality of output jpeg from 0 to 100")
							
	argParser.add_argument("-r", "--repetitions",
							metavar = "int",
							type = int,
							help = "Default: 1; How many times you want to apply the specified settings to the image. WARNING: unfortunately, each repitition opens and writes the file!")
							
	argParser.add_argument("output",
							metavar = "output",
							type = str)
							
	argParser.add_argument("--profile", "-p",
							metavar = "name",
							type = str,
							default = "regular",
							help = "Default: regular; Different profiles to use. Profiles are \"default\", \"colorful\", \"sharp\", \"contrast\", and \"cook\".")
							
	profiles = {
				"default": { "sharp": 1.25, "con": 1.25 , "col": 1.25, "qual": 65, "rep": 1 },
				"contrast": { "sharp": 1.5, "con": 10, "col": 1, "qual": 50, "rep": 10 },
				"sharp": { "sharp": 10, "con": 1.25, "col": 1, "qual": 50, "rep": 10 },
				"colorful": { "sharp": 1, "con": 1, "col": 10, "qual": 50, "rep": 10 },
				"cook": {"sharp": 25, "con": 3, "col": 5, "qual": 1, "rep": 5}
			}
	
	args = argParser.parse_args()
	
	profile = profiles[args.profile] if args.profile in profiles else profiles["default"]
	profile["sharp"] = args.sharpness if args.sharpness != None else profiles[args.profile]["sharp"]
	profile["con"] = args.contrast if args.contrast != None else profiles[args.profile]["con"]
	profile["col"] = args.color_factor if args.color_factor != None else profiles[args.profile]["col"]
	profile["qual"] = args.quality if args.quality != None else profiles[args.profile]["qual"]
	profile["rep"] = args.repetitions if args.repetitions != None else profiles[args.profile]["rep"]
	
	for i in range(profile["rep"]):
		img = Image.open(args.input)
		img = memeImage(img, profile["sharp"], profile["con"], profile["col"])
		img.save(args.output, format = "JPEG", quality = profile["qual"])
		if(profile["rep"] > 1):
			print("(" + str(i + 1) + "/" + str(profile["rep"]) + ")")
		
	
if __name__ == "__main__":
	main()