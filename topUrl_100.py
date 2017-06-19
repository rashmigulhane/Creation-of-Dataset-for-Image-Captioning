from selenium import webdriver
from bs4 import BeautifulSoup
from urlparse import urlparse
from os.path import basename
import requests
import urllib2
import urllib
import os
import re
import sys
import preProcess as pre_process
import time

reload(sys)
sys.setdefaultencoding('UTF-8')

QUERY = raw_input("Enter word")
print "--------------Creating Directory--------------"

base = QUERY
try:
    os.stat(base)
except:
    os.makedirs(base)

location= base+"/"+QUERY+"_Text"
try:
    os.stat(location)
except:
    os.makedirs(location)

location2 = base+"/"+QUERY+"_ProcessedText"
try:
    os.stat(location2)
except:
    os.makedirs(location2)

location3 = base+"/"+QUERY+"_keywords"
try:
    os.stat(location3)
except:
    os.makedirs(location3)

img_location = base+"/"+QUERY+"_Images"
try:
    os.stat(img_location)
except:
    os.makedirs(img_location)

url = "http://galleryhip.com/red-apple-png.html"
cnt = 46
img_name = "Large_Red_Apples_PNG_Clipart.png"


def getImage(img, count, name):
    #STORE IMAGES
    #for img in img_url:
        #raw_img = urllib.urlopen(img).read()
        #add the directory for your image here 
        #DIR="/home/shuchita/Documents/3-2/SOP/code/Data/"
        #cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
        #print cntr
        #f = open(DIR + image_type + "_"+ str(cntr)+".jpg", 'wb')
        #f.write(raw_img)
        #f.close()
    if ".png" in name:
        ext = ".PNG"
    else:
        ext = ".JPG"
    try:
        urllib.urlretrieve(img,img_location+"/"+str(count)+ext)
    except:
        print "image fail to load"
        img_fail.append(count)

def getText(url, cnt, img_name, QUERY):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    print "Getting text for image " , img_name 
    f = open(location+"/"+str(cnt)+".txt", 'w')
    f1 = open(location2+"/"+str(cnt)+".txt", 'w')
    f2 = open(location3+"/"+str(cnt)+".txt", 'w')
    page_text = ""
    
    #find the image on page
    matches = [soup.find(href = re.compile(img_name)) , soup.find(src = re.compile(img_name)), soup.find(content =re.compile(img_name) )]
    try:
        tag  = next(t for t in matches if t is not None)
    except:
        tag = None
        print "Could not locate image on page"
    
    #Get alt text if available 
    try:
        alt = tag('img').get('alt')
        if not alt:
            raise exc
    except:
        try:
            alt = tag.get('alt')
            if not alt:
                raise exc
        except: 
            alt = ""
            print "alt not found"
    
    if not tag:
        print "Yet not found! Access denied!!"
        page_fail.append(cnt)
        #RANDOM
        try:
            random_p =  soup.body('p')
            num_p = len(random_p)
            num_cur  = 1
            num_found = min(num_p, 4)
            while(num_cur < num_found):
                tex = random_p[random.randint(0,num_p)].text
                if tex:
                    page_text+=tex
                num_cur+=1
        except:
            pass

    #if anchor tag or img tag =>
    elif tag.name == 'a' or tag.name == 'img':
        #Traverse until enough text is found...
        print "Is anchor or image tag"
        lis = tag.parent.parent('p')
        tag = tag.parent.parent
        try:
            while len(page_text.split(' '))<20 :
                #print "Inside while"
                for para in lis:
                    page_text += para.text + " "
                    if(len(page_text.split(' '))>300):
                        break
                tag = tag.parent
                if tag is None:
                    break
                lis = tag.parent('p')
        except:
	    print "execption for there is no text"
            pass

        #Traverse only two levels...
        # for para in tag.parent.parent('p'):
        #     print "inside prev impl, found paras"
        #     page_text += para.text + " "
        # if len(page_text.split())<20:
        #     for para in tag.parent.parent.parent('p'):
        #         page_text += para.text + " "
    
    elif tag.name == 'meta':
        for tag_elem in tag.parent('meta'):
            if tag_elem.get('content'):
                page_text += tag_elem.get('content')+ " "
    
    #write to file
    try:
        title=soup.title.contents[0].encode('ascii','ignore')
        if title is None:
            raise exc
    except:
        title = ""

    page_url_info = ""
    try:
        page_url_info = ' '.join(str(url).split('/')[3:])    
    except:
        page_url_info = ' '.join(str(url).split('/')[2:])

    page_text = title + "\n"+ alt + "\n"+ img_name+ "\n" + page_url_info + "\n" + page_text
    #print '\n', page_text
    #raw_input("check content ^^")
    f.write ('%s' %(title) + '%s' %(alt) + "\n\n")
    f.write(page_text)
    
    new_text = pre_process.process_text(page_text, QUERY, False)
#    kw_text = pre_process.process_text(page_text, QUERY, True)
    #print new_text
    #raw_input("check processed ^^")
    f1.write(new_text)
#    f2.write(kw_text)
    f.close()
    f1.close()
    f2.close()

#debug
#getText(url, cnt, img_name)

