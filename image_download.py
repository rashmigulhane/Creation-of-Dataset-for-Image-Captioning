import os
f = open("/home/rashmi/Desktop/rp/file_formating/files/url_index.txt")
f1 = open("/home/rashmi/Desktop/rp/file_formating/files/no_images.txt",'w')
path1="/home/rashmi/Desktop/rp/file_formating/files/img_unprocessed/"

for line in f:
	try:
		lines = line.split("\t",1)
		print lines[1]
		os.system("wget  -P /home/rashmi/Desktop/rp/file_formating/files/img_unprocessed  -A jpeg,jpg,bmp,gif,png  -R html " + lines[1])
		os.system("rm " + path1 + "*.*~")
		cnt = os.listdir(path1)
		if cnt>0:
			b = os.path.getsize(path1 + cnt[0])#f2 = open(path1 + cnt[0]).read()
			if b>40:
				os.rename(path1 + cnt[0],"/home/rashmi/Desktop/rp/file_formating/files/processed/"+lines[0])
		else:
			f1.write("\t" + lines[0])
	except:
		
		f1.write(" " +lines[0])

f1.close()
