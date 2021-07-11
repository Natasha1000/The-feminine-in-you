import os
folder="images\\gallery"
files=os.listdir(folder)
for file in files:
	path=folder+"\\"+file
	corrected_path="/".join(path.split("\\"))
	print(f'<img src="{corrected_path}" width="30%">')

	



