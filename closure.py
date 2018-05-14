#  Closure
# A Closure closes over the free variable from their enviroment
def out_func(msg):
  message = msg

  def inner_func():
    print(message)

  return inner_func

hi_func = out_func('Hi')
hi_func()


'''
import logging
logging.basicConfig(filename='example_closure.log', level=logging.INFO)

def logger(func):
  def log_func(*args):
    # logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
    print(func(*args))
  return log_func

def add(x, y):
  return x+y

def sub(x, y):
  return x-y

add_func = logger(add)
sub_func = logger(sub)

add_func(3,5)
sub_func(10, 6)

'''