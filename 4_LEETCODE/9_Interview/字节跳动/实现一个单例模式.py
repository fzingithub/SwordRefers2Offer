import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self, x):
        self.x = x
        # import time
        # time.sleep(1)  # 加入干扰元素，造成多线程出现问题

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with cls._instance_lock:  # 加并行锁
                if not hasattr(cls, '_instance'):
                    cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


def task(arg):
    obj = Singleton(arg)
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=(i,))
    t.start()