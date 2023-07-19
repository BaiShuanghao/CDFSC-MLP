import os
import tqdm

root_path = "/opt/data/private/FSL_data/"
dataset = [
    'EuroSAT',  # 0
    'Flower102',    # 1
    'CropDiseases', # 2
    'dtd',  # 3
    'DeepWeeds',    # 4
    'ISIC', # 5
    'kaokore',  # 6
    'Resisc45', # 7
    'ChestX',   # 8
    'Omniglot', # 9
    'SVNH', # 10
    'Sketch', # 11
]
index = 8

data_path = os.path.join(root_path, dataset[index])
class_file = os.listdir(data_path)

folder_name = os.path.join(data_path, 'images')
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

for i, class_file_i in enumerate(class_file):
    if class_file_i == 'images':
        continue
    
    dir = os.path.join(data_path, class_file_i)

    if not os.path.isdir(dir):
        continue
    if not os.listdir(dir):
        continue
    
    print('{}: {} is copying...'.format(i, class_file_i))
    if index == 8:
        inner_dir = os.path.join(dir, 'images')
        os.system('mv {}/{}/{}/* {}/{}/'.format('.', class_file_i, 'images',
                                                '.', 'images'))
        os.rmdir(inner_dir)
    else:
        os.system('cp {}/{}/* {}/{}/'.format('.', class_file_i, '.', 'images'))
        
    if index == 8:
        os.rmdir(dir)


