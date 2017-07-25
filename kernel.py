import numpy as np
from cvxopt import solvers
from cvxopt import matrix
xpoint = []
ypoint = []
dataq = []
f = open("nonlinsep.txt")
for line in f.readlines():
    linedata = (line.strip()).split(",")
    xpoint.append([float(linedata[i]) for i in range(0,2)])
    ypoint.append([float(linedata[2])])
xpoints = []
for item in xpoint:
    xpoints.append([1,item[0]**2,item[1]**2,(2**0.5)*item[0],(2**0.5)*item[1],(2**0.5)*item[0]*item[1]])


for i in range(0,len(xpoints)):
    for j in range(0,len(ypoint)):
        dataq.append(ypoint[i][0]*ypoint[j][0]*(xpoints[i][0]*xpoints[j][0] + xpoints[i][1]*xpoints[j][1] + xpoints[i][2]*xpoints[j][2] + xpoints[i][3]*xpoints[j][3] + xpoints[i][4]*xpoints[j][4] + xpoints[i][5]*xpoints[j][5]))

p = []
g = []
for i in range(0,len(xpoints)):
    p.append(-1)
    g.append(-1)

q = matrix(dataq, (len(xpoints),len(xpoints)),"d") #100*100
p = matrix(p, tc="d") #100*1
G = matrix(np.diag(g),tc="d") #100*100

h = matrix(np.zeros((len(xpoints),1)),tc="d") #100*1
A = matrix(ypoint,(1,len(xpoints)),tc="d") #1*100
b = matrix(0.0) #1*1

sol = solvers.qp(q,p,G,h,A,b)
sol = list(sol['x'])
solist = []
index = []

for i in range(0,len(sol)):
    if sol[i] >= 1e-06:
        solist.append(sol[i])
        index.append(i)
    else:
        solist.append(0)

w = sum(np.multiply(np.multiply(np.matrix(solist).reshape(len(xpoints),1),np.matrix(ypoint)), np.matrix(xpoints)))

b = 1.0/ypoint[index[0]][0] - np.matrix(xpoints)[index[0]] * w.T

print "w = ", w
print "b = ", b
print sol


