from PIL import Image
import os
folder="images\\gallery"
files=os.listdir(folder)
for file in files:
	if os.path.isfile(folder+"\\"+file):
		print(folder+"\\"+file)
		basewidth = 300
		img = Image.open(folder+"\\"+file)
		wpercent = (basewidth / float(img.size[0]))
		hsize = int((float(img.size[1]) * float(wpercent)))
		img = img.resize((basewidth, hsize), Image.LANCZOS)
		img.save(folder+"\\300\\"+file)

	



