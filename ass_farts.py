import urllib
import urllib2
import requests
import time

url = """https://ixquick-proxy.com/do/spg/show_picture.pl?l=english&rais=1&oiu=http%3A%2F%2Fwww.wallpapersxl.com%2Fget%2F6278005&sp=b17063d78ad6224e99be5d55027b2519"""

t = time.sleep(10)
while t > 1:
    print "doing stuff so wait bih"

f = raw_input("give me url you wan to hackz:  ")

print "downloading weebsite data...."
time.sleep(10)

print urllib.urlretrieve(url, "hackz.html")

print "getting all the specified hacker things"
time.sleep(5)

g = urllib2.urlopen(url)

data = g.read()

with open("hacks.html", "wb") as pic:
    pic.write(data)

print "getting more important stuffs"

r = requests.get(url)

with open("UltimitHaccerBro.html", "wb")as pic2:
    pic2.write(r.content)




