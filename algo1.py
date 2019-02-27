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


for i in range(0,len(a)/2):
    b.append(a[i])
for i in range(len(a)/2,len(a)):
    c.append(a[i])

print b


index =0
while index < len(b) :
    d.append(float(b[index]))
    index +=3
index=1
while index < len(b) :
    date_time_obj = datetime.datetime.strptime(b[index], ' %Y-%m-%d %H:%M:%S.%f ')
    time=date_time_obj
    e.append(time)
    index +=3

index=2
while index < len(b) :
    date_time_obj = datetime.datetime.strptime(b[index], '%Y-%m-%d %H:%M:%S.%f ')
    time = date_time_obj
    f.append(time)
    index +=3
l=[]
for i in e:
    for j in f:
        l.append(((i-j).total_seconds()))
        break

# print d
# print e
# print f
# print l


g=[]
h=[]
p=[]


index =0
while index < len(c) :
    g.append(float(c[index]))
    index +=3
index=1
while index < len(c) :
    date_time_obj = datetime.datetime.strptime(c[index], ' %Y-%m-%d %H:%M:%S.%f ')
    time=date_time_obj
    h.append(time)
    index +=3

index=2
while index < len(c) :
    date_time_obj = datetime.datetime.strptime(c[index], '%Y-%m-%d %H:%M:%S.%f ')
    time = date_time_obj
    p.append(time)
    index +=3
m=[]

for x in h:
    for j in p:
        m.append(((x-j).total_seconds()))
        break
#
# print g
# print h
# print p
# print m

# avg = []
#
# for i in range(12):
#     event=[e[i],h[i],f[i],p[i]]
#     speed=[d[i],g[i]]
#     start=[e[i],h[i]]
#     end=[f[i],p[i]]
#     diff=[l[i],m[i]]
#     event.sort()
#     # for i in end:
#     #     for j in start:
#     #         event.append(min(start))
#     #         start.remove(min(start))
#     #     event.append(min(end))
#     #     end.remove(min(end))
#
#     #for i in range(2):
#
#      #   j=i+1
#     print event
#
#     longProd=[]
#     longDiff=[]
#     a12 = 0
#
#     for i in range(len(event)-1):
#         j=i+1
#         if i==0 or i==2:
#             instDiff=abs((event[i] - event[j]).total_seconds())
#             instspeed= speed[a12]
#             a12=a12+1
#             prod=instDiff*instspeed
#             longProd.append(prod)
#             longDiff.append(instDiff)
#         else:
#             instDiff = abs((event[i] - event[j]).total_seconds())
#             instspeed = speed[0]+speed[1]
#             prod=instDiff*instspeed
#             longProd.append(prod)
#             longDiff.append(instDiff)
#
#     instavg=sum(longProd)/sum(longDiff)
#     avg.append(instavg)
#
#
# gbps=[]
# for i in avg:
#     gb=i*0.001
#     gbps.append(gb)
# print gbps
#



final_averages=[]
for a in range(12):

    events=[]
    speedEvent = []
    speedEvent.append(d[a])
    speedEvent.append(e[a])
    events.append(speedEvent)
    speedEvent1=[]
    speedEvent1.append(-d[a])
    speedEvent1.append(f[a])
    events.append(speedEvent1)
    speedEvent2=[]
    speedEvent2.append(g[a])
    speedEvent2.append(h[a])
    events.append(speedEvent2)
    speedEvent3=[]
    speedEvent3.append(-g[a])
    speedEvent3.append(p[a])
    events.append(speedEvent3)

   # print events
    sortedEvents= sorted(events, key=itemgetter(1))
    #print sortedEvents

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
        curr_speed += sortedEvents[i][0]
        pair.append(curr_speed)
        pair.append(abs(delta_t.total_seconds()))
        combine.append(pair)
        Ts = curr_event
    print combine

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
        title="2-2 Server Client Architecture"
    )
})


# q=[e+f for e,f  in zip(d,g)]
#
# print q
#
# final=[]
# for i in q:
#     for j in l:
#         a=i/abs(j)
#         a=a*0.001
#         final.append(a)
#         break
# print final

# print gbps
#
# plotly.offline.plot({
# "data": [
#      Scatter(x=[1,2,4,6,8,10,12,14.16,18,20,22.24], y=gbps)
#
# ],
# "layout": Layout(
#     title=" Single Wire No switch"
# )
# })



# diff=[]
#
# for i in q:
#     for j in m:
#         diff.append((i-j).total_seconds())
#         break
# print diff





# index =0
# while index < len(c) :
#     e.append(float(c[index]))
#     index +=3
#
# print d
# print e
#
#
# q=[e+f for e,f  in zip(d,e)]
#
# o=[]
# for i in q:
#     i = i * 0.001
#     o.append(i)
# print o
#
# k=0
# for i in o:
#     k=k+i
#
# k=k/len(o)
# print k
#



