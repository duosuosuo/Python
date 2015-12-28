#!/usr/bin/python

import json
#import codecs
#import sys
import os
#import shutil

pathCopyTo = "/Users/Jason/ShenJing/Python/JsonMerge/copyTo"

def getallFileWithAbPath(path):
	allFileWithAbPath = []
	for i in os.walk(path):
		for j in i[2]:
			FileAbsolutePath = i[0] + "/" + j
			allFileWithAbPath.append(FileAbsolutePath)
	return allFileWithAbPath

allFileWithAbPath = getallFileWithAbPath(pathCopyTo)
print allFileWithAbPath