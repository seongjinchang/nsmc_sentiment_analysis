import logging
import torch
import random
import numpy as np


def init_logger():
    logging.basicConfig(format='%(asctime)s %(clientip)-15s %(user)-8s %(message)s',
                        level=logging.INFO)


def set_device():
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")


def set_seed():
    random.seed(42)
    np.random.seed(42)
    torch.manual_seed(42)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(42)