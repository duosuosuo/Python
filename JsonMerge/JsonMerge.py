import json
import codecs

import sys,os

path = sys.path[0]
print path

jsonFile = "E:\Shenjing\Python\Python\JsonMerge\CDN\ui\page\page.json"
jsonData = codecs.open(jsonFile,'r','utf_8_sig')
jsonString = jsonData.read()
#print jsonString
jsonString2 = json.loads(jsonString)
print jsonString2['Name']

URL = jsonString2['RelativePath']
print URL 	
jsonData.close()