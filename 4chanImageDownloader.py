from BeautifulSoup import BeautifulSoup
import urllib, urllib2
import os
import sys

#Where we want to store all images
directory = "/home/pat/Pictures/Wallpapers/"

try:
	print "Grabbing images from thread: " + sys.argv[1]
	thread = urllib2.urlopen(sys.argv[1])
	threadID = sys.argv[1].split('/')[-1]
	print "threadID: " + threadID
	soup = BeautifulSoup(thread)
	images = soup.findAll('a',attrs={'class':'fileThumb'})
	num = len(images)

	if not os.path.exists(directory + threadID):
		os.makedirs(directory + threadID)

	for i in range(0, num):
		link = "http://" + images[i]['href'][2:]
		if link[-3:] == "jpg":
			filename = threadID + str(i) + ".jpg"
		elif link[-3:] == "png":
			filename = threadID + str(i) + ".png"
		elif link[-3:] == "gif":
			filename = threadID + str(i) + ".gif"
		print "Downloading ", link
		print "Saving as, ", filename
		resource = urllib.urlopen(link)
		output = open(os.path.join(directory + threadID, filename), 'wb')
		output.write(resource.read())
		output.close()

	print "Saved ", num, " Images"
except IndexError, e:
	print "Invalid Number of Arguments: " + str(e)
except OSError, e:
	print str(e)
except urllib2.URLError, e:
	print str(e)
except urllib2.HTTPError, e:
	print str(e)
