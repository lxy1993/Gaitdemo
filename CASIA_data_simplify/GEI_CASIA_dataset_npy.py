import os
import numpy as np
import re
import natsort
from lxy_log_cpu import lxy_log_cpu
############按照角度进行数据划分，就是摄像头数据集的划分###################

##########生成tracklet_train_info.npy#######################
#######start| end|  person_ID|  Camera_ID只有体现tracklet中行人身份信息和角度信息，没有状态信息。

data_dir = "/media/tonner/documents/CASIA_split/info"
f = open(os.path.join(data_dir, "train_name.txt"))
img_files = f.readlines()
print(len(img_files))
# ###图像文件名去除-xxx.jpg后缀
cut_img_file = []
for img in img_files:
    cut_img_file.append(img.split(".")[0][:-4])


#提取每一个tracklet的名字以及在cut_img_file中的索引号
uni_img_file, index = np.unique(cut_img_file, return_index=True) ##找到每一段tracklet的名字、对应的索引号。
uni_img_file=natsort.natsorted(uni_img_file)
index = natsort.natsorted(index)

tracklet_n = len(uni_img_file)
print(tracklet_n)

info = np.zeros((tracklet_n, 5))
seq={"bg-01":1,"bg-02":2,"cl-01":3,"cl-02":4,"nm-01":5,"nm-02":6,"nm-03":7,"nm-04":8,"nm-05":9,"nm-06":10}


for i in range(tracklet_n):
    p_id = int(uni_img_file[i].split("-")[0])
    c_id = uni_img_file[i].split("-")[-1].lstrip("c")
    seq_type = uni_img_file[i].split(".")[0][4:9]
    if i == tracklet_n - 1:
        start = index[i]
        end = len(cut_img_file)-1
    else:
        start = index[i]
        end = index[i + 1] - 1
    print("i:",i,"p_id:", p_id, "c_id:", c_id, "seq_type",seq_type,"seq",seq[seq_type],"star:", start, "end:", end, "\n")
    info[i, 0] = start
    info[i, 1] = end
    info[i, 2] =p_id
    info[i, 3] = c_id
    info[i,4] =seq[seq_type]
np.save(os.path.join(data_dir, 'train_info.npy'), info)



#######

###################提取tracklet_test_info.npy###########
#######提取gallery set（cl,bg）###########
# data_dir="/media/tonner/documents/CASIA_split/info"
# f = open(os.path.join(data_dir, "test_name.txt"))
# img_files = f.readlines()
#
# cut_img_file = []
# for img in img_files:
#     cut_img_file.append(img.split(".")[0][:-4])
# #
# # #提取每一个tracklet的名字以及在cut_img_file中的索引号
# uni_img_file, index = np.unique(cut_img_file, return_index=True) ##找到每一段tracklet的名字、对应的索引号。
# uni_img_file=natsort.natsorted(uni_img_file)
# index = natsort.natsorted(index)
# tracklet_n = len(uni_img_file)
# print(tracklet_n)
# # info = np.zeros((tracklet_n, 4))
# info=[]
# seq={"bg-01":1,"bg-02":2,"cl-01":3,"cl-02":4,"nm-01":5,"nm-02":6,"nm-03":7,"nm-04":8,"nm-05":9,"nm-06":10}
# j=0
# for i in range(tracklet_n):
# # ##########为probe nm 特殊添加一段的代码，保证galleryset 没有nm状态
#     if uni_img_file[i].split("-")[1]=="cl":
#         print(uni_img_file[i])
#         continue
# # ########################################
#
#     p_id = int(uni_img_file[i].split("-")[0])
#     c_id = uni_img_file[i].split("-")[-1].lstrip("c")  ####drop out str "c"
#     seq_type = uni_img_file[i].split(".")[0][4:9]
#     if i == tracklet_n - 1:
#         start = index[i]
#         end = len(cut_img_file)-1
#     else:
#         start = index[i]
#         end = index[i + 1] - 1
#     print("i:",i,"p_id:", p_id, "c_id:", c_id,"seq",seq_type, "star:", start, "end:", end, "\n")
#     # info[i, 0] = start
#     # info[i, 1] = end
#     # info[i, 2] =p_id
#     # info[i, 3] = c_id
#     infos=[start,end,p_id,c_id,seq[seq_type]]
#     info.append(infos)
#     j+=1
#
# info=np.array(info).astype(np.float64)
# print(j,"\n",len(info))
# print(info.dtype,type(info))
# np.save(os.path.join(data_dir, 'test_cl_info.npy'), info)

