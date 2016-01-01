#!/usr/bin/python
import DefLib
import os
import codecs
import json
import sys

from DefLib import getallFileWithAbPath
from DefLib import getRelativePath
from DefLib import getUnity3dFileName
from DefLib import addVersion
from DefLib import getAllJsonFile
from DefLib import JsonCounter
from DefLib import addVersion
from DefLib import bigJsonToStr

#path = sys.path[0]  #relative path   os.path.join(dirpath,name)
pathCopyFrom =  "/Users/Jason/ShenJing/Python/JsonMerge/CDN"
pathCopyTo = "/Users/Jason/ShenJing/Python/JsonMerge/copyTo"

'''
pathCopyFrom =  "E:\Shenjing\Python\Python\JsonMerge\CDN"
pathCopyTo = "E:\Shenjing\Python\Python\JsonMerge\copyTo"
'''

#Get Finally big json file with path
allJsonFile = getAllJsonFile(pathCopyTo)
bigJsonFilePath = sys.path[0]
bigJsonFileName = "bigJsonFile_1.json"
bigJsonFileNum = 2
for onefile in os.listdir(bigJsonFilePath):
	if bigJsonFileName == onefile:
		bigJsonFileName = "bigJsonFile" + "_" + str(bigJsonFileNum) + ".json"
		bigJsonFileNum = bigJsonFileNum + 1
bigJsonFileWithPath = os.path.join(bigJsonFilePath,bigJsonFileName)

#Add version to latest version Json file.
allLatestJsonFile = []
strtemp = ""
for oneJsonFile in allJsonFile:
	p,f = os.path.split(oneJsonFile)
	if f[-7:] == "_1.json":
		s = f[:-7]
		counter = JsonCounter(p,s)
		f = s + "_" + str(counter) + ".json"
		latestVersionJsonWithPath = os.path.join(p,f)
		allLatestJsonFile.append(latestVersionJsonWithPath)
		addVersion(latestVersionJsonWithPath,counter)
		
#Merge json file
strtemp = bigJsonToStr(latestVersionJsonWithPath,strtemp)
bigJsonStr = "{\'Json\':[" + strtemp + "]}"
print bigJsonStr
bigJsonDict = dict(bigJsonStr)

'''
#String to dict
json.dump(bigJsonDict,open(bigJsonFileWithPath,'w'))
jsonData.close()
'''


