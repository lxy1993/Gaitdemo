import os
import numpy as np
import re
import argparse

<<<<<<< HEAD
result_name="./4.2_v4/result_cl_v3.0.txt"
=======
parser = argparse.ArgumentParser(description="result data process")
parser.add_argument("-sf","-result_filename",type=str)
parser.add_argument("-pf","-process_filename",type=str)
>>>>>>> e1fdcc8f4afa6134cf4fc1d093e8f605864c6f57

args = parser.parse_args()


file =open(args.sf,"r")
lines =file.readlines()
flie_p =open(args.pf,"a")


mAP=[]
rank1 = []
rank5 = []
rank10 = []
rank20 = []
for line in lines:
	if bool(line.find(":",0,len(line))):
		a=line.split(":")[0]
		if line.split(":")[0]=="mAP":
			score=re.findall(r"\d+\.?\d",line)
			mAP.append(score[0])

		elif line.split(":")[0]=="Rank-1  ":
			score=re.findall(r"\d+\.?\d",line)
			rank1.append(score[0])

		elif line.split(":")[0]=="Rank-5  ":
			score=re.findall(r"\d+\.?\d",line)
			rank5.append(score[0])
		elif line.split(":")[0]=="Rank-10 ":
			score=re.findall(r"\d+\.?\d",line)
			rank10.append(score[1])
		elif line.split(":")[0]=="Rank-20 ":
			score=re.findall(r"\d+\.?\d",line)
			rank20.append(score[1])
mAP=np.array(mAP).astype("float64").mean()
rank1=np.array(rank1).astype("float64").mean()
rank5=np.array(rank5).astype("float64").mean()
rank10=np.array(rank10).astype("float64").mean()
rank20 =np.array(rank20).astype("float64").mean()

reslut=args.sf+"\n"+"mAP:"+str(mAP)+"\n"+"rank1:"+str(rank1)+"\n"+"rank5:"+str(rank5)+"\n"\
	+"rank10:"+str(rank10)+"\n"+"rank20:"+str(rank20)+"\n"
flie_p.write(reslut)

print ("mAP##############",mAP,"\n","rank1##############",rank1,"\n","rank5##############",rank5,"\n"
	   "rank10##############",rank10,"\n","rank20##############",rank20)


