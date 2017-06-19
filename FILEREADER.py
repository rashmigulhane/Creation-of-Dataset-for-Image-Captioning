#files to be created 
import os
from collections import defaultdict
'''
url_url = "/media/administrator/F/dataset_reformat/files/url_url.txt"
query_url = "/media/administrator/FE66077E66073745/rp/dataset_reformat/files/query_url.txt"
url_data = "/media/administrator/FE66077E66073745/rp/dataset_reformat/files/url_data.txt"
url_index = "/media/administrator/FE66077E66073745/rp/dataset_reformat/files/url_index.txt"
'''

url_url = "/home/rashmi/Desktop/rp/file_formating/files/url_url.txt"
query_url = "/home/rashmi/Desktop/rp/file_formating/files/query_url.txt"
url_data = "/home/rashmi/Desktop/rp/file_formating/files/url_data.txt"
url_index = "/home/rashmi/Desktop/rp/file_formating/files/url_index.txt"

main_path = "/home/rashmi/Desktop/rp/file_formating/football"
main_files =os.listdir(main_path)
url_data_f = open(url_data,'w')
url_index_f = open(url_index,'w')
#query_url_f = open(query_url,'w')
url_url_f = open(url_url,'w')
query_url_f = open(query_url,'w')
all_urls = {}
globall = 0
query_url_f = open(query_url,'w')
all_urls_list = []
for l in main_files:
    l = l.strip()
    l = str(l)
    #ld = l.replace(" ","\ ")	
    if (l.find(".")==-1):
	IN =os.path.join(main_path,l)
	#print IN
	b =  os.listdir(IN)
	#print b
	ass = l + "_urls"
	cnt = 0
	while cnt < len(b):
		if b[cnt].find("urls")>-1:
			url = b[cnt]
		cnt=cnt+1
	cnt = 0
	while cnt < len(b):
		if b[cnt].find("_Text")>-1:
			text = b[cnt]
		cnt=cnt+1
	
	#indexx = b.index("onside kick in football_urls")
	
	IN_url = os.path.join(IN,url)
	IN_text = os.path.join(IN,text)
	#print IN 
	l_query = str(IN)
	#l_text =  main_path + "/" +str(l) + "/" + str(l)+"_Text/"
	#print l_text
	#print l_query
	f = open(IN_url)
	inside_main_files =os.listdir(IN_text + "/" )
	#print "Containe of main file"
	#print inside_main_files
	
	for line in f:
		try:
			url_details = line.split(":",1)
			#print all_urls.has_key(url_details[1].strip())
			#print url_details[1]
			#serachng key in arraylist
			rew = 0
			utl_1 = "false"
			val_in =""
			while rew < len(all_urls_list):
				if(all_urls_list[rew][0] == url_details[1]):
					print "found"
					utl_1="true"
					val_in = all_urls_list[rew][1]
				rew=rew+1
			if utl_1=="false":
			#print IN_text
				print "INNNNNNN"
				IN_file = os.path.join(IN_text,url_details[0] + ".txt")
				#print IN_file
				tempor = open(IN_file).read() 
		    		tempor = tempor.replace("\n"," ")
		   		url_data_f.write(str(globall) + "\t" + tempor + "\n")
				p = str(globall) + "\t"  +  url_details[1].strip() +"\n"
		    		url_index_f.write(p)
				p = l + "\t"  + str(globall) +"\n"
		    		query_url_f.write(p)
		    		url_url_f.write("\n" + str(globall) + "\t")
				all_urls.setdefault(url_details[1],globall)
				print "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDCCCCCCCCCCCCCCCCCCCCCCCCCCC"
			#	print all_urls
				utl_10 = []
				utl_10.append(url_details[1])
				utl_10.append(globall)
				all_urls_list.append(utl_10)
		    		globall = globall +1
			
				top_10 = IN + "/Simailar_Images/"+url_details[0] + "/" + "Similar_images_Text/"
				#print "top100000000000000000000000000000000000000"
				#print os.listdir(top_10)
				top_10_f = IN + "/Simailar_Images/"+url_details[0] + "/" + "Similar_images_urls"
				f_in = open(top_10_f)
			else:
				
				globall_2 = val_in
				IN_file = os.path.join(IN_text,url_details[0] + ".txt")
				#print IN_file
				#tempor = open(IN_file).read() 
		    		#tempor = tempor.replace("\n"," ")
		   		#url_data_f.write(str(globall) + "\t" + tempor + "\n")
				#p = str(globall) + "\t"  +  url_details[1].strip() +"\n"
		    		#url_index_f.write(p)
				p = l + "\t"  + str(globall_2) +"\n"
		    		query_url_f.write(p)
		    		url_url_f.write("\n" + str(globall_2) + "\t")
				
				top_10 = IN + "/Simailar_Images/"+url_details[0] + "/" + "Similar_images_Text/"
				#print "top100000000000000000000000000000000000000"
				#print os.listdir(top_10)
				top_10_f = IN + "/Simailar_Images/"+url_details[0] + "/" + "Similar_images_urls"
				f_in = open(top_10_f)
			for line_in in f_in:
				try:
					url_details_in = line_in.split(":",1)
					rew_2=0
					utl_1_1 = "false"
					val_in_1 = ""
					while rew_2 < len(all_urls_list):
						if(all_urls_list[rew_2][0] == url_details_in[1]):
							print "found"
							utl_1_1="true"
							val_in_1 = all_urls_list[rew][1]
						rew_2=rew_2+1
					if utl_1_1=="false":
						IN_file_in = os.path.join(top_10,url_details_in[0] + ".txt")
						tempor = open(IN_file_in).read() 
		    				tempor = tempor.replace("\n"," ")
		   				url_data_f.write(str(globall) + "\t" + tempor + "\n")
						p = str(globall) + "\t"  +  url_details_in[1].strip() +"\n"
		    				url_index_f.write(p)
						url_url_f.write(str(globall) + ",")
						all_urls.setdefault(url_details_in[1],globall)
						globall = globall +1
					else:
						#IN_file_in = os.path.join(top_10,url_details_in[0] + ".txt")
					#tempor = open(IN_file_in).read() 
	    				#tempor = tempor.replace("\n"," ")
	   				#url_data_f.write(str(globall) + "\t" + tempor + "\n")
					#p = str(globall) + "\t"  +  url_details_in[1].strip() +"\n"
	    				#url_index_f.write(p)
						url_url_f.write(str(val_in_1) + ",")
					#all_urls.setdefault(url_details_in[1],globall)
					
				except:
					print "missing inside file"
			
			#print "urlllll100000000000000000000000000000000000000"
			
		except:
			print "file missing"
	    
	#write to url_index ,url_data,url_url,query_url
	#inner_loop = 0
	#while inner_loop < len(inside_main_files):
		
	#	inner_loop = inner_loop+1    
