import csv
from time import time 
import plotly.figure_factory as ff
import statistics
import pandas as pd 
import random


df = pd.read_csv('c110.csv')
data=df['temp'].tolist()

population_mean=statistics.mean(data)
sdp=statistics.stdev(data)
print('population sd -----> ',sdp)
print('population MEAN -----> ',population_mean)




def samp_mean():
    sample=[]

    for i in range(0,100):
        temp=data[random.randint(0,len(data)-1)]
        sample.append(temp)
    mean_of_sample=statistics.mean(sample)
    return (mean_of_sample)
 


def cal_mean():
    mean_list=[]
    for i in range(0,1000):
        means=samp_mean()
        mean_list.append(means)

    print(' sampiling sd -----> ',statistics.stdev(mean_list))
    print('MEAN OF sampiling distribution',statistics.mean(mean_list))
    # fig2=ff.create_distplot([mean_list],['ali'],show_hist=False)
    # fig2.show()
    
cal_mean()
