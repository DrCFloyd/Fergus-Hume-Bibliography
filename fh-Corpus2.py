import urllib2
url = 'http://www.gutenberg.org/cache/epub/55376/pg55376.txt'

response = urllib2.urlopen(url)
webContent = response.read()

f = open('piccadillyPuzzle.txt', 'w')
f.write(webContent)
f.close
#
url = 'http://www.gutenberg.org/cache/epub/55348/pg55348.txt'

response = urllib2.urlopen(url)
webContent = response.read()

f = open('redHeaded.txt', 'w')
f.write(webContent)
f.close
#
url = 'http://www.gutenberg.org/cache/epub/54979/pg54979.txt'

response = urllib2.urlopen(url)
webContent = response.read()

f = open('yellowHolly.txt', 'w')
f.write(webContent)
f.close
#
url = 'http://www.gutenberg.org/cache/epub/55101/pg55101.txt'

response = urllib2.urlopen(url)
webContent = response.read()

f = open('whiteRoom.txt', 'w')
f.write(webContent)
f.close
#
