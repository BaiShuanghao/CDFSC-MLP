import csv
import os
import pandas as pd
import numpy as np

data_path = # your data path
classes = ['train', 'val', 'test']
dataset_name = [
    'DeepWeeds',
    'ISIC',
    'kaokore',
    'ChestX-ray',
]
index = 1
csv_name = [
    'labels/labels.csv',
    'ISIC2018_Task3_Training_GroundTruth/ISIC2018_Task3_Training_GroundTruth.csv',
    'labels.csv',
    'Data_Entry_2017.csv',
]
all_csv = os.path.join(data_path, dataset_name[index], csv_name[index])
class_split = [
    [3, 1, 5],     
    [1, 1, 5],      
    [2, 1, 5],     
    [4, 2, 9],      

]
train_classes = class_split[index][0]
val_classes = class_split[index][1]
test_classes = class_split[index][2]

# 获取每个数据集的文件名和标签
train_imgs, train_labels = [], []
val_imgs, val_labels = [], []
test_imgs, test_labels = [], []
label_list = []
with open(all_csv, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    list_reader = list(reader)
    for j, row in enumerate(list_reader):
        if j == 0:
            if index == 1:
                label_name_list = row[1:]
            continue 
        if index == 0:
            label = row[1]
            label_name = row[2]
            img_name = row[0]
        if index == 1:
            label = np.array([int(float(i)) for i in row[1:]]).argmax()
            label_name = label_name_list[label]
            img_name = row[0]+'.jpg'
        elif index == 2:
            label = int(row[1]) * 4 + int(row[2])
            label_name = label
            imgs_name = row[0]
        elif index == 3:
            label_name = row[1]
            if '|' in label_name:
                continue
            if label_name not in label_list:
                label_list.append(label_name)
            label = label_list.index(label_name)
            img_name = row[0]

        if label in range(train_classes):
            train_imgs.append(img_name)
            train_labels.append(label_name)
        elif label in range(train_classes, train_classes+val_classes):
            val_imgs.append(img_name)
            val_labels.append(label_name)
        else:
            test_imgs.append(img_name)
            test_labels.append(label_name)
        

# 将文件名和标签组合成DataFrame，并保存为csv文件
train_df = pd.DataFrame({'filename': train_imgs, 'label': train_labels})
val_df = pd.DataFrame({'filename': val_imgs, 'label': val_labels})
test_df = pd.DataFrame({'filename': test_imgs, 'label': test_labels})

train_csv = os.path.join(data_path, dataset_name[index], 'train.csv')
val_csv = os.path.join(data_path, dataset_name[index], 'val.csv')
test_csv = os.path.join(data_path, dataset_name[index], 'test.csv')
train_df.to_csv(train_csv, index=False)
val_df.to_csv(val_csv, index=False)
test_df.to_csv(test_csv, index=False)