############################   MAke file for urls!!! #######################
count=0
url=[]
img_url = []
page_url = []
image_succ = []
tags = dict()
i=0
res=[]
base2 = "/home/abc/Desktop/rp_rashmi"
f3 = open(base2+"/"+"QueryDetails"+".txt", 'a')
f3.write( "\n" + QUERY + "\t");

f3.close()
if not os.path.isfile(base+"/"+QUERY+"_urls"):
    #Make the file!!! 
    f = open(base+"/"+QUERY+"_urls", "w")    
    #Trying to disable plugins to enable faster page loading
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('permissions.default.styleshet', 2)
    firefox_profile.set_preference('permissions.default.image', 2)
    firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    browser = webdriver.Firefox(firefox_profile=firefox_profile)
    query_path = "https://www.google.co.in/search?q=%s&client=ubuntu&hs=dzZ&channel=fs&gbv=2&um=1&hl=en&tbm=isch&tab=wi&oq=apple&gs_l=img.3..0l10.3517.4354.0.4630.5.5.0.0.0.0.285.1001.1j0j4.5.0.msedr...0...1ac.1.34.img..2.3.531.a5tQBcP9Fe4"
    browser.get(query_path % (QUERY.replace('_', '%20')))
    html_source = browser.page_source
    #response = requests.get("https://www.google.com/search?site=&tbm=isch&source=hp&biw=1366&bih=613&q=apple&oq=apple&gs_l=img.3...56497.57214.0.57424.5.5.0.0.0.0.265.265.2-1.1.0.msedr...0...1ac.1.64.img..4.1.264.6s-2IbourLk")
    #html_source = response.text
    soup = BeautifulSoup(html_source)
    #print soup.contents[0]
    results = soup.findAll("a")
 
    for r in results:
        try:
            if "imgres?imgurl" in r['href']:
                url.append(r['href'])
                i=i+1
                #print "\n"
                #print i
                #elem = len(r.contents)
                #print elem, r.contents[0]
                #print 1
                #print r.contents[1] 
                #print "\n\n the iorig....% molol;,;ll"+r
                
        except Exception as e:
            print e
            a=0
   
    countx=0
    
    for u in url:
       
           
           x=u.find("&imgrefurl")
           x=x             
           y = u.find("imgurl=")
           y=y+7
           url_jpg=u[y:x]
           url_jpg = urllib.unquote_plus(url_jpg)
           f.write(str(countx)+":"+str(url_jpg)+"\n")
           countx=countx+1

    f.close()

#raw_input("check file")

#Read urls from file
f = open(base+"/"+QUERY+"_urls")
a = f.readline().replace("\n", "")
while not a == "":
    url.append(a)
    a = f.readline().replace("\n", "")

page_fail = []
img_fail = []
start_time = 0
counter2=0
for im in url:
    print "url containnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn"
    print im
    print "valueee in url"
    #print url
    #print "original::: ", str(count), "\n", im
    refer_url = urllib.unquote_plus(str(im))
    refer_url = urlparse(refer_url)
   # refer_url = urllib.unquote_plus(refer_url)
    #print "\n after urlparse:: \n", refer_url
    img_url.append(refer_url.query.split("&")[0].replace("imgurl=",""))
    page_url.append(refer_url.query.split("&")[1].replace("imgrefurl=",""))
    print count
    print 'Image: ' + img_url[count] +"\n"
    print 'Page: ' + page_url[count] +"\n\n"
    img_name = basename(urlparse(str(img_url[count])).path)
    img_name = img_name.split('%')[0]
    #print img_name
    #raw_input("check name")
    #######################    GET PAGE TEXT  ########################
    f3 = open(base2+"/"+"QueryDetails"+".txt", 'a')
    f3.write(" " + str(count) +",")
    f3.close()
    try:
        start_time = time.time()
        getText(page_url[count], count, img_name, QUERY)
        
	image_succ.append(count + "\n")
    
	
    except Exception as e:
        print "exception at getText"
        print e
        if count not in page_fail:
            page_fail.append(count) 
            counter2=counter2+1
#getText(page_url[count], count, img_name, QUERY)       
    
    try:
        #getImage(img_url[count], count, img_name)
        a=0
    except:
        if count not in img_fail:
            img_fail.append(count)

    count =count+1

    if count%10 == 0:
        print "\n\n", "Could not get text from => ", page_fail 
        print "\nCould not get following images => ", img_fail 

	



while(counter2!=0):
    counter2=0
    for pg in page_fail:
        try:
            start_time = time.time()
            getText(page_url[pg], count, img_name, QUERY)
            page_fail.remove(pg)
        except Exception as e:
            print "exception at getText"
            print e
            #if count not in page_fail:
            #   page_fail.append(count) 
            counter2=counter2+1
    #getText(page_url[count], count, img_name, QUERY)       
        
        try:
            #getImage(img_url[count], count, img_name)
            a=0
        except:
            if count not in img_fail:
                img_fail.append(count)


    print "\n\n", "Could not get text from => ", page_fail 
    print "\nCould not get following images => ", img_fail 


print "\n\n", "Could not get text from => ", page_fail 
print "\nCould not get following images => ", img_fail
