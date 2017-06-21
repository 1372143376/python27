import re
import urllib
import urllib2
import os


def getHtml(url):
	 page=urllib.urlopen(url)
	 html=page.read()
	 return html
	
def getImg(html):
	 reg=r'"objURL":"(.*?)"'	
	 imgre=re.compile(reg)
	 imglist=re.findall(imgre,html)
	 print imgre
	 l=len(imglist)
	 print l
	 return imglist

def downLoad(urls,path):
 index=1
 for url in urls:
	  print("downind",url)
	  filename=os.path.join(path,str(index)+".jpg")
	  urllib.urlretrieve(url,filename)
	  index+=1

html=getHtml("https://image.baidu.com/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs2&word=%E8%B6%85%E7%BA%A7%E6%90%9E%E7%AC%91%E5%9B%BE%E7%89%87%E7%AC%91%E6%AD%BB%E4%BA%BA&oriquery=%E6%9C%80%E8%BF%91%E5%BE%88%E7%81%AB%E7%9A%84%E6%90%9E%E7%AC%91%E5%9B%BE%E7%89%87&ofr=%E6%9C%80%E8%BF%91%E5%BE%88%E7%81%AB%E7%9A%84%E6%90%9E%E7%AC%91%E5%9B%BE%E7%89%87&hs=2")
Savepath="D:\soft\python27\image\imgs"
downLoad(getImg(html),Savepath)
		