#!/bin/bash

GPU=0
NGPU=1
CFG=protonet_res12_55_mini.yaml  # config file
DS=mini

python3 -m run_trainer \
    -gpus ${GPU} \
    -n_gpu ${NGPU} \
    -config_name ${CFG} \
    -domain_set ${DS}

