# Algorithm for all possible index-distanced arrangements 
An algorithm, that prints out for any number *n*, the arrangements of *n* girls and *n* boys (in a line) such that between girl with index *k* and boy with index *k*, there are exactly *k* people. I call these arrangements index-equal distanced arrangements of an *(n,n)-tuple*. 

Such arrangement only exists if *n=4k+3* or *n=4k*. See my proof on that here: 
https://artofproblemsolving.com/community/u362975h3075710p27779770

This was inspired by the problem found on the link above. 

## The output
You can modify the code in the end to try out other numbers. As said so, solutions only exist for *n = 3* or *0* *(mod 4)*. 
![image](https://github.com/me9hanics/Every-Index-Equal-Distanced-Arrangement-Algorithm/assets/82604073/b1d71c46-151e-4ce3-afbd-d00329409d1f)

## Notes
Of course this is not a fast algorithm, recursion takes a long time.

However, since the number of ways to arrange these numbers is (2n)!/(2^n), I expect the number of feasible arrangements to be "factioral" too (even worse than exponential), therefore, even the fastest possible algorithm would take a long time just to find all solutions, since there are so many of them.
