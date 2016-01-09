#!/usr/bin/python
from JsonCopy import Copy
from JsonMerge import Merge

#Please give the pathCopyFrom and pathCopyTo
pathCopyFrom =  "/Users/Jason/ShenJing/Python/JsonMerge/CDN"
pathCopyTo = "/Users/Jason/ShenJing/Python/JsonMerge/copyTo"

############
#Copy
############
Copy(pathCopyFrom,pathCopyTo)



#############
#Merge
#############
Merge(pathCopyTo)