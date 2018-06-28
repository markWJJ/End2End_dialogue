

import pickle


data=pickle.load(open('./user_goals_first_turn_template.v2.p','rb'),encoding='utf-8')


for ele in data:
    print(ele)