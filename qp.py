import numpy as np
from cvxopt import solvers
from cvxopt import matrix
xpoint = []
ypoint = []
dataq = []
f = open("linsep.txt")
for line in f.readlines():
    linedata = (line.strip()).split(",")
    xpoint.append([float(linedata[i]) for i in range(0,2)])
    ypoint.append([float(linedata[2])])

for i in range(0,len(xpoint)):
    for j in range(0,len(ypoint)):
        dataq.append(ypoint[i][0]*ypoint[j][0]*(xpoint[i][0]*xpoint[j][0] + xpoint[i][1]*xpoint[j][1]))

p = []
g = []
for i in range(0,len(xpoint)):
    p.append(-1)
    g.append(-1)

q = matrix(dataq, (len(xpoint),len(xpoint)),"d") #100*100
p = matrix(p, tc="d") #100*1
G = matrix(np.diag(g),tc="d") #100*100

h = matrix(np.zeros((len(xpoint),1)),tc="d") #100*1
A = matrix(ypoint,(1,len(xpoint)),tc="d") #1*100
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

w = sum(np.multiply(np.multiply(np.matrix(solist).reshape(len(xpoint),1),np.matrix(ypoint)), np.matrix(xpoint)))

b = 1.0/ypoint[index[0]][0] - np.matrix(xpoint)[index[0]] * w.T

print "w = ", w
print "b = ", b







