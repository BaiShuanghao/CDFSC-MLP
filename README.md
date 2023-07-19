# CDFSC-PEM


## Installation 
For installation and other package requirements, please follow the instructions as follows. 
This codebase is tested on Ubuntu 18.04 LTS with python 3.7. Follow the below steps to create environment and install dependencies.

* Setup conda environment.
```bash
# Create a conda environment
conda create -y -n pem python=3.7

# Activate the environment
conda activate pem

# Install torch (requires version >= 1.5.0) and torchvision
# Please refer to https://pytorch.org/get-started/previous-versions/ if your cuda version is different
conda install pytorch==1.12.0 torchvision==0.13.0 torchaudio==0.12.0 cudatoolkit=11.3 -c pytorch
```

* Clone PEM code repository and install requirements
```bash
# Clone PEM code base
git clone https://github.com/BaiShuanghao/CDFSC-PEM.git

cd CDFSC-PEM/

# Install requirements
pip install -r requirements.txt
```

## Data preparation
Please follow the instructions as follows to prepare all datasets.
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
- [Sketch](https://github.com/HaohanWang/ImageNet-Sketcht)
- [SVNH](http://ufldl.stanford.edu/housenumbers/)

<hr />


## Training and Evaluation
Please follow the instructions for training, evaluating and reproducing the results.
Firstly, you can modify the name of cfg file if you need.
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

<hr />

## Citation
If you use our work, please consider citing:
```bibtex
xxxxxxxxxxxxxxxxxxxxx
```


## Acknowledgements

Our code is based on [LibFewShot](https://github.com/RL-VIG/LibFewShot) repository. We thank the authors for releasing their code. If you use their model and code, please consider citing these works as well.

