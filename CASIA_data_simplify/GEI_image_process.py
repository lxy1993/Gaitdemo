import os
import shutil
from shutil import copyfile
import numpy as np
import scipy.io as sio
from natsort import natsort

# def replace_img_name(name, value):
#     name = name.split("-")
#     name[-1] = value
#     return "-".join(name)
#
# ####GEI_image rename
# dir="/home/tonner/Downloads/GEI"
# dir_out="/home/tonner/Downloads/GEI_out"
#
#
# camera_angle = {"000": "c1", "018": "c2", "036": "c3", "054": "c4", "072": "c5", "090": "c6", "108": "c7",
#                 "126": "c8", "144": "c9", "162": "c10", "180": "c11"}
# img_list=os.listdir(dir)
# for i in range(len(img_list)):
#     img_name=img_list[i]
#     src=os.path.join(dir,img_name)
#     view=img_name.split(".")[0].split("-")[-1]
#     for key, value in camera_angle.items():
#         if view == key:
#             img_name=replace_img_name(img_name,value)
#             img_name_out=img_name+".jpg"
#             dst=os.path.join(dir_out,img_name_out)
#             shutil.copyfile(src, dst)
#             print(img_name)
#             break

#####################GEI_image 交集CASIA_split#############################
dir_GEI="/home/tonner/Downloads/GEI_out/"
dir_casia_train="/media/tonner/documents/CASIA_split/bbox_train/"
dir_casia_test ="/media/tonner/documents/CASIA_split/bbox_test"
img_cache=[]
pids=124

#######bbox_train和bbox_test序列信息#################
for pid in range(pids):
    pid="%03d" %(pid+1)
    if int(pid) <= 84:
        mv_dir_trian =os.path.join(dir_casia_train,pid)
        img_lists_train=os.listdir(mv_dir_trian)
        for img in img_lists_train:
            img_list = img.split(".")[0][:-4]
            img_cache.append(img_list)
        img_cache_u, _ = np.unique(img_cache, return_index=True)

    else:

        mv_dir_test=os.path.join(dir_casia_test,pid)
        img_lists_test = os.listdir(mv_dir_test)
        for img in img_lists_test:
            img_list=img.split(".")[0][:-4]
            img_cache.append(img_list)
        img_cache_u,_=np.unique(img_cache,return_index=True)
print(img_cache_u)
print(len(img_cache_u))


###############GEI image 信息提取##########
GEI_cache=[]
GEI_data=os.listdir(dir_GEI)
for GEI in GEI_data:
    GEI=GEI.split(".")[0]
    GEI_cache.append(GEI)
GEI_cache_u,_=np.unique(GEI_cache,return_index=True)
print(len(GEI_cache_u))


####获取两个list的交集########
CASIA_intersection=[]
CASIA_intersection=list(set(GEI_cache_u).intersection(set(img_cache_u)))
print(len(CASIA_intersection))
######差集确保 GEI和CASIA中到底差多少不一样的
print(list(set(GEI_cache_u).difference(set(CASIA_intersection))))

# ########取两个list的差集,并remov差集中的图片序列。
# CASIA_difference=list(set(img_cache_u).difference(set(GEI_cache_u)))
# print(len(CASIA_difference))
# print(CASIA_difference)
# ######remove CASIA_difference 对应文件下图片序列
# for seq_name in CASIA_difference:
#     pid=seq_name.split("-")[0]
#     if int(pid)<=84:
#       train_dir=os.path.join(dir_casia_train,pid)
#       train_imgs=os.listdir(train_dir)
#       for train_img in train_imgs:
#           train_img_split=train_img.split(".")[0][:-4]
#           if seq_name==train_img_split:
#               img_dir=os.path.join(train_dir,train_img)
#               print(img_dir)
#               os.remove(img_dir)
#     else:
#       test_dir=os.path.join(dir_casia_test,pid)
#       test_imgs=os.listdir(test_dir)
#       for test_img in test_imgs:
#           test_img_split=test_img.split(".")[0][:-4]
#           if seq_name==test_img_split:
#               img_dir=os.path.join(test_dir,test_img)
#               print(img_dir)
#               os.remove(img_dir)
#

#########rename the gei image  ########


# camera_angle = {"000": "c1", "018": "c2", "036": "c3", "054": "c4", "072": "c5", "090": "c6", "108": "c7",
#                 "126": "c8", "144": "c9", "162": "c10", "180": "c11"}
#
# def replace_img_name(name, value):
#     name = name.split("-")
#     name[-1] = value
#     return "-".join(name)
#
# gei_dir="/home/tonner/Downloads/GEI_npy/"
#
# gei_npy =os.listdir(gei_dir)
# gei_npys=natsort.natsorted(gei_npy)
# for gei_npy in gei_npys:
#     gei_drop=gei_npy.split(".")[0].rstrip("_GEI")
#     gei_split =gei_drop.split("-")
#     gei_view =camera_angle[gei_split[3]]
#     gei_re =replace_img_name(gei_drop,gei_view)+".npy"
#     src =os.path.join(gei_dir,gei_npy)
#     print("original name ######:",src)
#     dst =os.path.join(gei_dir,gei_re)
#     print("rename ########",dst)
#     os.rename(src,dst)





