# coding=gbk
import os
import multiprocessing
from datetime import datetime


bind = '127.0.0.1:8000'

backlog = 512

timeout = 30

worker_class = 'gevent'

workers = multiprocessing.cpu_count() * 2 + 1

reload = True
debug = False

max_requests = 2000

loglevel = 'info'

out_dir = '/data/log/hello/'

now_time = datetime.now()
time_str = datetime.strftime(now_time, '%y-%m-%d')

access_log_name = 'request_%s.log' % time_str
error_log_name = 'error_%s.log' % time_str

access_log_dir = out_dir + 'request/'
error_log_dir = out_dir + 'error/'
if not os.path.exists(access_log_dir):
    os.makedirs(access_log_dir)
if not os.path.exists(error_log_dir):
    os.makedirs(error_log_dir)

accesslog = access_log_dir + access_log_name
errorlog = error_log_dir + error_log_name
if not os.path.isfile(accesslog):
    f = open(accesslog, mode='w', encoding='utf-8')
    f.close()
if not os.path.isfile(errorlog):
    f = open(errorlog, mode='w', encoding='utf-8')
    f.close()