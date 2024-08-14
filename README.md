# Improving Cross-domain Few-shot Classification with Multilayer Perceptron [ICASSP 2024]

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/improving-cross-domain-few-shot/cross-domain-few-shot-on-chestx)](https://paperswithcode.com/sota/cross-domain-few-shot-on-chestx?p=improving-cross-domain-few-shot)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/improving-cross-domain-few-shot/cross-domain-few-shot-on-cropdisease)](https://paperswithcode.com/sota/cross-domain-few-shot-on-cropdisease?p=improving-cross-domain-few-shot)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/improving-cross-domain-few-shot/cross-domain-few-shot-on-isic2018)](https://paperswithcode.com/sota/cross-domain-few-shot-on-isic2018?p=improving-cross-domain-few-shot)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/improving-cross-domain-few-shot/cross-domain-few-shot-on-eurosat)](https://paperswithcode.com/sota/cross-domain-few-shot-on-eurosat?p=improving-cross-domain-few-shot)

[![arXiv](https://img.shields.io/badge/arXiv-2312.09589-b31b1b.svg)](https://arxiv.org/abs/2312.09589)
![GitHub stars](https://img.shields.io/github/stars/BaiShuanghao/CDFSC-MLP)
![GitHub forks](https://img.shields.io/github/forks/BaiShuanghao/CDFSC-MLP)

Official implementation of the paper "[Improving Cross-domain Few-shot Classification with Multilayer Perceptron](https://arxiv.org/abs/2312.09589)".

Authors: [Shuanghao Bai](https://scholar.google.com/citations?user=xhd94DIAAAAJ&hl=zh-CN), [Wanqi Zhou](https://scholar.google.com/citations?user=3Q_3PR8AAAAJ&hl=zh-CN), [Zhirong Luan](https://scholar.google.com/citations?user=mJNCeucAAAAJ&hl=zh-CN), [Donglin Wang](https://scholar.google.com/citations?user=-fo6wdwAAAAJ&hl=zh-CN), [Badong Chen](https://scholar.google.com/citations?user=mq6tPX4AAAAJ&hl=zh-CN&oi=ao).

<hr />

## Installation 
For installation and other package requirements, please follow the instructions as follows. 
This codebase is tested on Ubuntu 18.04 LTS with python 3.7. Follow the below steps to create environment and install dependencies.

* Setup conda environment.
```bash
# Create a conda environment
conda create -y -n cdfsc_mlp python=3.7

# Activate the environment
conda activate cdfsc_mlp

# Install torch (requires version >= 1.5.0) and torchvision
# Please refer to https://pytorch.org/get-started/previous-versions/ if your cuda version is different
conda install pytorch==1.12.0 torchvision==0.13.0 torchaudio==0.12.0 cudatoolkit=11.3 -c pytorch
```

* Clone CDFSC-MLP code repository and install requirements
```bash
# Clone PEM code base
git clone https://github.com/BaiShuanghao/CDFSC-MLP.git
cd CDFSC-MLP

# Install requirements
pip install -r requirements.txt
```

## Data Preparation
Please follow the instructions to prepare all datasets.
Datasets list:
- [miniImageNet](https://drive.google.com/drive/u/0/folders/1SEoARH5rADckI-_gZSQRkLclrunL-yb0)
- [ChestX-ray](https://nihcc.app.box.com/v/ChestXray-NIHCC)
- [CropDieases](https://data.mendeley.com/datasets/tywbtsjrjv/1)
- [DeepWeeds](https://github.com/AlexOlsen/DeepWeeds)
- [DTD](https://www.robots.ox.ac.uk/~vgg/data/dtd/)
- [EuroSAT](https://github.com/phelber/eurosat)
- [Flower102](https://www.robots.ox.ac.uk/~vgg/data/flowers/102/)
- [ISIC](https://challenge.isic-archive.com/landing/2018/)
- [Kaokore](https://github.com/rois-codh/kaokore)
- [Omniglot](https://github.com/brendenlake/omniglot)
- [Resisc45](https://github.com/canturan10/satellighte)
- [Sketch](https://github.com/HaohanWang/ImageNet-Sketch)
- [SVHN](http://ufldl.stanford.edu/housenumbers/)

You need to put all images in **only one** folder namely **images**, and split each dataset into **train.csv**, **val.csv**, and **test.csv**, thus organizing them as follows. 

```shell
ChestX/
  ├── images
  ├── train.csv
  ├── val.csv
  └── test.csv

EuroSAT/
  ├── images
  ├── train.csv
  ├── val.csv
  └── test.csv

...
```

We supply our splits in [process_data/data_splits](process_data/data_splits). Also, you can use the code in [process_data](process_data/) folder to process 12 datasets and get your own data splits.

Notably, for fair SOTA comparisons, we use the **test_compare_with_sota files**, which are generated by [code of ATA method](https://github.com/Haoqing-Wang/CDFSL-ATA/tree/master/filelists). 
By the way, if you use their code, you need to transform the JSON file that is generated by [code of ATA method](https://github.com/Haoqing-Wang/CDFSL-ATA/tree/master/filelists) to CSV file. 
Then, you need to put these split files in each corresponding dataset folder for SOTA comparison experiments.

<hr />


## Training and Evaluation
Please follow the instructions for training, evaluating, and reproducing the results.
Firstly, you can modify the name of the CFG file that trains on different models. These CFG files are in [our_config](our_config).
### Training 
```bash
bash train.sh
```

### Evaluation
```bash
bash test_all.sh
```

### Resume Training
```bash
bash train_resume.sh
```


## Citation
If our code is helpful to your research or projects, please consider citing:
```bibtex
@inproceedings{bai2024improving,
  title={Improving Cross-domain Few-shot Classification with Multilayer Perceptron},
  author={Bai, Shuanghao and Zhou, Wanqi and Luan, Zhirong and Wang, Donglin and Chen, Badong},
  booktitle={ICASSP 2024-2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  pages={5250--5254},
  year={2024},
  organization={IEEE}
}
```


## Contact
If you have any questions, please create an issue on this repository or contact at baishuanghao@stu.xjtu.edu.cn.


## Acknowledgements

Our code is based on [LibFewShot](https://github.com/RL-VIG/LibFewShot) repository. We thank the authors for releasing their code. If you use their code, please consider citing their work as well.

```bibtex
@article{li2021LibFewShot,
title = {LibFewShot: A Comprehensive Library for Few-Shot Learning},
author={Li, Wenbin and Wang, Ziyi and Yang, Xuesong and Dong, Chuanqi and Tian, Pinzhuo and Qin, Tiexin and Huo Jing and Shi, Yinghuan and Wang, Lei and Gao, Yang and Luo, Jiebo},
journal = {IEEE Transactions on Pattern Analysis &amp; Machine Intelligence},
year = {2023},
number = {01},
issn = {1939-3539},
pages = {1-18}
}
```




