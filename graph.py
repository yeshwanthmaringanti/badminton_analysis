import pandas as pd
from matplotlib import pyplot as plt
def dominance_graph(points,name):
    x=list(range(len(points)))
    y1=0
    y2=0
    p1=[0]
    p2=[0]
    count=1
    while count<len(points):
        first=points.iat[count,0]-points.iat[count-1,0]
        second=points.iat[count,1]-points.iat[count-1,1]
        if first==1:
            y1+=1
            y2-=1
        elif second==1:
            y2+=1
            y1-=1
        p1.append(y1)
        p2.append(y2)
        count+=1
    plt.plot(x,p1,'r',label='Player 1')
    plt.plot(x,p2,'b',label='Player 2')
    plt.xlabel('points')
    plt.ylabel('Dominance')
    plt.legend()
    plt.savefig(name)
    plt.close()
def strokes_graph(strokes,name):
    x=list(range(len(strokes)))
    y=list(strokes['strokes'])
    plt.plot(x,y)
    plt.xlabel('points')
    plt.ylabel('No. of strokes')
    plt.savefig(name)
    plt.close()
def set_graphs(name):
    p='./{}/{}.csv'.format(name,name)
    s='./{}/{}_strokes.csv'.format(name,name)
    dg='./static/images/{}_dominance.png'.format(name)
    sg='./static/images/{}_strokes.png'.format(name)
    points=pd.read_csv(p)
    strokes=pd.read_csv(s)
    dominance_graph(points,dg)
    strokes_graph(strokes,sg)