#######################query_idx#############################
#####提取test中每一个ID的第一个track对应的行号存储在query_idx.npy
# print(info[:,2],"number",len(info[:,2]))
#
# uni_q_img,q_index=np.unique(info[:,2], return_index=True)
# np.save(os.path.join(data_dir, 'query_IDX.npy'), q_index)

########query中只保存nm的01的0°和02的90°和03的180度

# data_dir="/media/tonner/documents/CASIA_split/info"
# f = open(os.path.join(data_dir, "test_name.txt"))
# img_files = f.readlines()
#
# cut_img_file = []
# for img in img_files:
#     cut_img_file.append(img.split(".")[0][:-4])
#
# #提取每一个tracklet的名字以及在cut_img_file中的索引号
# uni_img_file, index = np.unique(cut_img_file, return_index=True) ##找到每一段tracklet的名字、对应的索引号。
# uni_img_file=natsort.natsorted(uni_img_file)     ###返回的乱序文件进行重新排序
# index = natsort.natsorted(index)
# tracklet_n = len(uni_img_file)
# print(tracklet_n)
# # info = np.zeros((tracklet_n, 4))
# query_info=[]
# seq={"bg-01":1,"bg-02":2,"cl-01":3,"cl-02":4,"nm-01":5,"nm-02":6,"nm-03":7,"nm-04":8,"nm-05":9,"nm-06":10}
#
# for i in range(tracklet_n):
# ##########为probe nm 特殊添加一段的代码，保证galleryset 没有nm状态，xxx-nm-01-c1,xxx-nm-02-c6,xxx-nm-01-c11
#     if uni_img_file[i].split("-")[1]=="bg":
#             if int(uni_img_file[i].split("-")[2]) ==1 or int(uni_img_file[i].split("-")[2]) ==2:
#                 p_id = int(uni_img_file[i].split("-")[0])
#                 c_id = uni_img_file[i].split("-")[-1].lstrip("c")
#                 seq_type = uni_img_file[i].split(".")[0][4:9]
#                 if i == tracklet_n - 1:
#                     start = index[i]
#                     end = len(cut_img_file)-1
#                 else:
#                     start = index[i]
#                     end=index[i+1]-1
#                 print("i:", i, "p_id:", p_id, "c_id:", c_id,"seq:",seq_type ,"star:", start, "end:", end, "\n")
#                 query_infos=[start,end,p_id,c_id,seq[seq_type]]
#                 query_info.append(query_infos)
#
#
# query_info=np.array(query_info).astype(np.float64)
# print(len(query_info))
# print(query_info.dtype,type(query_info))
# np.save(os.path.join(data_dir, 'query_IDX_bg.npy'),query_info)
# lxy_log_cpu()



#########生成train_name.txt和test_name.txt 和 energy image的npy文件的txt
# data_dir = "/media/tonner/documents/CASIA_split"
# if not os.path.exists(os.path.join(data_dir, "info/train_name.txt")):
#     img_dir = "/media/tonner/documents/CASIA_split/bbox_train"
#
#     fid = open(os.path.join(data_dir, "info/train_name.txt"), "w")
#     for file in natsort.natsorted(os.listdir(img_dir)):
#         for img in natsort.natsorted(os.listdir(os.path.join(img_dir, file))):
#             # split_img = img.split("-")
#             # frame_index = split_img[-1].split(".")[0]
#             # frame_index = int(frame_index)
#             # frame_index = "%03d" % frame_index
#             # split_img[-1] = frame_index+".jpg"
#             # img1 = "-".join(split_img)
#             # print(img1)
#             # os.rename(os.path.join(img_dir,file,img),os.path.join(img_dir,file,img1))
#             print(img)
#             fid.write(img+"\n")

# data_dir = "/home/tonner/Downloads/MEAEI/MEAEI_npy"
# fid = open("MEAEI_name.txt", "w")
# for file in natsort.natsorted(os.listdir(data_dir)):
#     for img in natsort.natsorted(os.listdir(data_dir)):
#         # split_img = img.split("-")
#         # frame_index = split_img[-1].split(".")[0]
#         # frame_index = int(frame_index)
#         # frame_index = "%03d" % frame_index
#         # split_img[-1] = frame_index+".jpg"
#         # img1 = "-".join(split_img)
#         # print(img1)
#         # os.rename(os.path.join(img_dir,file,img),os.path.join(img_dir,file,img1))
#         print(img)
#         fid.write(img+"\n")


