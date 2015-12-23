import json
import codecs
import sys
import os

path = sys.path[0]
#print path  #relative path   os.path.join(dirpath,name)

'''
#Get the relative path of json file.
jsonFile = "E:\Shenjing\Python\Python\JsonMerge\CDN\ui\page\page.json"
jsonData = codecs.open(jsonFile,'r','utf_8_sig')
jsonString = jsonData.read()
#print jsonString
jsonString2 = json.loads(jsonString)
#print jsonString2['Name']

URL = jsonString2['RelativePath']
#print URL 	
jsonData.close()
'''
def getDocOrFile(path):
	doc = []
	for i in os.walk(path):
		doc = doc + i[2]
	return doc
	
def getRelativePath(jsonDoc):
	jsonData = codecs.open(jsonDoc,'r','utf_8_sig')
	jsonString = jsonData.read()
	jsonStringPthon = json.loads(jsonString)
	return jsonStringPthon['Name']
	
docOrFile = getDocOrFile(path)
print docOrFile

for doc in docOrFile:
	print type(doc)
	'''
	if "json" in doc:
		Print doc
		#getRelativePath(doc)
		'''
	
'''
for docOrFile in os.walk(path):
	#print docOrFile
	absolutePath = docOrFile [0]
	print absolutePath
	doc = docOrFile[2]  #doc is "yuan zu"
	for i in doc:
		#print i
		if "json" in i:
			print "ok"  #i is the json doc
'''
