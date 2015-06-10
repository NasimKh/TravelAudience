'''
Created on Jun 10, 2015

@author: nasim
'''
import numpy as np
import csv as csv
import pandas as pd 
import pylab as py
import matplotlib.pyplot as plt

    
def read_csv_file(filepath):
    csv_file_object=csv.reader(open(filepath,'rb'))
    header=csv_file_object.next()
    
    data=[]
    count=0
    for row in csv_file_object :
        data.append(row)
    data=np.array(data)
    return data

def mostFliedAirportsPandas(data,groupBy,topN,colmn):
    grouped=data.groupby(groupBy)
    frequentAirports=grouped.sum().sort(colmn,ascending=False)[0:topN]
    #frequentAirports=sorted(grouped.size().iteritems(), key=lambda (k,v): (v,k),reverse=True)[0:topN]
    return frequentAirports


if __name__ == '__main__':
    
    
    # Reading the sampled Search file and Sampled booking File
    search=pd.read_csv(r'C:\Users\nasim\workspace\Pandas\data\searches_small_rand.csv', delimiter='^',error_bad_lines=False, infer_datetime_format=True,parse_dates=[0])
    booking=pd.read_csv(r'C:\Users\nasim\workspace\Pandas\data\bookings_small_rand.csv', delimiter='^',error_bad_lines=False, infer_datetime_format=True,parse_dates=[6])
    
###########################TASK1
    print "length of Sampled searches is %s" %len(search.index)
    print "length of sampled booking is %s" %len(booking.index)
    
 
#############################TASK 2
    
    print 'top ten arrivals airports in the world 2013\n %s' %mostFliedAirportsPandas(booking[['arr_port','pax']],'arr_port',10,'pax')


#############################TASK 3
    
    group=search.groupby(['Destination',search['Date'].map(lambda x: x.month)])
    cities=['BCN','AGP','MAD']
    for item in cities:
        group.size().loc[item].plot()
        print group.size().loc[item]   
            
    plt.legend(cities) 
    my_xticks = ['Jan','Feb','March','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    plt.xticks(range(1,13), my_xticks)
    plt.ylabel('Monthly number of searches')   
    plt.show()    
    
##############################task 4
   # for this task i made a new colmn called combi which will concat the origin:destination airport on both file. 
   # at the first step only the searches were accepted that has the same origin:destination as the booking
   # for making this even more accurate I thought that the booking can only take place if the cre_date is after the search date. 
   #the third condition was that the pax has to be greater than zero.
    
    booking.rename(columns=lambda x: str(x).strip())
    search['combi'] = pd.Series(search["Origin"]+':'+search["Destination"])
    search['ind'] = range(0,len(search.index))
    booking['combi'] = pd.Series(booking.dep_port.map(lambda x:str(x).strip()) + ":" +booking.arr_port.map(lambda x:str(x).strip()))#,columns=["combiDA"]))[['combiDA',booking.columns[0],'pax']]
    sameFlights=pd.merge(search[['combi','Date','ind']], booking[['combi',booking.columns[6],'pax']],how='inner')
    wasBooked = sameFlights[((sameFlights['Date']<sameFlights[booking.columns[6]]) & (sameFlights['pax']>0))]['ind']
    search['wasBooked'] = pd.Series(np.tile(0, len(search.index)))
    search['wasBooked'][wasBooked] = 1
    search.drop('combi',inplace=True,axis=1)
    search.to_csv(r'C:\Users\nasim\workspace\Pandas\data\searches_was_booked.csv')
    