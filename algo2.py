# -*- coding: utf-8 -*-
import datetime
import plotly
print(plotly.__version__)  # version >1.9.4 required
from plotly.graph_objs import Scatter, Layout
from operator import itemgetter

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


for i in range(0,len(a)/4):
    b.append(a[i])
for i in range(len(a)/4,len(a)/2):
    c.append(a[i])
for i in range(len(a)/2,((len(a))-(len(a)/4))):
    d.append(a[i])
for i in range(((len(a))-(len(a)/4)),len(a)):
    e.append(a[i])


index =0
while index < len(b) :
    f.append(float(b[index]))
    index +=3
index=1
while index < len(b) :
    date_time_obj = datetime.datetime.strptime(b[index], ' %Y-%m-%d %H:%M:%S.%f ')
    time=date_time_obj
    g.append(time)
    index +=3
index=2
while index < len(b) :
    date_time_obj = datetime.datetime.strptime(b[index], '%Y-%m-%d %H:%M:%S.%f ')
    time = date_time_obj
    h.append(time)
    index +=3

l=[]
for i in g:
    for j in h:
        l.append(((i-j).total_seconds()))
        break

#
# print f
# print g
# print h
# print l
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


# print f3
# print g3
# print h3
# print l3









#GRAPH PLOT CODE



# q4=[e+f+g+h for e,f,g,h  in zip(f,f1,f2,f3)]
#
# print q4
#
# final=[]
# for i in q4:
#     for j in l:
#         a=i/abs(j)
#         a=a*0.001
#         final.append(a)
#         break
# print final



# plotly.offline.plot({
# "data": [
#      Scatter(x=[20,22.24], y=final)
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
    speedEvent.append(f[a])
    speedEvent.append(g[a])
    events.append(speedEvent)
    speedEvent1=[]
    speedEvent1.append(-f[a])
    speedEvent1.append(h[a])
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

    print events
    sortedEvents= sorted(events, key=itemgetter(1))
  #  print sortedEvents

    curr_speed = 0

    Ts = sortedEvents[0][1]
    combine = []
    for i in range(len(sortedEvents)):
        pair = []
        if i<(len(sortedEvents)-1):
            a=i+1
        else:
            a=i
        curr_event =  sortedEvents[a][1]

        delta_t = curr_event - Ts
        curr_speed = curr_speed + sortedEvents[i][0]
        pair.append(curr_speed)
        pair.append(abs(delta_t.total_seconds()))
        combine.append(pair)
        Ts = curr_event
   # print combine

    total_n = 0
    for i in range(len(combine)):
        total_n += combine[i][1]
    prod = 0
    for i in range(len(combine)):
        curr_prod = (combine[i][0]) * (combine[i][1])
        prod = prod + curr_prod

    final_avg = prod / total_n
    final_avg = final_avg * 0.001
    #print final_avg
    final_averages.append(final_avg)
print final_averages

plotly.offline.plot({
    "data": [
        Scatter(x=[1, 2, 4, 6, 8, 10, 12, 14.16, 18, 20, 22, 24], y=final_averages)

    ],
    "layout": Layout(
        title="4-4 Server Client Architecture"
    )
})
