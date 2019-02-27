import plotly
print(plotly.__version__)  # version >1.9.4 required
from plotly.graph_objs import Scatter, Layout

b=[]

for i in a:
    print i
    c=sum(i)
    b.append(c)


c=[]
for i in range(4000):
    c.append(i)


plotly.offline.plot({
"data": [
Scatter(x=c, y=b, name="1-1 Server Client")

],

"layout": Layout(
    title=" 80GB WITHOUT SWITCH 16 CORES",
xaxis=dict(
        title='TIME INSTANT IN MILLISECONDS',
        titlefont=dict(
            family='Arial, sans-serif',
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,
        tickangle=45,
        tickfont=dict(
            family='Old Standard TT, serif',
            size=14,
            color='black'
        ),
        exponentformat='e',
        showexponent='all'
    ),
    yaxis=dict(
        title='CPU UTILIZATION',
        titlefont=dict(
            family='Arial, sans-serif',
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,
        tickangle=45,
        tickfont=dict(
            family='Old Standard TT, serif',
            size=14,
            color='black'
        ),
        exponentformat='e',
        showexponent='all'
    )

)
})




