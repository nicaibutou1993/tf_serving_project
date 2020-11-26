import json
import requests
import numpy as np
# X_new = [[1,4,5,7,8],[2,4,5,9,10]]
# input_data_json = json.dumps({
#     "signature_name": "serving_default",
#     "instances": X_new,
# })
# SERVER_URL = 'http://192.168.18.99:8501/v1/models/my_cls_model:predict'
# response = requests.post(SERVER_URL, data=input_data_json)
# response.raise_for_status() # raise an exception in case of error
# response = response.json()
# y_proba = np.array(response["predictions"])
# print(y_proba)
#API_ENDPOINT = "http://localhost:5000/cls/"
sentence = '物 流 慢 的 一 撇 。 2 9 号 下 单 4 号 下 午 才 收 到 货 。 卖 家 未 2 4 小 时 发 货 。 坑 的 一 撇 。 急 用 的 朋 友 就 不 要 考 虑 这 家 店 了 。'

import time
time_time = time.time()
def run(name):
    #time_time = time.time()

    API_ENDPOINT = np.random.choice(
        ['http://localhost:5000/cls/', 'http://localhost:5001/cls/', 'http://localhost:5002/cls/',
         'http://localhost:5003/cls/'])

    r = requests.post(url=API_ENDPOINT, data=sentence.encode('utf-8'))

    print('......',name, time.time() - time_time)
    print(r.text)
import threading


from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=100)

for j in range(100):
    request_list = []
    for i in range(100):
        print(i,j)
        task1 = executor.submit(run, (i))

    # map(task_pool.putRequest, request_list)
    # task_pool.poll()

print(time.time()-time_time)

