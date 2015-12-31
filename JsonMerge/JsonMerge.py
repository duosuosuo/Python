#!/usr/bin/python
import DefLib
import os

from DefLib import getallFileWithAbPath
from DefLib import getRelativePath
from DefLib import getUnity3dFileName
from DefLib import addVersion
from DefLib import getAllJsonFile
from DefLib import JsonCounter
from DefLib import addVersion
'''
#path = sys.path[0]  #relative path   os.path.join(dirpath,name)
pathCopyFrom =  "/Users/Jason/ShenJing/Python/JsonMerge/CDN"
pathCopyTo = "/Users/Jason/ShenJing/Python/JsonMerge/copyTo"
'''
pathCopyFrom =  "E:\Shenjing\Python\Python\JsonMerge\CDN"
pathCopyTo = "E:\Shenjing\Python\Python\JsonMerge\copyTo"


allJsonFile = getAllJsonFile(pathCopyTo)

latestJsonVersion = []

for oneJsonFile in allJsonFile:
	p,f = os.path.split(oneJsonFile)
	if f[-7:] == "_1.json":
		s = f[:-7]
		counter = JsonCounter(p,s)
		f = s + "_" + str(counter) + ".json"
		latestVersionJsonWithPath = os.path.join(p,f)
		addVersion(latestVersionJsonWithPath,counter)
		latestJsonVersion.append(latestVersionJsonWithPath)

JsonMergeFile = []
for onefile in latestJsonVersion:
	jsonData = codecs.open(onefile,'r','utf_8_sig')
	JsonMergeFile.append(jsonData)
print JsonMergeFile



	#jsonData.close()



