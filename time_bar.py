#!/usr/bin python
# --*-- coding:utf-8 --*--

import time
import progressbar
from tqdm import tqdm 


# N = 1000
# st = time.clock()
# for i in range(N):
#     p = round((i + 1) * 100 / N)
#     duration = round(time.clock() - st, 2)
#     remaining = round(duration * 100 / (0.01 + p) - duration, 2)
#     print("进度:{0}%,已耗时:{1}s,预计剩余时间:{2}s".format(p, duration, remaining), end='\r')
#     time.sleep(0.01)


# p = progressbar.ProgressBar()
# N = 1000
# p.start()
# for i in p(range(N)):
#     time.sleep(0.01)
#     p.update(i + 1)
# p.finish()


# total = 1000
 
# def dosomework():
#     time.sleep(0.01)
 
# widgets = ['Progress: ',progressbar.Percentage(), ' ', progressbar.Bar('#'),' ', progressbar.Timer(), ' ', 
#         progressbar.ETA(), ' ', progressbar.FileTransferSpeed()]
# pbar = progressbar.ProgressBar(widgets=widgets, maxval=10*total).start()
# for i in range(total):
#     # do something
#     pbar.update(10 * i + 1)
#     dosomework()
# pbar.finish()



# for i in tqdm.tnrange(4, desc="1st loop"):
#     for j in tqdm.tnrange(100, desc="2nd loop"):
#         time.sleep(0.01)



# def viewBar(i):
#     """
#     进度条效果
#     :param i:
#     :return:
#     """
#     output = sys.stdout
#     for count in range(0, i + 1):
#         second = 0.1
#         sleep(second)
#         output.write('\rcomplete percent:%.0f%%' % count)
#     output.flush()

# viewBar(200)


for i in tqdm(range(1000)):
    pass
