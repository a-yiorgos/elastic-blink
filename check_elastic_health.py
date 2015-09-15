
import json
import urllib2
import sys

hostname = None
port = 9200
blink = None

if hostname is None:
  sys.exit("You need to set the hostname")

if blink is None:
  sys.exit("You need to set the blinkstick public URL")

elastic = "http://" + hostname + ":" + str(port) + "/_cluster/health"

req  = urllib2.Request(elastic)
response = urllib2.urlopen(req)
r = response.read()
j = json.loads(r)

if  j['status'] != "green":
	print j['status']

blink = blink + "/" + j['status'] + ".json"

req = urllib2.Request(blink)
response = urllib2.urlopen(req)
r = response.read()
j = json.loads(r)

