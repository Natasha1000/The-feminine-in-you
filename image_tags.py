import os
folder="images\\gallery"
files=os.listdir(folder)
for file in files:
	path=folder+"\\"+file
	if os.path.isfile(path):
		corrected_path="/".join(path.split("\\"))
		print(f'		<img src="{corrected_path}" width="30%" loading="lazy">')

	



