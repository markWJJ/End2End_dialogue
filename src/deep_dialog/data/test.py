

import pickle


data=pickle.load(open('./movie_kb.1k.p','rb'),encoding='utf-8')


for ele in data:
    print(ele)