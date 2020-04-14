import os 
import numpy

root_dir=""
image_files =os.listdir(root_dir)
images_files =natsorted(image_files)
N=len(images_files)

for i in range(N):
	img=cv2.imread(os.path.join(root_dir,image_files[i]))
	if i==0:
		Diff_img=img
	else:
		diff_img =img-diff_img
	sum_diff_img +=diff_img

AEI = sum_diff_img/N

