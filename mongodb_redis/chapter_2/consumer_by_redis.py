'''
Author: geekli
Date: 2021-01-06 18:37:07
LastEditTime: 2021-01-06 18:37:07
LastEditors: your name
Description: 
FilePath: /database/mongodb_redis/chapter2/consumer_by_redis.py
'''
import json
import time
import redis
import random
from threading import Thread


class Consumer(Thread):
    def __init__(self):
        super().__init__()
        self.queue = redis.Redis()

    def run(self):
        while True:
            num_tuple = self.queue.blpop('producer')
            a, b = json.loads(num_tuple[1].decode())
            print(f'消费者消费了一组数，{a} + {b} = {a + b}')
            time.sleep(random.randint(0, 10))


consumer = Consumer()
consumer.start()
consumer.join()
