# -*- coding: utf-8 -*-
import datetime
from operator import itemgetter
import plotly
print(plotly.__version__)  # version >1.9.4 required
from plotly.graph_objs import Scatter, Layout

from Tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

file = open(filename,"r")
#print file.read()
a= file.read().split(',')


b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]
k=[]





for i in range(0,len(a)/8):
    b.append(a[i])
for i in range(len(a)/8,len(a)/4):
    c.append(a[i])
for i in range(len(a)/4, (3*len(a))/8):
    d.append(a[i])
for i in range((3*len(a))/8, len(a)/2 ):
    e.append(a[i])
for i in range(len(a)/2,(5*len(a))/8):
    f.append(a[i])
for i in range((5*len(a))/8, (3*len(a))/4):
    g.append(a[i])
for i in range((3*len(a))/4,(7*len(a))/8):
    h.append(a[i])
for i in range((7*len(a))/8,len(a)):
    k.append(a[i])


m=[]
n=[]
o=[]


index =0
while index < len(b) :
    m.append(float(b[index]))
    index +=3
index=1
while index < len(b) :
    date_time_obj = datetime.datetime.strptime(b[index], ' %Y-%m-%d %H:%M:%S.%f ')
    time=date_time_obj
    n.append(time)
    index +=3
index=2
while index < len(b) :
    date_time_obj = datetime.datetime.strptime(b[index], '%Y-%m-%d %H:%M:%S.%f ')
    time = date_time_obj
    o.append(time)
    index +=3

lo=[]
for i in n:
    for j in o:
        lo.append(((i-j).total_seconds()))
        break


# print m
# print n
# print o
# print lo
#
#




f1=[]
g1=[]
h1=[]



index =0
while index < len(c) :
    f1.append(float(c[index]))
    index +=3
index=1
while index < len(c) :
    date_time_obj = datetime.datetime.strptime(c[index], ' %Y-%m-%d %H:%M:%S.%f ')
    time=date_time_obj
    g1.append(time)
    index +=3
index=2
while index < len(c) :
    date_time_obj = datetime.datetime.strptime(c[index], '%Y-%m-%d %H:%M:%S.%f ')
    time = date_time_obj
    h1.append(time)
    index +=3

l1=[]
for i in g1:
    for j in h1:
        l1.append(((i-j).total_seconds()))
        break

#
# print f1
# print g1
# print h1
# print l1
#


f2=[]
g2=[]
h2=[]




index =0
while index < len(d) :
    f2.append(float(d[index]))
    index +=3
index=1
while index < len(d) :
    date_time_obj = datetime.datetime.strptime(d[index], ' %Y-%m-%d %H:%M:%S.%f ')
    time=date_time_obj
    g2.append(time)
    index +=3
index=2
while index < len(d) :
    date_time_obj = datetime.datetime.strptime(d[index], '%Y-%m-%d %H:%M:%S.%f ')
    time = date_time_obj
    h2.append(time)
    index +=3

l2=[]
for i in g2:
    for j in h2:
        l2.append(((i-j).total_seconds()))
        break


# print f2
# print g2
# print h2
# print l2
#



f3=[]
g3=[]
h3=[]




index =0
while index < len(e) :
    f3.append(float(e[index]))
    index +=3
index=1
while index < len(e) :
    date_time_obj = datetime.datetime.strptime(e[index], ' %Y-%m-%d %H:%M:%S.%f ')
    time=date_time_obj
    g3.append(time)
    index +=3
index=2
while index < len(d) :
    date_time_obj = datetime.datetime.strptime(e[index], '%Y-%m-%d %H:%M:%S.%f ')
    time = date_time_obj
    h3.append(time)
    index +=3

l3=[]
for i in g3:
    for j in h3:
        l3.append(((i-j).total_seconds()))
        break

#
# print f3
# print g3
# print h3
# print l3


f4=[]
g4=[]
h4=[]




index =0
while index < len(f) :
    f4.append(float(f[index]))
    index +=3
