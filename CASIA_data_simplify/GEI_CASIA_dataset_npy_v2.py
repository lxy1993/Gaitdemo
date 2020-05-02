import os
import numpy as np
import re
import natsort
from lxy_log_cpu import lxy_log_cpu
############按照角度进行数据划分，就是摄像头数据集的划分###################
##########生成tracklet_train_info.npy#######################
#######start| end|  person_ID|  Camera_ID只有体现tracklet中行人身份信息和角度信息，没有状态信息。

data_dir = "/media/tonner/documents/CASIA_split/info_4.23"
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
info_train=[]
info_val=[]
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

    if p_id <=68:
        print("i:", i, "p_id:", p_id, "c_id:", c_id, "seq_type", seq_type, "seq", seq[seq_type], "star:", start, "end:",
              end, "\n")
        # print("train##########","p_id:", p_id)
        train=[start,end,p_id,c_id,seq[seq_type]]
        info_train.append(train)
    else:
        print("val##########", "p_id:", p_id)
        val =[start,end,p_id,c_id,seq[seq_type]]
        info_val.append(val)

np.save(os.path.join(data_dir, 'm_train_info.npy'), np.array(info_train))
np.save(os.path.join(data_dir, 'val_info.npy'),  np.array(info_val))

##################提取tracklet_test_info.npy###########
######提取gallery set（cl,bg）###########
# data_dir="/media/tonner/documents/CASIA_split/info_4.23"
# f = open(os.path.join(data_dir, "test_name.txt"))
# img_files = f.readlines()
#
# cut_img_file = []
# for img in img_files:
#     cut_img_file.append(img.split(".")[0][:-4])
#
# # #提取每一个tracklet的名字以及在cut_img_file中的索引号
# uni_img_file, index = np.unique(cut_img_file, return_index=True) ##找到每一段tracklet的名字、对应的索引号。
# uni_img_file=natsort.natsorted(uni_img_file)
# index = natsort.natsorted(index)
# tracklet_n = len(uni_img_file)
# print(tracklet_n)
#
# info=[]
#
# seq ={"nm-05":9, "nm-06":10}     ####将gallery中数据nm 数据集由1～6减少到5～6
# j=0
# for i in range(tracklet_n):
# # ##########为probe nm 特殊添加一段的代码，保证galleryset 没有nm状态
# #     print(uni_img_file[i][4:9])
# #     print((uni_img_file[i][4:9] not in list(seq.keys())))
#     if uni_img_file[i][4:9] in list(seq.keys()):
#         print(uni_img_file[i])
#         p_id = int(uni_img_file[i].split("-")[0])
#         c_id = uni_img_file[i].split("-")[-1].lstrip("c")  ####drop out str "c"
#         seq_type = uni_img_file[i].split(".")[0][4:9]
#         if i == tracklet_n - 1:
#             start = index[i]
#             end = len(cut_img_file)-1
#         else:
#             start = index[i]
#             end = index[i + 1] - 1
#         print("i:",i,"p_id:", p_id, "c_id:", c_id,"seq",seq[seq_type], "star:", start, "end:", end, "\n")
#         infos=[start,end,p_id,c_id,seq[seq_type]]
#         info.append(infos)
#         j+=1
#
# info=np.array(info).astype(np.float64)
# print(j,"\n",len(info))
# print(info.dtype,type(info))
# np.save(os.path.join(data_dir, 'test_info.npy'), info)

######################query_idx#############################
########query中只保存nm的01的0°和02的90°和03的180度

# data_dir="/media/tonner/documents/CASIA_split/info_4.23"
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
# query_info=[]
# seq ={"bg-01":1,"bg-02":2,"cl-01":3,"cl-02":4,"nm-01":5,"nm-02":6}
#
# for i in range(tracklet_n):
# ##########为probe nm 特殊添加一段的代码，保证galleryset 没有nm状态，xxx-nm-01-c1,xxx-nm-02-c6,xxx-nm-02-c11
#
#     if uni_img_file[i].split("-")[1]=="nm" and int(uni_img_file[i].split("-")[2]) ==1:
#
#         p_id = int(uni_img_file[i].split("-")[0])
#         c_id = uni_img_file[i].split("-")[-1].lstrip("c")
#         seq_type = uni_img_file[i].split(".")[0][4:9]
#
#         if c_id=="1" :
#             if i == tracklet_n - 1:
#                 start = index[i]
#                 end = len(cut_img_file)-1
#             else:
#                 start = index[i]
#                 end=index[i+1]-1
#             print("i:", i, "p_id:", p_id, "c_id:", c_id,"seq:",seq_type ,"star:", start, "end:", end, "\n")
#             query_infos=[start,end,p_id,c_id,seq[seq_type]]
#             query_info.append(query_infos)
#
#     if uni_img_file[i].split("-")[1]=="nm" and int(uni_img_file[i].split("-")[2]) ==2:
#         p_id = int(uni_img_file[i].split("-")[0])
#         c_id = uni_img_file[i].split("-")[-1].lstrip("c")
#         seq_type = uni_img_file[i].split(".")[0][4:9]
#
#         if c_id=="6" or c_id=="11":
#             if i == tracklet_n - 1:
#                 start = index[i]
#                 end = len(cut_img_file)-1
#             else:
#                 start = index[i]
#                 end=index[i+1]-1
#             print("i:", i, "p_id:", p_id, "c_id:", c_id,"seq:",seq_type ,"star:", start, "end:", end, "\n")
#             query_infos=[start,end,p_id,c_id,seq[seq_type]]
#             query_info.append(query_infos)
#
# query_info=np.array(query_info).astype(np.float64)
# print(len(query_info))
# print(query_info.dtype,type(query_info))
# np.save(os.path.join(data_dir, 'query_IDX_nm.npy'),query_info)




#########生成train_name.txt和test_name.tx
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


