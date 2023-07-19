# -*- coding: utf-8 -*-
import sys
import os
from core.config import Config

VAR_DICT = {
    "test_epoch": 5,
    "device_ids": "0",
    "n_gpu": 1,
    "test_episode": 600,
    "episode_size": 2,
}
config_file = None
config, path = Config(config_file, VAR_DICT, is_train=False).get_config_dict()
os.environ["CUDA_VISIBLE_DEVICES"] = str(config["device_ids"])
sys.dont_write_bytecode = True

import torch
from core.test import Test


def main(rank, config, path):
    if config["dataset"] != 'miniImgaNet':
        test = Test(rank, config, path, config["dataset"])
    else:
        test = Test(rank, config, path)
    test.test_loop()


if __name__ == "__main__":
    if config["n_gpu"] > 1:
        config["device_ids"] = "0,1"
        torch.multiprocessing.spawn(main, nprocs=config["n_gpu"], args=(config, path))
    else:
        main(0, config, path)