index=1
while index < len(f) :
    date_time_obj = datetime.datetime.strptime(f[index], ' %Y-%m-%d %H:%M:%S.%f ')
    time=date_time_obj
    g4.append(time)
    index +=3
index=2
while index < len(f) :
    date_time_obj = datetime.datetime.strptime(f[index], '%Y-%m-%d %H:%M:%S.%f ')
    time = date_time_obj
    h4.append(time)
    index +=3

l4=[]
for i in g4:
    for j in h4:
        l4.append(((i-j).total_seconds()))
        break

#
# print f4
# print g4
# print h4
# print l4


f5=[]
g5=[]
h5=[]




index =0
while index < len(g) :
    f5.append(float(g[index]))
    index +=3
index=1
while index < len(g) :
    date_time_obj = datetime.datetime.strptime(g[index], ' %Y-%m-%d %H:%M:%S.%f ')
    time=date_time_obj
    g5.append(time)
    index +=3
index=2
while index < len(g) :
    date_time_obj = datetime.datetime.strptime(g[index], '%Y-%m-%d %H:%M:%S.%f ')
    time = date_time_obj
    h5.append(time)
    index +=3

l5=[]
for i in g5:
    for j in h5:
        l5.append(((i-j).total_seconds()))
        break


# print f5
# print g5
# print h5
# print l5



f6=[]
g6=[]
h6=[]




index =0
while index < len(h) :
    f6.append(float(h[index]))
    index +=3
index=1
while index < len(h) :
    date_time_obj = datetime.datetime.strptime(h[index], ' %Y-%m-%d %H:%M:%S.%f ')
    time=date_time_obj
    g6.append(time)
    index +=3
index=2
while index < len(h) :
    date_time_obj = datetime.datetime.strptime(h[index], '%Y-%m-%d %H:%M:%S.%f ')
    time = date_time_obj
    h6.append(time)
    index +=3

l6=[]
for i in g6:
    for j in h6:
        l6.append(((i-j).total_seconds()))
        break


# print f6
# print g6
# print h6
# print l6
#


f7=[]
g7=[]
h7=[]




index =0
while index < len(k) :
    f7.append(float(k[index]))
    index +=3
index=1
while index < len(k) :
    date_time_obj = datetime.datetime.strptime(k[index], ' %Y-%m-%d %H:%M:%S.%f ')
    time=date_time_obj
    g7.append(time)
    index +=3
index=2
while index < len(k) :
    date_time_obj = datetime.datetime.strptime(k[index], '%Y-%m-%d %H:%M:%S.%f ')
    time = date_time_obj
    h7.append(time)
    index +=3

l7=[]
for i in g7:
    for j in h7:
        l7.append(((i-j).total_seconds()))
        break


# print f7
# print g7
# print h7
# print l7
#








#GRAPH PLOT CODE



# q4=[e+f+g+h+i+j+k+l for e,f,g,h,i,j,k,l  in zip(m,f1,f2,f3,f4,f5,f6,f7)]
#
# print q4
#
# final=[]
# for i in q4:
#     for j in lo:
#         a=i/abs(j)
#         a=a*0.001
#         final.append(a)
#         break
# print final
#
#
#
# plotly.offline.plot({
# "data": [
#      Scatter(x=[1,2,4,6,8,10,12,14.16,18,20,22.24], y=final)
#
# ],
# "layout": Layout(
#     title=" Single Wire No switch"
# )
# })



