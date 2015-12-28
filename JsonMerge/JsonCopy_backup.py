#!/usr/bin/python
import json
import codecs
import sys
import os
import shutil

#path = sys.path[0]  #relative path   os.path.join(dirpath,name)
pathCopyFrom =  "/Users/Jason/ShenJing/Python/JsonMerge/CDN"
pathCopyTo = "/Users/Jason/ShenJing/Python/JsonMerge/copyTo"

def getallFileWithAbPath(path):
	allFileWithAbPath = []
	for i in os.walk(path):
		for j in i[2]:
			FileAbsolutePath = i[0] + "/" + j
			allFileWithAbPath.append(FileAbsolutePath)
	return allFileWithAbPath
	
def getRelativePath(jsonDoc):
	jsonData = codecs.open(jsonDoc,'r','utf_8_sig')
	jsonString = jsonData.read()
	jsonStringPthon = json.loads(jsonString)
	return jsonStringPthon['RelativePath']

def getUnity3dFileName(jsonDoc):
	jsonData = codecs.open(jsonDoc,'r','utf_8_sig')
	jsonString = jsonData.read()
	jsonStringPthon = json.loads(jsonString)
	return jsonStringPthon['Name']

def copyNewFile(fileCopyFrom,pathCopyTo,name):
	#judge whether the file "copyto" exists.
	if os.path.exists(pathCopyTo):
		# Judge whether json file exists.
		fileInCopyTo = os.listdir(pathCopyTo)
		counter = 0
		for oneFile in fileInCopyTo:
			if oneFile[0:-7] == name:
				counter = counter + 1
		if counter == 0:
			jpathCopyTo = pathCopyTo + "/" + name + "_1.json"
			shutil.copy(fileCopyFrom,jpathCopyTo)
			upathCopyTo = pathCopyTo + "/" + name + "_1.unity3d"
			shutil.copy(fileCopyFrom,upathCopyTo)
		elif counter != 0:
			counter = counter + 1
			jpathCopyTo = pathCopyTo + "/" + name + "_" + str(counter) + ".json"
			shutil.copy(fileCopyFrom,jpathCopyTo)
			upathCopyTo = pathCopyTo + "/" + name + "_" + str(counter) + ".unity3d"
			shutil.copy(fileCopyFrom,upathCopyTo)
	else:
		os.makedirs(pathCopyTo)
		#Copy the json file and unity3d file
		jpathCopyTo = pathCopyTo + "/" + name + "_1.json"
		shutil.copy(fileCopyFrom,jpathCopyTo)
		upathCopyTo = pathCopyTo + "/" + name + "_1.unity3d"
		shutil.copy(fileCopyFrom,upathCopyTo)

	
allFileWithAbPath = getallFileWithAbPath(pathCopyFrom)
for oneFileWithAbPath in allFileWithAbPath:
	if "json" in oneFileWithAbPath[-4:]:
		jsonFileRelativePath = getRelativePath(oneFileWithAbPath)
		jsonPathCopyFrom = oneFileWithAbPath
		jsonPathCopyTo = pathCopyTo + "/" + jsonFileRelativePath

		#Get the unity3d file infor
		unity3dFileName = getUnity3dFileName(oneFileWithAbPath)
		unity3dFileCopyFrom = jsonPathCopyFrom[0:-4] + "unity3d"
		unity3dFileCopyTo = jsonPathCopyTo
		
		#Get the file name without Suffix.
		nameWithoutSuffix = unity3dFileName[0:-8]

		copyNewFile(jsonPathCopyFrom,jsonPathCopyTo,nameWithoutSuffix)


