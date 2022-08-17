# Python 3.8
# file: arguments.py
# url: https://docs.python.org/ko/3/library/multiprocessing.html
# author: steve.jeong

import argparse
import time
import os
import multiprocessing as mp

num = 50

class parallel:
  def __init__(self):
    self.new = 1

  def func_pipe(self, conn):
    print(conn.recv())
    conn.send([21, None, 'send from child_conn'])
    conn.close()

  def func_pool(self, process_name): # it is count f.
    for i in range(1, 100001):
      print(process_name, i)
    
  def func_process(self, name): # it is print pid f.
    global num

    num += 1
    print('pid of parent: ', os.getppid())
    print('pid of %s : %d' % (name, os.getpid()))
    print('%d' % num)

  def func_queue(self, q, l:list):
    q.put(l)

  def func_value_and_array(self, n, arr, idx):
    n.value = idx
    for i in range(len(arr)):
        arr[i] = -arr[i]

  def use_pipe(self):
      parent_conn, child_conn = mp.Pipe()
      parent_conn.send([22, None, 'send form parent_conn'])
      ps = mp.Process(target=self.func_pipe, args=(child_conn,))

      ps.start()
      print(parent_conn.recv())
      ps.join()

  def use_pool(self):
    start_time = time.time()
    ps_list = ['proc_1', 'proc_2', 'proc_3', 'proc_4']
    pool = mp.Pool(processes = 4)
    pool.map(self.func_pool, ps_list)
    pool.close()
    pool.join()
    print(time.time() - start_time)

  def use_process(self):
    ps1 = mp.Process(target=self.func_process, args=('proc_1',))
    ps2 = mp.Process(target=self.func_process, args=('proc_2',))
    ps1.start(); ps1.join()
    ps2.start(); ps2.join()

  def use_queue(self):
    q = mp.Queue()
    ps1 = mp.Process(target=self.func_queue, args=(q, [7, None, 'process 1']))
    ps2 = mp.Process(target=self.func_queue, args=(q, [9, None, 'process 2']))

    ps1.start()
    print(q.get())
    ps1.join()

    ps2.start()
    print(q.get())
    ps2.join()

  def use_value_and_array(self):
    num = mp.Value('d', 0.0)
    arr = mp.Array('i', range(10))

    ps1 = mp.Process(target=self.func_value_and_array, args=(num, arr, 1))
    ps1.start()
    ps1.join()

    ps2 = mp.Process(target=self.func_value_and_array, args=(num, arr, 2))
    ps2.start()
    ps2.join()

    print(num.Value)
    print(arr[:])

if __name__ == '__main__':
  mode = parallel()

  parser = argparse.ArgumentParser(
    description = 'parallel codes in python3',
    formatter_class = argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument(
      '-m', '--mode', default='procsss', help='select funcs in multiprocessing')

  args = parser.parse_args()
  if args.mode == "pipe":
    mode.use_pipe()
  elif args.mode == "pool":
    mode.use_pool()
  elif args.mode == "process":
    mode.use_process()
  elif args.mode == "queue":
    mode.use_queue()
  elif args.mode == "value-array":
    mode.use_value_and_array()
  else:
    print("Invalid option!")
    print("e.g. python3 parallel.py -m process")

# vim: set ft=python ts=2 sw=2 sts=2 et
