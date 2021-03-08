#!usr/bin/env python
#_*_coding=cp936 _*_

"""
#######  
#
#######  By:Shi Zhikai 
#
####### Create Date:2016-07-29
Python 程序后台所需绝对路径

更换运行环境时需要配置此文件
"""


import os.path
import os.path
from functools import partial



###全局变量,指定所需路径
python_path='/it/is/a/test/'
image_path=r'D:\tomcat\apache-tomcat-8.0.23\webapps\HubuTraff\images\\'
zip_log_file_path=''
current_log_file_path='E:\\dataTraffic\\'
unzip_log_file_path=''

















__all__ = [
    'get_dir_walker',
    'walk',
    'listdir',
    'list_directories',
    'list_files',
    'absolute_path',
    'real_absolute_path',
    'parent_dir_path',
]
def get_dir_walker(recursive, topdown=True, followlinks=False):
    if recursive:
        walk = partial(os.walk, topdown=topdown, followlinks=followlinks)
    else:
        def walk(path, topdown=topdown, followlinks=followlinks):
            try:
                yield next(os.walk(path, topdown=topdown, followlinks=followlinks))
            except NameError:
                yield os.walk(path, topdown=topdown, followlinks=followlinks).next() #IGNORE:E1101
    return walk


def walk(dir_pathname, recursive=True, topdown=True, followlinks=False):
    walk_func = get_dir_walker(recursive, topdown, followlinks)
    for root, dirnames, filenames in walk_func(dir_pathname):
        yield (root, dirnames, filenames)


def listdir(dir_pathname,
            recursive=True,
            topdown=True,
            followlinks=False):
    for root, dirnames, filenames\
    in walk(dir_pathname, recursive, topdown, followlinks):
        for dirname in dirnames:
            yield absolute_path(os.path.join(root, dirname))
        for filename in filenames:
            yield absolute_path(os.path.join(root, filename))


def list_directories(dir_pathname,
                     recursive=True,
                     topdown=True,
                     followlinks=False):
    for root, dirnames, filenames\
    in walk(dir_pathname, recursive, topdown, followlinks):
        for dirname in dirnames:
            yield absolute_path(os.path.join(root, dirname))


def list_files(dir_pathname,
               recursive=True,
               topdown=True,
               followlinks=False):
    for root, dirnames, filenames\
    in walk(dir_pathname, recursive, topdown, followlinks):
        for filename in filenames:
            yield absolute_path(os.path.join(root, filename))


def absolute_path(path):

    return os.path.abspath(os.path.normpath(path))


def real_absolute_path(path):
    return os.path.realpath(absolute_path(path))


def parent_dir_path(path):
    return absolute_path(os.path.dirname(path))

def main():
	print 'This program is being run by it self'

if __name__=='__main__':
    main()