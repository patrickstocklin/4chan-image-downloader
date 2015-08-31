from BeautifulSoup import BeautifulSoup
import urllib, urllib2
import os
import sys

if len(sys.argv) > 1:
	print "Grabbing images from thread: " + sys.argv[1]
	url = sys.argv[1]
	thread = urllib2.urlopen('https://boards.4chan.org/wg/thread/6302506/caturday')
	threadID = url.split('/')[-1]
	print "threadID: " + threadID
	soup = BeautifulSoup(thread)
	images = soup.findAll('a',attrs={'class':'fileThumb'})
	num = len(images)
	for i in range(0, num):
		link = "http://" + images[i]['href'][2:]
		filename = link.split('/')[-1]
		print link
		print filename
		resource = urllib.urlopen(link)
		output = open(os.path.join('/home/pat/Pictures/Wallpapers', filename), 'wb')
		output.write(resource.read())
		output.close()

	print "Saved " + num + " Images"
else:
	print "Invalid Number of Arguments"