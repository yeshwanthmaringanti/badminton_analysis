from flask import Flask, redirect, url_for, request,render_template
import pandas as pd
from matplotlib import pyplot as plt

app = Flask(__name__)
# to find dominance graph for a set and save result in static/images
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
    
# to find strokes graph for a set and save result in static/images
def strokes_graph(strokes,name):
    x=list(range(len(strokes)))
    y=list(strokes['strokes'])
    plt.plot(x,y)
    plt.xlabel('points')
    plt.ylabel('No. of strokes')
    plt.savefig(name)
    plt.close()
# calling function for setting both graphs 
def set_graphs(name):
    p='./sets/{}/{}.csv'.format(name,name)
    s='./sets/{}/{}_strokes.csv'.format(name,name)
    dg='./static/images/{}_dominance.png'.format(name)
    sg='./static/images/{}_strokes.png'.format(name)
    points=pd.read_csv(p)
    strokes=pd.read_csv(s)
    dominance_graph(points,dg)
    strokes_graph(strokes,sg)
# to find the result of set
def result_setwise(name):
    p='./sets/{}/{}.csv'.format(name,name)
    points=pd.read_csv(p)
    if points['player_1'].max()>points['player_2'].max():
        winner=1
    else:
        winner=2
    return winner
#to find the winner of game
def winner():
    s=['set1','set2','set3']
    win1=0
    win2=0
    for i in s:
        w=0
        try:
            w=result_setwise(i)
        except:
            continue
        if w==1:
            win1+=1
        elif w==2:
            win2+=1
    if win1>win2:
        return 1
    else:
        return 2
    
@app.route('/sets',methods = ['POST', 'GET'])
def sets():
   return  render_template('sets.html')

@app.route('/set_analysis/<name>',methods = ['POST', 'GET'])
def set_analysis(name):
   a=str(name)+'.html'
   try:
       set_graphs(name)
       win=result_setwise(name)
       return render_template(a,name=win)
   except:
       return render_template('no.html')
@app.route('/result',methods = ['POST', 'GET'])
def result():
    win=winner()
    return render_template('result.html',name=win)

@app.route('/match',methods = ['POST', 'GET'])
def match(): 
   return render_template('match.html')

@app.route('/home',methods = ['POST', 'GET'])
def home():
    return render_template('home.html')  

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
   
