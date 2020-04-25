import os
import shutil
from shutil import copyfile
import numpy as np
import scipy.io as sio


##############cASAI_data_prepare#################
# 001_nm_01_000 c1_0.jpg
# person_ID_state_time段数_camera ID_frame

# person ID:train dataset取奇数，test dataset 取偶数
# camera_ID:c1 代表拍摄角度为0|c2代表角度为36°|c3代表角度为90°|c4代表角度为144°|c5代表角度位180°
def replace_img_name(name, value):
    name = name.split("-")
    name[-1] = value
    return "-".join(name)


if __name__ == "__main__":

    raw_data_dir = "D:\\CASIA"
    train_data_dir = "D:\\CASIA_split\\train"
    val_data_dir = "D:\\CASIA_split\\val"
    test_data_dir = "D:\\CASIA_split\\test"

    ##########新建数据集文件夹#########################
    p_filenames = sorted(os.listdir(raw_data_dir))
    for p_filename in p_filenames:
        if not os.path.exists(os.path.join(train_data_dir, p_filename)):
            if int(p_filename) <= 84:
                os.makedirs(os.path.join(train_data_dir, p_filename))
            elif not os.path.exists(os.path.join(val_data_dir, p_filename)):
                if 84 < int(p_filename) <= 104:
                    os.makedirs(os.path.join(val_data_dir, p_filename))
                elif not os.path.exists(os.path.join(test_data_dir, p_filename)):
                    os.makedirs(os.path.join(test_data_dir, p_filename))
                else:
                    pass

        # ############图片重新命名，进行归类#################
    # camera_angle={"000":"c1","036":"c2","090":"c3","144":"c4","180":"c5"}
    camera_angle = {"000": "c1", "018": "c2", "036": "c3", "054": "c4", "072": "c5", "090": "c6", "108": "c7",
                    "126": "c8", "144": "c9", "162": "c10", "180": "c11"}
    camera_angle1 = {"162": "c10"}
    for p_filename in p_filenames:
        s_filenames_path = os.path.join(raw_data_dir, p_filename)
        s_filenames = sorted(os.listdir(s_filenames_path))  # 获取对应person ID的"nm"或者"bg"文件夹
        for s_filename in s_filenames:
            # if s_filename=="nm":
            video_filenames = sorted(
                os.listdir(os.path.join(s_filenames_path, s_filename)))  # 获取"nm"状态下的视频切的图片，并以视频名字命名的文件夹
            for video_filename in video_filenames:
                if int(video_filename.split("-")[2]) <= 2:
                    # print(video_filename.split("-")[2])
                    M_video_filename = video_filename
                    video_filenames_path = os.path.join(s_filenames_path, s_filename)
                    img_lists = sorted(
                        os.listdir(os.path.join(video_filenames_path, video_filename)))  # 以视频名字+帧的序号命名的图片集合
                    for key, value in camera_angle1.items():
                        if video_filename.split("-")[-1] == key:
                            M_video_filename = replace_img_name(M_video_filename, value)
                            ##字符串复制，str.replace(),不改变str原始值
                            # M_video_filename=M_video_filename.split("-")
                            # M_video_filename[-1]=value
                            # str(M_video_filename)
                            print(M_video_filename)
                            #######重命名并复制图片到另一个文件夹中
                            if int(video_filename.split("-")[0]) <= 84:
                                img_dir = os.path.join(train_data_dir, M_video_filename.split("-")[0])
                                for img_list in img_lists:
                                    src = os.path.join(video_filenames_path, video_filename, img_list)
                                    dst = os.path.join(img_dir, M_video_filename + "-" + "%03d" % int(
                                        img_list.split(".")[0]) + ".jpg")  # 拷贝的目标路径，并进行重命名。
                                    shutil.copyfile(src, dst)  # 拷贝图片
                            elif 84 < int(video_filename.split("-")[0]) <= 104:
                                img_dir = os.path.join(val_data_dir, M_video_filename.split("-")[0])
                                for img_list in img_lists:
                                    src = os.path.join(video_filenames_path, video_filename, img_list)
                                    dst = os.path.join(img_dir, M_video_filename + "-" + img_list.split(".")[0] + ".jpg")  # 拷贝的目标路径，并进行重命名。
                                    shutil.copyfile(src, dst)
                            elif 104 < int(video_filename.split("-")[0]) <= 124:
                                img_dir = os.path.join(test_data_dir, M_video_filename.split("-")[0])
                                for img_list in img_lists:
                                    src = os.path.join(video_filenames_path, video_filename, img_list)
                                    dst = os.path.join(img_dir, M_video_filename + "-" + img_list.split(".")[0] + ".jpg")  # 拷贝的目标路径，并进行重命名。
                                    shutil.copyfile(src, dst)

                elif 6 >= int(video_filename.split("-")[2]) > 2:
                    M_video_filename = video_filename
                    video_filenames_path = os.path.join(s_filenames_path, s_filename)
                    img_lists = sorted(
                        os.listdir(os.path.join(video_filenames_path, video_filename)))  # 以视频名字+帧的序号命名的图片集合
                    for key, value in camera_angle.items():
                        if video_filename.split("-")[-1] == key:
                            M_video_filename = replace_img_name(M_video_filename, value)
                            ##字符串复制，str.replace(),不改变str原始值
                            # M_video_filename=M_video_filename.split("-")
                            # M_video_filename[-1]=value
                            # str(M_video_filename)
                            print(M_video_filename)
                            #######重命名并复制图片到另一个文件夹中
                            if int(video_filename.split("-")[0]) <= 84:
                                img_dir = os.path.join(train_data_dir, M_video_filename.split("-")[0])
                                for img_list in img_lists:
                                    src = os.path.join(video_filenames_path, video_filename, img_list)
                                    dst = os.path.join(img_dir, M_video_filename + "-" + "%03d" % int(
                                        img_list.split(".")[0]) + ".jpg")  # 拷贝的目标路径，并进行重命名。
                                    shutil.copyfile(src, dst)  # 拷贝图片
                            elif 84 < int(video_filename.split("-")[0]) <= 104:
                                img_dir = os.path.join(val_data_dir, M_video_filename.split("-")[0])
                                for img_list in img_lists:
                                    src = os.path.join(video_filenames_path, video_filename, img_list)
                                    dst = os.path.join(img_dir, M_video_filename + "-" + img_list.split(".")[0] + ".jpg")  # 拷贝的目标路径，并进行重命名。
                                    shutil.copyfile(src, dst)
                            elif 104 < int(video_filename.split("-")[0]) <= 124:
                                img_dir = os.path.join(test_data_dir, M_video_filename.split("-")[0])
                                for img_list in img_lists:
                                    src = os.path.join(video_filenames_path, video_filename, img_list)
                                    dst = os.path.join(img_dir, M_video_filename + "-" + img_list.split(".")[0] + ".jpg")  # 拷贝的目标路径，并进行重命名。
                                    shutil.copyfile(src, dst)
