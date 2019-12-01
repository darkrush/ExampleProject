import sys
sys.path.append("..")
from utils.argpaser import Singleton_argpaser as args
from utils.logger import Singleton_logger as logger

def sth():
    logger.add_log('run sth','DEBUG')