'''
  for lm in inside_main_files:
		lm = lm.split(".")
		
		top_10_inside_main_files =os.listdir(main_path + "/" + l + "/" + "Simailar_Images"+"/"+lm[0]+"/"+"Similar_images_Text")

        print l
        query_url_f.write(str(globall) + "\t" + l   + "\n")
        globall = globall +1 
        #top_10_p = main_path + "/" + l + "/" + 
        







url_data_f = open(url_data,'w')
url_index_f = open(url_index,'w')

f = open("/home/administrator/Desktop/rp/Similar_images/Similar_images_urls")
b = "/home/administrator/Desktop/rp/Similar_images/Similar_images_Text/"

for line in f:
    url_details = line.split(":",1)
    tempor = open(b + url_details[0] + ".txt").read() 
    tempor = tempor.replace("\n"," ")
    url_data_f.write(str(globall) + "\t" + tempor + "\n")
    #url_details[1].replace("\n","")
    #formating to print in url_index file
    p = str(globall) + "\t"  +  url_details[1].strip() +"\n"
    url_index_f.write(p)
    globall =globall+1


url_data_f.close()
url_index_f.close()
'''
query_url_f.close()
url_url_f.close()
query_url_f.close()
url_index_f.close()
print "All urls"

print all_urls_list
