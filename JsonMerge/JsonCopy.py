#!/usr/bin/python
import DefLib
import os

from DefLib import getallFileWithAbPath
from DefLib import getRelativePath
from DefLib import getUnity3dFileName
from DefLib import copyNewFile

'''
#path = sys.path[0]  #relative path   os.path.join(dirpath,name)
pathCopyFrom =  "/Users/Jason/ShenJing/Python/JsonMerge/CDN"
pathCopyTo = "/Users/Jason/ShenJing/Python/JsonMerge/copyTo"
'''
pathCopyFrom =  "E:\Shenjing\Python\Python\JsonMerge\CDN"
pathCopyTo = "E:\Shenjing\Python\Python\JsonMerge\copyTo"

	
allFileWithAbPath = getallFileWithAbPath(pathCopyFrom)
for oneFileWithAbPath in allFileWithAbPath:
	if "json" in oneFileWithAbPath[-4:]:
		jsonFileRelativePath = getRelativePath(oneFileWithAbPath)
		jsonPathCopyFrom = oneFileWithAbPath
		jsonPathCopyTo = os.path.join(pathCopyTo,jsonFileRelativePath)

		#Get the unity3d file infor
		unity3dFileName = getUnity3dFileName(oneFileWithAbPath)
		unity3dFileCopyFrom = jsonPathCopyFrom[0:-4] + "unity3d"
		unity3dFileCopyTo = jsonPathCopyTo
		
		#Get the file name without Suffix.
		nameWithoutSuffix = unity3dFileName[0:-8]

		copyNewFile(jsonPathCopyFrom,jsonPathCopyTo,nameWithoutSuffix)