final_averages=[]
for a in range(12):

    events=[]
    speedEvent = []
    speedEvent.append(m[a])
    speedEvent.append(n[a])
    events.append(speedEvent)
    speedEvent1=[]
    speedEvent1.append(-m[a])
    speedEvent1.append(o[a])
    events.append(speedEvent1)
    speedEvent2=[]
    speedEvent2.append(f1[a])
    speedEvent2.append(g1[a])
    events.append(speedEvent2)
    speedEvent3=[]
    speedEvent3.append(-f1[a])
    speedEvent3.append(h1[a])
    events.append(speedEvent3)
    speedEvent4 = []
    speedEvent4.append(f2[a])
    speedEvent4.append(g2[a])
    events.append(speedEvent4)
    speedEvent5 = []
    speedEvent5.append(-f2[a])
    speedEvent5.append(h2[a])
    events.append(speedEvent5)
    speedEvent6 = []
    speedEvent6.append(f3[a])
    speedEvent6.append(g3[a])
    events.append(speedEvent6)
    speedEvent7 = []
    speedEvent7.append(-f3[a])
    speedEvent7.append(h3[a])
    events.append(speedEvent7)
    speedEvent8 = []
    speedEvent8.append(f4[a])
    speedEvent8.append(g4[a])
    events.append(speedEvent8)
    speedEvent9 = []
    speedEvent9.append(-f4[a])
    speedEvent9.append(h4[a])
    events.append(speedEvent9)
    speedEvent10 = []
    speedEvent10.append(f5[a])
    speedEvent10.append(g5[a])
    events.append(speedEvent10)
    speedEvent11 = []
    speedEvent11.append(-f5[a])
    speedEvent11.append(h5[a])
    events.append(speedEvent11)
    speedEvent12 = []
    speedEvent12.append(f6[a])
    speedEvent12.append(g6[a])
    events.append(speedEvent12)
    speedEvent13 = []
    speedEvent13.append(-f6[a])
    speedEvent13.append(h6[a])
    events.append(speedEvent13)
    speedEvent14 = []
    speedEvent14.append(f7[a])
    speedEvent14.append(g7[a])
    events.append(speedEvent14)
    speedEvent15 = []
    speedEvent15.append(-f7[a])
    speedEvent15.append(h7[a])
    events.append(speedEvent15)
    print events
    sortedEvents= sorted(events, key=itemgetter(1))
    #print sortedEvents





    # speed.append(f2[a])
    # events.append(g2[a])
    # events.append(h2[a])
    # speed.append(f3[a])
    # events.append(g3[a])
    # events.append(h3[a])
    # speed.append(f4[a])
    # events.append(g4[a])
    # events.append(h4[a])
    # speed.append(f5[a])
    # events.append(g5[a])
    # events.append(h5[a])
    # speed.append(f6[a])
    # events.append(g6[a])
    # events.append(h6[a])
    # speed.append(f7[a])
    # events.append(g7[a])
    # events.append(h7[a])


    curr_speed=0

    Ts=sortedEvents[0][1]
    combine=[]
    for i in range(len(sortedEvents)):
        pair=[]
        if i<(len(sortedEvents)-1):
            a=i+1
        else:
            a=i
        curr_event =  sortedEvents[a][1]
        delta_t= curr_event- Ts
        curr_speed= curr_speed + sortedEvents[i][0]
        pair.append(curr_speed)
        pair.append(abs(delta_t.total_seconds()))
        combine.append(pair)
        Ts=curr_event
    #print combine

    total_n = 0
    for i in range(len(combine)):

        total_n+=combine[i][1]
    prod=0
    for i in range(len(combine)):
        curr_prod=(combine[i][0])*(combine[i][1])
        prod=prod+curr_prod

    final_avg=prod/total_n
    final_avg=final_avg*0.001
    print final_avg
    final_averages.append(final_avg)
print final_averages

plotly.offline.plot({
"data": [
     Scatter(x=[1,2,4,6,8,10,12,14.16,18,20,22,24], y=final_averages)

],
"layout": Layout(
    title="8-8 Server Client Architecture"
)
})


    # diff=[]
    # for i in start:
    #     for j in end:
    #
    #         diff.append(abs((i-j).total_seconds()))
    #         break
    # speedss1=[]
    # for i in speed:
    #     a = i * 0.001
    #     speedss1.append(a)
    #
    # import plotly.graph_objs
    #
    # plotly.offline.plot({
    #     "data": [
    #         plotly.graph_objs.Bar(x=diff, y=speedss1)
    #
    #     ]
    # })