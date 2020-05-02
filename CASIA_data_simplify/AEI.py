import os 
import numpy
from natsort import natsort
import cv2
root_dir="/home/tonner/Downloads/GaitDatasetB-silh/001/cl-01/054"
image_files =os.listdir(root_dir)
image_files =natsort.natsorted(image_files)
diff_img1=[]

N=len(image_files)
print(image_files)
for i in range(N):
	img=cv2.imread(os.path.join(root_dir,image_files[i]))
	if i==0:
		diff_img=img
		diff_img1 =diff_img
	else:

		diff_img =cv2.imread(os.path.join(root_dir,image_files[i-1]))
		diff_img1 =abs(img-diff_img)
		diff_img1 +=diff_img1




cv2.imshow("diffrence", diff_img1)
cv2.waitKey(1)
cv2.imwrite("diffrence1.png",diff_img1)

AEI = diff_img1/N
cv2.imwrite("diffrence2.png",AEI)
# cv2.imshow("diffrence",AEI)
# cv2.waitKey(1)
