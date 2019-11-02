'''
BERT调试数据处理的py文件
'''

import pandas as pd
import numpy as np





lab = pd.read_csv("/home/fantasy/PycharmWorks/bert_pytorch/result.csv") #, usecols = [1])
pd.set_option('display.max_rows', None)
print(lab.sort_values(by = 'tag', ascending = True))
print(lab.describe())

import csv
# file = "/home/fantasy/PycharmWorks/bert_pytorch/train.csv"
#
# with open(file, 'r', encoding = 'UTF-8') as f:
#     reader = csv.DictReader(f)
#     questionlist = []
#     labellist = []
#     for row in reader:
#         questionlist.append(row['question'])
#         labellist.append(row['tag'])
# dict = [questionlist, labellist]
#
# print(dict[1][:])




# list = [[1, 2, 3, 4 ,5], [6, 7, 8, 9, 10]]
# for i in range(len(list[0][:])):
#     print(i)
# for (i, infor) in enumerate(list):
#     guid = "%s-%s" % ('train', i)
#     print(guid, 'and', i, ' and ', infor)
#
# print(list)



# import gzip
# input_file = "/home/fantasy/PycharmWorks/bert_pytorch/train.csv"
# with open(input_file, 'r') as f:
#     reader = csv.DictReader(f)  # 可能要修改？？
#     questionlist = []
#     labellist = []
#     dicts = []
#     i = 0
#     for row in reader:
#         i += 1
#         questionlist.append(row['question'])
#         labellist.append(row['tag'])
# dicts = [questionlist, labellist]
# print(dicts[0][:])
# print(dicts[1][:])
# print(type(dicts))
# print(i)


# -----------------------读取csv文件并将标点与字母分开-------------------------
# import re
# input_file = "/home/fantasy/PycharmWorks/bert_pytorch/train.csv"
# with open(input_file, 'r') as f:
#     reader = pd.read_csv(f)
#     dicts = reader.ix[:, ['question','tag']]
#     # tag = reader.iloc[:, 10]
#     #val = reader.sample(frac = 0.1)
#
#
# # for i in range(len(dicts['question'])):
# #     dicts['question'][i] = re.split(r'([.,;?!\s])', dicts['question'][i])
# #     dicts['question'][i] = [x for x in dicts['question'][i] if x != ' ' and x]
# #
# # print(dicts)
#
# dicts['question'][1] = re.split(r'([.,;?!\'\"\s])', dicts['question'][1])
# dicts['question'][1] = [x for x in dicts['question'][1] if x != ' ' and x]
# dicts['question'][1] = ' '.join(dicts['question'][1])
# print(dicts['question'][1])








# print(val)
# val.to_csv('/home/fantasy/PycharmWorks/bert_pytorch/val.csv', index = False)

# for i in range(len(dicts)):
#     print(dicts.iloc[0]['tag'])


# predict = np.zeros((0,), dtype=np.int32)
# print(predict)





# -----------------------------导出结果--------------------------------
# tag = np.random.randint(0, 35, 899)
# predict = np.random.randint(0, 35, 899)
# input_file = "/home/fantasy/PycharmWorks/bert_pytorch/test.csv"
# with open(input_file, 'r') as f:
#     reader = pd.read_csv(f)
#     dicts = reader.ix[:, ['question','tag']]
#
# # tag = pd.DataFrame(tag)
# # predict = pd.DataFrame(predict)
#
# #print(result)
#
# label_dict = {0:'Adviserefund', 1:'Alreadyrefunded', 2:'Buyerpay', 3:'Canbechanged', 4:'Cancellation', 5:'Cannotbechanged', 6:'DelayOTHERSITES', 7:'DelayUS',
#                  8:'Deliverfailed', 9:'Faster1', 10:'Faster2', 11:'Howtorequest', 12:'Instock', 13:'IntransitGB', 14:'IntransitOTHERSITES', 15:'Invoiceleadtime',
#                  16:'Missing', 17:'Notacceptedreturn', 18:'Notracking', 19:'Ourfault1', 20:'Ourfault2', 21:'Outstock', 22:'Photoproof', 23:'Plswait',
#                  24:'Redelivery', 25:'Refund', 26:'Return_tracking', 27:'ShippingCharge1', 28:'ShippingCharge2', 29:'Tracking', 30:'Wishtochange', 31:'Wishtowait',
#                  32:'mark_as_urgent', 33:'replacement', 34:'when_instock'}
#
# g = []
# p = []
# for i in range(len(tag)):
#     g.append(label_dict[tag[i]])
# for j in range(len(predict)):
#     p.append(label_dict[predict[j]])
#
# result = pd.DataFrame({'question':dicts['question'], 'tag':g, 'predict':p}, columns = ['question', 'tag', 'predict'])
# result.to_csv('/home/fantasy/PycharmWorks/bert_pytorch/result.csv', index = False)



# a = np.arange(3)
# b = []
# for i in range(len(a)):
#     b.append(label_dict[a[i]])
# print(b)