""" This class defines a feature of a DNA sequence. The core function of this class is to name a sequence pattern that can be used as a search token when scanning DNA sequences for a pattern Pattern should define a regular expression string that will be used to search for the sequence of interest. You will want to sanitize this (TODO)
    	self.PDistTable= 
    	an array intended to deal with fuzzy positions#these really should be unique since they are the look up keys
     	self.layer define a layer for establishing the heirarchy of features?

		self.fttype=ftype #a holder for the type of the feature, this may need to be a more limited list

		Remember you can always add more features latter through a variety of means The most important thing is to have the name and the pattern"""
from re import compile 
class DNAFeature():
    def __init__(self, ftname='feature', pattern='', comments=''):		
		self.comments = '//DNAFeature/' #this string can be anything (xml)
		self.impattern = r'(?P<' + ftname + r'>' + pattern + r')'
		self.patternregex  = compile(pattern)
		self.ftname = ftname #easy way to access the name of the feature