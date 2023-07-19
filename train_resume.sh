#!/bin/bash

GPU=0
NGPU=1
CFG=RFSModel-miniImageNet--ravi-resnet12-Two_MLP_layer_False-5-5-May-22-2023-12-00-02  # config file in trained file
DS=mini

python3 -m run_trainer_resume \
    -gpus ${GPU} \
    -n_gpu ${NGPU} \
    -config_name ${CFG} \
    -domain_set ${DS}


