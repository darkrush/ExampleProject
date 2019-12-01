import sys
sys.path.append("..")
from src.some_code import sth
import torch
import numpy as np
from utils.argpaser import Singleton_argpaser as args
from utils.logger import Singleton_logger as logger

DEFAULT_DEVICE = torch.device("cuda:0") if torch.cuda.is_available() else torch.device("cpu")
    

def run():
    logger.add_log('Start')
    for i in range(12):
        torch_tensor = torch.rand(size = [2,2],device = DEFAULT_DEVICE)
        data_to_save = torch_tensor.detach().cpu().numpy()
        sth()
        logger.append_data('data',i,data_to_save)
        logger.add_log('%f'%data_to_save[0,0],'INFO')
        logger.add_log('debug','DEBUG')
        logger.dump_log()
    logger.add_log('End')
    logger.dump_data(dump_mat = True)
    