import urllib
import re

def getHtml(url):
 page=urllib.urlopen(url)
 html=page.read()
 return html
	
def getImg(html):
 reg=r'src="(.+?\.jpg)"'	
 imgre=re.compile(reg)
 imglist=re.findall(imgre,html)
 x=1
 for imgurl in imglist:
    urllib.urlretrieve(imgurl,"./img/%s.jpg" %x)
    x+=1
 return imglist
html=getHtml("http://www.zuofan.cn")
print getImg(html) 
print 'success'
		