# Badminton Analysis

This project focuses on displaying useful stats like player dominance and no. of stokes in each score of a badminton singles match

## Assumptions

As a example, a dummy data set is used for the points table and no. of strokes table which is assumed that the machine learning algorithm implemented in reaserch paper titled "Towards Structured Analysis of Broadcast Badminton Videos" would fetch and return as csv format.

## Prerequisites

All the flask applications are made in Python 3.7 and to use each API install requirements.txt. The repository has the dockerfile and by building that docker and running it

```
$ docker build -t badminton_analysis:latest .
```
### Run of Application

On running the docker image created we launch a flask application and to access the web pages we can open a browser and open the following URL:-
```
localhost:5000/home
```
This URL will launch the home page and thus we can access the application for different stataistics.

### Stataistics available in application

As mentioned earlier, right now application is using a dummy data set created mannually, by which the application is able to calculate set-wise analysis and result analysis.

#### Set-wise analysis
The UI of the application is kept simple and on selecting set-wise analysis you are given the winner of each set, found based on points csv file and also the dominace and no. of strokes graph, giving you a breif analysis about the game and the play.

#### Result analysis
It is still in development mode but currently it just shows the winner of the game.

## Reference and inspiration
* **https://researchweb.iiit.ac.in/~anurag.ghosh/static/structured-analysis-broadcast.pdf**

## Author
* **Yeshwanth Kumar Maringanti** - (https://github.com/yeshwanthmaringanti)
