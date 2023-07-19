#!/bin/bash

GPU=2
CFGDIR=MTL-miniImageNet--ravi-resnet12-Two_MLP_layer_False-5-5-May-23-2023-10-52-56
DS=mini

# bash test_all.sh
# bash test_all.sh 0 before

DATASETS=(
    'ChestX'   # 1
    'CropDiseases' # 2
    'DeepWeeds'    # 3
    'DTD'  # 4
    'EuroSAT'  # 5
    'Flower102'    # 6
    'ISIC' # 7
    'kaokore'  # 8
    'Omniglot' # 9
    'Resisc45' # 10
    'Sketch' # 11
    'SVNH' # 12
)

for ((i=0; i<12; i++));
do
    DATASET=${DATASETS[i]}
    python3 -m run_test \
        -gpus ${GPU} \
        -res_config_dir ${CFGDIR} \
        -domain_set ${DS} \
        -dataset ${DATASET} \
        -cross \

done

