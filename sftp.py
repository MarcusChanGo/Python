#!/usr/local/bin/python3
# coding: utf-8 

import paramiko
import os
from stat import S_ISDIR as isdir


def down_from_remote(sftp_obj, remote_dir_name, local_dir_name):
    remote_file = sftp_obj.stat(remote_dir_name)
    if isdir(remote_file.st_mode):
        check_local_dir(local_dir_name)
        print('开始下载文件夹：' + remote_dir_name)
        for remote_file_name in sftp.listdir(remote_dir_name):
            sub_remote = os.path.join(remote_dir_name, remote_file_name)
            sub_remote = sub_remote.replace('\\', '/')
            sub_local = os.path.join(local_dir_name, remote_file_name)
            sub_local = sub_local.replace('\\', '/')
            down_from_remote(sftp_obj, sub_remote, sub_local)
    else:
        print('开始下载文件：' + remote_dir_name)
        sftp.get(remote_dir_name, local_dir_name)


def check_local_dir(local_dir_name):
    if not os.path.exists(local_dir_name):
        os.makedirs(local_dir_name)


if __name__ == "__main__":
    host_name = '10.247.228.122'
    user_name = 'root'
    password = 'f(69#)BgXA7d'
    port = 22
    remote_dir = '/usr1/code/sdktest_5807/code/current/mutitrack_code/test/sc/build_at/libsdk5807.so'
    local_dir = 'D:/testsdk'

    t = paramiko.Transport((host_name, port))
    t.connect(username=user_name, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)

    down_from_remote(sftp, remote_dir, local_dir)

    t.close()
