# -*- coding:utf-8 -*- 
__author__ = 'czk'
__date__ = '2021/1/27 8:02 下午'
# 批量、直接 删除 指定目录下 的子文件及子文件夹后缀名，不递归
# from CZKTool import *
import  os
# 设置一级目录
# root_dir=os.curdir
root_dir=os.curdir+os.sep+"内部资源"
# 设置要删掉的文件夹名称后缀
houzhui_del="-目录"
# 获得该目录下都有哪些一级文件夹
dirs=os.listdir(root_dir)
astr=dirs
print(astr)
# 获得文件夹的名称
for adir in dirs:
    # 判断是否该删
    if adir.endswith(houzhui_del):
        new_dir=adir.replace(houzhui_del,"")
        # 尝试重命名文件夹，
        old_fullpath=root_dir+os.sep+adir
        new_fullpath=root_dir+os.sep+new_dir
        os.rename(old_fullpath,new_fullpath)




# 如果失败，就抛出异常

