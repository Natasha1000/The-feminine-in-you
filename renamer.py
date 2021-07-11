import os
folder="images\\gallery"
files=os.listdir(folder)
for file in files:
	print(folder+"\\"+file,folder+"\\"+"".join(file.lower().split(" ")))
	os.rename(folder+"\\"+file,folder+"\\"+"".join(file.lower().split(" ")))



