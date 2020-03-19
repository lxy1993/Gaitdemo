import os
import numpy as np

file =open("/Users/luxiaoyan/Gaitdemo/result/result_bg.txt")
lines =file.readlines()

mAP=[]
rank1 = []
rank5 = []
rank10 = []
rank20 = []


for line in lines:
	if bool(line.find(":",0,len(line))):
		if line.split(":")=="mAP":
			score=re.findall(r"\d+\.?\d",line)
			print “11”
			print score
			mAP.append(score)

print mAP



