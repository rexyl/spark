"""wiki.py"""
import wikipedia
bd = wikipedia.page("big data")
directory = 'wikiset/'
wf = open(directory+'home','w')
wf.write(bd.content.encode('utf8'))
wf.close()
for l in bd.links:
	try:
		f = open(directory+l,'w')
		extern = wikipedia.page(l.encode('utf8'))
		f.write(extern.content.encode('utf8'))
		f.close()
	except:
		pass