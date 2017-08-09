# SVM
introduction and implementation of Support Vector Machine


Question:
You are given two data files - linsep.txt and nonlinsep.txt - each of which contains 100 2D points with classification labels +1 or -1. The first two columns in each file indicate the 2D coordinates of a point; and the third column indicates its classification label. The points in linsep.txt are linearly separable. The points in nonlinsep.txt are not linearly separable in the original space but are linearly separable in a z-space that uses a simple nonlinear transformation.
Part (a) [3.5 points]: Find the fattest margin line that separates the points in linsep.txt. Please solve the problem using a Quadratic Programming solver. Report the equation of the line of separation.
Part (b) [3.5 points]: Using a kernel function of your choice along with the same Quadratic Programming solver, find the equation of a curve that separates the points in nonlinsep.txt. Report the kernel function you use as well as the equation of the line of separation.


Answer:
Python
In Python implementation, for the linear separable, we first review the standard form of a quadratic programming function CVXOPT. We need to prepare our data for the definition:

We want to obtain x which is alpha in this case. P is the Q matrix which means  Q(i,j)=y(i)*y(j)*x(i)’*x(j). At the same time, the constraints in KKT condition need to be satisfied as listed above. Alpha is obtained by the following code:

from cvxopt import solvers 
sol = solvers.qp(P,q,G,h)

If you had A, b as well, you would call:

sol = solvers.qp(P,q,G,h,A,b)

We take most entries in alpha which is less than 10^-6 as 0’s while the indexes of remained entries greater than 0 should be append to a list. Points in those indexes are support vectors whose coordinates would help us calculate weights w with and constant b.

Hence, we have all the terms we need for the line equation:

w =  [[ 7.25005616 -3.86188932]]
b =  [[-0.10698729]]

So equation will be 7.2500561*x1 -3.86188932*x2 -0.10698729 = 0.

The difference between considering linear separable and nonlinearly separable is that we need to  change inner product of X vector in matrix Q with a function K. We choose Polynomial Kernel as kernel function:

It is the same process for getting alpha from quadratic programming function, so w and b for the equation is obtained.

w =  [[  8.64344226e-10   1.60702131e-01   1.58698040e-01  -9.47655776e-03 -3.85759106e-02  -1.10224094e-03]]
b =  [[-16.66005249]]



