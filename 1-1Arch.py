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
d=[]
e=[]
f=[]

for i in range(len(a)):
    b.append(a[i])

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

print d

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

    print events
    sortedEvents = sorted(events, key=itemgetter(1))
    print sortedEvents

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
    print final_avg
    final_averages.append(final_avg)
print final_averages

plotly.offline.plot({
    "data": [
        Scatter(x=[1, 2, 4, 6, 8, 10, 12, 14.16, 18, 20, 22, 24], y=final_averages)

    ],
    "layout": Layout(
        title="1-1 Server Client Architecture"
    )
})

