#_*_coding:utf-8_*_
__author__ = 'Alex Li'
import os,sys
BASE_DIR = "E:\\python\\anaconda\\python_fullstack\\django\\T\\CMDBagent\\plugins"
sys.path.append(BASE_DIR)

from linux import linuxSysinfo
from windows import windowsSysinfo




def LinuxSysInfo():
    #print __file__
    return  linuxSysinfo.collect()


def WindowsSysInfo():
    return windowsSysinfo.collect()
