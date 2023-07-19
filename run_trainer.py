# -*- coding: utf-8 -*-
import sys
import os
from core.config import Config

config_file = None
config = Config(config_file, is_train=True).get_config_dict()
os.environ["CUDA_VISIBLE_DEVICES"] = str(config["device_ids"])
sys.dont_write_bytecode = True

import torch
from core.trainer import Trainer


def main(rank, config):
    trainer = Trainer(rank, config)
    trainer.train_loop(rank)


if __name__ == "__main__":
    if config["n_gpu"] > 1:
        config["device_ids"] = "0,1"
        torch.multiprocessing.spawn(main, nprocs=config["n_gpu"], args=(config,))
    else:
        main(0, config)
