# Before Going through code firstly please read the question 
'''The Manhattan Distance between two points (a, b) and (c, d) is given by |a − c| +
|b − d|, where |u − v| refers to the absolute value of (u − v). For example, the
Manhattan Distance between the points (2, 3) and (−1, 7) is |2 − (−1)| + |3 − 7| =
|3| + | − 4| = 3 + 4 = 7.
Given an integer S, your task is to find the number of points (x, y), where both x
and y are integers, such that the Manhattan Distance between (x, y) and (0, 0) is
at most S.
For example, suppose S = 1. The only point whose Manhattan Distance from
(0, 0) is exactly 0 is (0, 0). The set of points whose Manhattan Distance from
(0, 0) is exactly 1 is {1, 0),(0, 1),(−1, 0),(0, −1)}. Thus, there are 5 points whose
Manhattan Distance from (0, 0) is at most 1, and so the answer for S = 1 is 5.
Find the number of points whose Manhattan Distance from (0, 0) is at most S for
the following values of S:
(a) S = 4
(b) S = 10
(c) S = 23

solution given below
'''

lst1 = []
n = int(input('Enter a number '))
for  i in range(0,n+1):
    for j in range(0,n+1):
        m = i +j
        if m <= n:
            a = i,j
            lst1.append(list(a))
            if i != 0 and j == 0:
                c = -i,j

                lst1.append(list(c))
            elif i == 0 and j !=0:
                d = i,-j

                lst1.append(list(d))
            elif i != 0 and j != 0 :
                e = -i,-j
                f = -i,j
                g = i,-j
                lst1.append(list(e))
                lst1.append(list(f)) 
                lst1.append(list(g))      
print(len(lst1))
