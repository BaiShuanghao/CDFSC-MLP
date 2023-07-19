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

* Clone APT code repository and install requirements
```bash
# Clone APT code base
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
Firstly, you need to modify the directory of data.
### Training 
```bash
# trains on Office-Home dataset, and the source domian is art and the target domain is clipart (a-c)
bash scripts/apt/main_apt.sh officehome b32_ep10_officehome APT ViT-B/16 2 a-c 0
```

### Evaluation
```bash
# evaluates on Office-Home dataset, and the source domian is art and the target domain is clipart (a-c)
bash scripts/apt/eval_apt.sh officehome b32_ep10_officehome APT ViT-B/16 2 a-c 0
```
The details are at each method folder in [scripts folder](scripts/).
<hr />

## Citation
If you use our work, please consider citing:
```bibtex
xxxxxxxxxxxxxxxxxxxxx
```


## Acknowledgements

Our code is based on [CoOp and CoCoOp](https://github.com/KaiyangZhou/CoOp), [DAPL](https://github.com/LeapLabTHU/DAPrompt/tree/main) and [MaPLe](https://github.com/muzairkhattak/multimodal-prompt-learning) etc. repository. We thank the authors for releasing their code. If you use their model and code, please consider citing these works as well.
Supported methods are as follows:

| Method                    | Paper                                         |                             Code                            |  
|---------------------------|:----------------------------------------------:|:---------------------------------------------------------------:|
| CoOp                      | [IJCV 2022](https://arxiv.org/abs/2109.01134) |  [link](https://github.com/KaiyangZhou/CoOp)                         |
| CoCoOp                    | [CVPR 2022](https://arxiv.org/abs/2203.05557) |  [link](https://github.com/KaiyangZhou/CoOp)                         |
| VPT*                      | [-](https://arxiv.org/abs/2203.17274)         |  [link](https://github.com/hjbahng/visual_prompting)                 |
| VPT                       | [ECCV 2022](https://arxiv.org/abs/2203.17274) |  [link](https://github.com/KMnP/vpt)                                 |
| IVLP & MaPLe              | [CVPR 2023](https://arxiv.org/abs/2210.03117) | [link](https://github.com/muzairkhattak/multimodal-prompt-learning)  |
| DAPL                      | [-](https://arxiv.org/abs/2202.06687)         | [link](https://github.com/LeapLabTHU/DAPrompt)                       |
