import pandas as pd
import os
import torch
from torchvision import datasets, transforms

# 定义数据转换器
transform = transforms.Compose([
    transforms.Resize((84, 84)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# 加载数据集
data_path = "/opt/data/private/FSL_data/"
dataset_name = [
    'EuroSAT',  # 0
    'CropDiseases', # 1
    'dtd',  # 2
    'Resisc45', # 3
    'Sketch',   # 4
    'Omniglot', # 5
    'SVNH', # 6
]
index = 4
dataset = datasets.ImageFolder(root=os.path.join(data_path, dataset_name[index]), transform=transform)

# 获取类别数和每个类别的样本数量
num_classes = len(dataset.classes)
class_split = [
    [3, 2, 5],      # 1-[5, 2, 3]
    [20, 8, 10],
    [20, 10, 17],
    [20, 10, 15],
    [400, 200, 400], 
    [600, 364, 659], 
    [0, 0, 10],

]
train_classes = class_split[index][0]
val_classes = class_split[index][1]
test_classes = class_split[index][2]

# 定义随机种子，确保每次划分结果相同
torch.manual_seed(42)

# 获取每个数据集的文件名和标签
train_imgs = []
train_labels = []
val_imgs = []
val_labels = []
test_imgs = []
test_labels = []
for dir, label in dataset.imgs:
    img_name = dir.split('/')[-1]
    label_name = dataset.classes[label]
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


