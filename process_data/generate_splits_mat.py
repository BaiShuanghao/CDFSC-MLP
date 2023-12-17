import scipy.io
import os
import pandas as pd

data_path = # your data path

index = 1
dataset = [
    'Flower102',
    'SVHN',
]
mat_file = [
    'imagelabels.mat',
    'test_32x32.mat',
]
# 加载 mat 文件
mat = scipy.io.loadmat(os.path.join(data_path, dataset[index], mat_file[index]))

# 获取 mat 文件中的数据
data = mat

# 获取类别数和每个类别的样本数量
lables = data['labels'].tolist()[0]     # [77, 77, 42, ...]
num_classes = max(lables)
class_split = [
    [50, 20, 32],

]
train_classes = class_split[index][0]
val_classes = class_split[index][1]
test_classes = class_split[index][2]

imgs_dir = os.path.join(data_path, dataset[index], 'jpg')
imgs_name = os.listdir(imgs_dir)
imgs_name.sort()

# 获取每个数据集的文件名和标签
train_imgs = []
train_labels = []
val_imgs = []
val_labels = []
test_imgs = []
test_labels = []
for img_name, label in zip(imgs_name, lables):

    if label-1 in range(train_classes):
        train_imgs.append(img_name)
        train_labels.append(label)
    elif label-1 in range(train_classes, train_classes+val_classes):
        val_imgs.append(img_name)
        val_labels.append(label)
    else:
        test_imgs.append(img_name)
        test_labels.append(label)

# 将文件名和标签组合成DataFrame，并保存为csv文件
train_df = pd.DataFrame({'filename': train_imgs, 'label': train_labels})
val_df = pd.DataFrame({'filename': val_imgs, 'label': val_labels})
test_df = pd.DataFrame({'filename': test_imgs, 'label': test_labels})

train_csv = os.path.join(data_path, dataset[index], 'train.csv')
val_csv = os.path.join(data_path, dataset[index], 'val.csv')
test_csv = os.path.join(data_path, dataset[index], 'test.csv')
train_df.to_csv(train_csv, index=False)
val_df.to_csv(val_csv, index=False)
test_df.to_csv(test_csv, index=False)
