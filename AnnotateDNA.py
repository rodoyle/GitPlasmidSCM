from sys import argv

import re, DNAFeature
		
def cleanDNA(sequence):
	return re.sub('\W|\d','',sequence) #scrub anything but letters

if __name__ == "__main__":
	print argv
	script, filename, name, pattern = argv
	pattern = r'(?P<'+name+r'>'+pattern+r')'
	print pattern
	feat1= re.compile(pattern)
	Seqfile = open(filename, 'r')
	construct = cleanDNA(Seqfile.read())
	feat1hits = feat1.finditer(construct)

	print "Analyzing DNA sequence from %s. Sequence found is "
	print filename
	print Seqfile
	
	print "Searching for ", name, " ..."
	if feat1hits:
		print "Matches found"
		for match in feat1hits:
			print "%02d-%02d: %s" %(match.start(), match.end(), match.group(0))
	else:
		print "FeaSture not found"
	
	
	""" How do you find matches that overlap, or that wrap back to
	the begining of the circular plasmid"""
