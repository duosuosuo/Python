#!/usr/bin/python


import os

#Print the class name in result.txt
path = "/Users/Jason/ShenJing/ClassFinder/ABC/"
key = "class"

def getContent(existFile):
	f = open (existFile,'r')
	string = f.read()
	return string

def findValuesByKey(content, key):
	l = []
	location = 0
	location = content.find(key, 0, len(content))
	while location != -1:
		val = getFollowValueByKey(content,location,key)
		l.append(val)
		location = content.find(key, location + len(key), len(content))
	return l

def getFollowValueByKey(content, location, key):
	nameBegin = location + len(key) + 1
	letter = content[nameBegin]
	i = 1
	while  letter != ' ':
		i = i + 1
		letter = content[location + len(key) + i]
	nameEnd = location + len(key) + i
	name = content[nameBegin:nameEnd]
	return name

resultList = []
for file in os.listdir(path):	
	existFile = os.path.join(path,file)
	content = getContent(existFile)
	partValue = findValuesByKey(content, key)
	resultList = resultList + partValue

for v in resultList:
	print v

