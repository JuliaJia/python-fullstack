#_*_coding:utf-8_*_
import os,sys,platform
# BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   #即可得到父目录
# #
WINDOWS_BASE_PATH = "E:\\python\\anaconda\\python_fullstack\\django\\T\\CMDBagent"
# sys.path.append(BASE_PATH)
#for linux
if platform.system() == "Windows":
    # BASE_DIR = '\\'.join(os.path.abspath(os.path.dirname(__file__)).split('\\')[:-1])
    sys.path.append(WINDOWS_BASE_PATH)
else:
    BASE_DIR = '/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
    sys.path.append(BASE_DIR)
#
from core import HouseStark
#

if __name__ == '__main__':

    HouseStark.ArgvHandler(sys.argv)