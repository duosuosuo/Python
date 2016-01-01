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
	#Judge whether json file exists.
	fileInCopyTo = os.listdir(pathCopyTo)
	counter = 0
	name_ = name + "_"
	length = len(name_)
	for oneFile in fileInCopyTo:
		if oneFile[0:length] == name_:
			counter = counter + 1
	counter = counter / 2
	return counter

def copyNewFile(fileCopyFrom,pathCopyTo,name):
	#judge whether the file "copyto" exists.
	if os.path.exists(pathCopyTo):
		# Judge whether json file exists.
		counter = JsonCounter(pathCopyTo,name)
		if counter == 0:
			jsonName = name + "_1.json"
			jpathCopyTo = os.path.join(pathCopyTo,jsonName)
			shutil.copy(fileCopyFrom,jpathCopyTo)			
			
			unity3dName = name + "_1.unity3d"
			upathCopyTo = os.path.join(pathCopyTo,unity3dName)			
			shutil.copy(fileCopyFrom,upathCopyTo)
		elif counter != 0:
			counter = counter + 1
			jsonName = name + "_" + str(counter) + ".json"
			jpathCopyTo = os.path.join(pathCopyTo,jsonName)			
			shutil.copy(fileCopyFrom,jpathCopyTo)

			unity3dName = name + "_" + str(counter) + ".unity3d"
			upathCopyTo = os.path.join(pathCopyTo,unity3dName)						
			shutil.copy(fileCopyFrom,upathCopyTo)
	else:
		os.makedirs(pathCopyTo)
		#Copy the json file and unity3d file
		jsonName = name + "_1.json"
		jpathCopyTo = os.path.join(pathCopyTo,jsonName)
		shutil.copy(fileCopyFrom,jpathCopyTo)

		unity3dName = name + "_1.unity3d"
		upathCopyTo = os.path.join(pathCopyTo,unity3dName)
		shutil.copy(fileCopyFrom,upathCopyTo)

def getAllJsonFile(path):
	allJsonFile = []
	for i in os.walk(path):
		for j in i[2]:
			if j[-4:] == "json":
				JsonFile = os.path.join(i[0],j)
				allJsonFile.append(JsonFile)
	return allJsonFile

def addVersion(jsonDoc,counter):
	jsonData = codecs.open(jsonDoc,'r','utf_8_sig')
	jsonString = jsonData.read()
	jsonStringPython = json.loads(jsonString)
	jsonStringPython['Version'] = counter
	json.dump(jsonStringPython,open(jsonDoc,'w'))
	jsonData.close()
	return jsonDoc

def bigJson(jsonDoc):
	pass
	
