import plotly
print(plotly.__version__)  # version >1.9.4 required
from plotly.graph_objs import Scatter, Layout


a1=[37.70056531350422, 39.162064227049015, 43.005891034754974, 37.72816432099586, 34.971690200346565, 34.05218834641151, 42.80057697396544, 36.295728872463656, 35.79396962640792, 34.78720317127993, 34.07531363539192, 33.18560005613869]
a2=[45.60053108991353, 45.61980455787415, 45.4987038478302, 45.68411122565996, 45.84313594135093, 46.3552616944185, 46.47467231858527, 46.4501766857547, 46.54820086216191, 55.491025304609636, 34.04890002158793, 23.16696158357805]
a3=[45.739210252442966, 45.718221559436024, 46.24375009950273, 46.405955162219605, 46.41730043908235, 46.75929713124666, 52.80106344669338, 59.48814224708126, 52.27107347877946, 44.61014216973543, 41.849930666194396, 38.64014129548365]
a4=[45.87564580764436, 46.01537647361425, 46.23094913960018, 47.15757186351951, 47.03737102983749, 46.381387923757174, 62.78038394690707, 60.31755510686176, 69.92550669552293, 61.36334498500264, 65.38893568483395, 56.150299736401855]
a5=[49.478154443072576, 49.1631314573986, 51.174092913451744, 51.24838454038377, 49.04983585589138, 47.89578710977183, 71.52293604585877, 61.09168479260873, 67.55509303548084, 67.61926969768533, 59.58920606300496, 51.56396172460529]
#a5=[37.530300515458336, 38.50648285374134, 38.46451777770777, 38.640642387282, 38.94933302569253, 58.95171772837839, 59.25547568623444, 54.39196936848063, 46.08093709122237, 44.90475455172179, 32.0046650435541, 40.52405716294153]
#a6=[37.74304900766578, 38.37283165778166, 38.53430404888612, 38.78778206811628, 38.53396241872188, 59.423962582900124, 57.39861376665549, 49.569951795169125, 60.01330050864049, 51.10214749583308, 61.628165628277216, 51.68284994835554]

# k=[]
# l=[]
# m=[]
# n=[]
# o=[]
# p=[]
# q=[]
# for i in a:
#     i=i*0.001
#     j.append(i)
# for i in b:
#     i=i*0.001
#     k.append(i)
# for i in c:
#     i=i*0.001
#     l.append(i)
# for i in d:
#     i=i*0.001
#     m.append(i)
# for i in e:
#     i=i*0.001
#     n.append(i)
# for i in f:
#     i=i*0.001
#     o.append(i)
# for i in g:
#     i=i*0.001
#     p.append(i)
# for i in h:
#     i=i*0.001
#     q.append(i)




plotly.offline.plot({
"data": [
Scatter(x=[1,2,4,6,8,10,12,14.16,18,20,22.24], y=a1, name="2-2 Server Client"),
Scatter(x=[1,2,4,6,8,10,12,14.16,18,20,22.24], y=a2, name="4-4 Server Client"),
Scatter(x=[1,2,4,6,8,10,12,14.16,18,20,22.24], y=a3, name="8-8 Server Client"),
 Scatter(x=[1,2,4,6,8,10,12,14.16,18,20,22.24], y=a4, name="12-12 Server Client"),
 Scatter(x=[1,2,4,6,8,10,12,14.16,18,20,22.24], y=a5, name="16-16 Server Client")
# Scatter(x=[1,2,4,6,8,10,12,14.16,18,20,22.24], y=a6, name="16-16 Server Client")



],

"layout": Layout(
    title=" 80GB WITHOUT SWITCH 16 CORES",
xaxis=dict(
        title='Parallel Threads',
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
        title='Speed in Gbps',
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

