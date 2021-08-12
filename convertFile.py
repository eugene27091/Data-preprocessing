import pandas as pd
import numpy as np
from itertools import chain
import datetime

df = pd.read_csv('C:/Users/EUGENE/PycharmProjects/dogpre_final/2021_08_11_12-41-14dogpre.csv') #파일 불러오기(경로 지정하셔야되요)

def chainer(s):
    return list(chain.from_iterable(s.str.split(',')))

# calculate lengths of splits
lens = df['review_date'].str.split(',').map(len)

# 'item_name', 'review_title', 'review_content','review_date', 'review_star', 'dog_breed', 'dog_age'

# print(chainer(df['review_title']))
print("review_title 개수")
print(len(chainer(df['review_title'])))

# print(chainer(df['review_content']))
print("review_content 개수")
print(len(chainer(df['review_content'])))


res = pd.DataFrame({'item_name': np.repeat(df['item_name'],lens),
                    'review_title': chainer(df['review_title']),
                    'review_content': chainer(df['review_content']),
                    'review_date': chainer(df['review_date']),
                    'review_star': chainer(df['review_star']),
                    'dog_breed': chainer(df['dog_breed']),
                    'dog_age': chainer(df['dog_age'])})

# res["review_total"] = res["review_title"].map(str) + " " + res["review_content"]
# res = res.drop(columns = ['review_title', 'review_content'])

print(res)

now = datetime.datetime.now()
nowDate = now.strftime("%Y_%m_%d_%H-%M-%S")

res.to_csv( str(nowDate) + 'dogPre' + '.csv', encoding='utf-8-sig')
print("Finish!")