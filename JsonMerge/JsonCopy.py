#!/usr/bin/python
import DefLib
import os

from DefLib import getallFileWithAbPath
from DefLib import getRelativePath
from DefLib import getUnity3dFileName
from DefLib import copyNewFile

def Copy(pathCopyFrom,pathCopyTo):	
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
