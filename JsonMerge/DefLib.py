#!/usr/bin/python
import json
import codecs
import sys
import os
import shutil

def getallFileWithAbPath(path):
	allFileWithAbPath = []
	for i in os.walk(path):
		for j in i[2]:
			FileAbsolutePath = os.path.join(i[0],j)
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

def JsonCounter(pathCopyTo,name):
	# Judge whether json file exists.
	fileInCopyTo = os.listdir(pathCopyTo)
	counter = 0
	for oneFile in fileInCopyTo:
		if oneFile[0:-7] == name:
			counter = counter + 1
	return counter

def copyNewFile(fileCopyFrom,pathCopyTo,name):
	#judge whether the file "copyto" exists.
	if os.path.exists(pathCopyTo):
		# Judge whether json file exists.
		counter = JsonCounter(pathCopyTo,name)
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

def addVersion(jsonDoc,counter):
	versionDict = {'Version':counter}
	jsonData = codecs.open(jsonDoc,'w','utf_8_sig')
	jsonData.write(json.loads(versionDict))
	jsonData.close()