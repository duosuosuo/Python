#!/usr/bin/python
import DefLib
import os
import codecs
import json
import sys

from DefLib import getallFileWithAbPath
from DefLib import getRelativePath
from DefLib import getUnity3dFileName
from DefLib import getAllJsonFile
from DefLib import JsonCounter
from DefLib import getAllLstJsonFile
from DefLib import getVersion
from DefLib import allJsonToArray

def Merge(pathCopyTo):
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

	#Add version and merge to dict 
	bigJsonArray = []
	allLstVersionJsonWithPath = getAllLstJsonFile(allJsonFile)
	for oneJsonFile in allLstVersionJsonWithPath:
		version = getVersion(oneJsonFile)
		bigJsonArray = allJsonToArray(oneJsonFile,bigJsonArray,version)
	bigJsonDict = {}
	bigJsonDict["json"] = bigJsonArray
	bigJson = json.dumps(bigJsonDict)

	#Create Finally big json file
	bigJsonFile = open(bigJsonFileWithPath,'w')
	bigJsonFile.write(bigJson)
	bigJsonFile.close()