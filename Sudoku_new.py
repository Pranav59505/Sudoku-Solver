import numpy as np
import copy
sudoku = []
Answer = [[[1, 2, 3, 4, 5, 6, 7, 8, 9] for _ in range(9)] for p in range(9)]
#"""
for i in range(9):
   x = map(int,input().split())
   sudoku.append(list(x))
sudoku=np.array(sudoku).reshape(9,9)

for a in range(9):
    for b in range(9):
        if sudoku[a][b]!=0:
            Answer[a][b]=int(sudoku[a][b])
#"""
def pop(lis, x):
    if isinstance(lis, list) and x in lis:
        lis.remove(x)

def subset(x,y):#Checking whether x is subset of y
    if isinstance(x,list) and isinstance(y,list):
        for j in x:
            if j not in y:
                return False
        return True
def union(list1,list2):
    # Initialize the union list with the first list
    union_list = list1[:]
    # Add elements from the second list if they are not already in the union list
    for item in list2:
        if item not in union_list:
            union_list.append(item)
    return union_list

def action(A,i,j): #removing the integer form other parts and if one is left then assigning that value
    x=A[i][j]
    if isinstance(x,int):
        for m in range(9):
            if m!=i:
                pop(A[m][j],x)
            if isinstance(A[m][j],list) and len(A[m][j])==1:
                A[m][j]=A[m][j][0]
        for n in range(9):
            if n!=j:
                pop(A[i][n],x)
            if isinstance(A[i][n],list) and len(A[i][n])==1:
                A[i][n]=A[i][n][0]
    s=i%3
    t=j%3
    for m in {-s,1-s,2-s}:
        for n in {-t,1-t,2-t}:
            if m!=0 or n!=0:
                pop(A[i+m][j+n],x)

def count(Answer,i,j,t): # if one number is there put that value
    Y = []
    for o in Answer[i]:
        if isinstance(o, list) and t in o and t not in Answer[i]:
            Y.append([i, Answer[i].index(o)])
    if len(Y) == 1:
        Answer[Y[0][0]][Y[0][1]] = t
    Y.clear()
    m = 0
    for o in range(9):
        if Answer[i][o] == t:
            m = m + 1
        if isinstance(Answer[i][o], list) and t in Answer[i][o]:
            Y.append([o, j])
    if len(Y) == 1 and m == 0:
        Answer[Y[0][0]][Y[0][1]] = t
    Y.clear()
   # """
    q=0
    s = i % 3
    p = j % 3
    for m in {-s, 1 - s, 2 - s}:
        for n in {-p, 1 - p, 2 - p}:
            if isinstance(t,int):
                if Answer[i+m][j+n] == t:
                    q = q + 1
            else:
                if len(t)==1 and Answer[i+m][j+n]==t[0]:
                    q=q+1
                if isinstance(Answer[i+m][j+n], list) and t in Answer[i+m][j+n]:
                    Y.append([i+m, j+n])
    if len(Y) == 1 and q == 0:
        Answer[Y[0][0]][Y[0][1]] = t
    Y.clear()
#"""
def skill(A, i, j, t):
    x = []
    Y = copy.deepcopy(A[i])
    for m in range(9):
        if isinstance(A[i][m], list) and subset(A[i][m], t) == True:
            x.append(m)
    if isinstance(t,list) and len(x) == len(t):
        for n in range(9):
            if n not in x and isinstance(A[i][n], list):
                for g in A[i][n]:
                    if g in t:
                        Y[n].remove(g)
    A[i] = Y.copy()
    x.clear()
    for m in range(9):
        if isinstance(A[m][j],list) and subset(A[m][j],t)==True:
            x.append(m)
    if isinstance(t,list) and len(x) == len(t):
        for n in range(9):
            if n not in x and isinstance(A[n][j], list):
                for g in t:
                    if g in A[n][j]:
                        A[n][j].remove(g)
    x.clear()
    s = i % 3
    p = j % 3
    for m in {-s, 1 - s, 2 - s}:
        for n in {-p, 1 - p, 2 - p}:
            if isinstance(A[i+m][j+n], list) and subset(A[i+m][j+n], t) == True:
                x.append([m,n])
    if isinstance(t, list) and len(x) == len(t):
        for q in {-s, 1 - s, 2 - s}:
            for u in {-p, 1 - p, 2 - p}:
                if [q,u] not in x and isinstance(A[i+q][j+u], list):
                    for g in t:
                        if g in A[i+q][j+u]:
                            A[i+q][j+u].remove(g)

def upskill(A,i,j,t):
    if isinstance(t, list):
        for p in A[i]:
            if isinstance(p,list):
                skill(A,i,j,union(p,t))
        for o in range(9):
            if isinstance(A[o][j],list):
               # print(union(A[o][j],t))
                skill(A,i,j,union(A[o][j],t))
"""
Answer[0][1]=[2,3]
Answer[0][2]=[2,5]
Answer[0][3]=[3,5]
Answer[0][0]=[2,3]
Answer[1][0]=[2,5]
Answer[2][0]=[3,5]
Answer[2][1]=[2,3,4,5,6]
#Answer[3][0]=4

action(Answer,3,0)
skill(Answer,0,1,Answer[0][1])

"""
for _ in range(pow(2,3)):
    for i in range(9):
        for j in range(9):
            action(Answer,i,j)
            for t in range(1,10):
                count(Answer,i,j,t)
            action(Answer,i,j)
            upskill(Answer,i,j,Answer[i][j])
            action(Answer,i,j)
            upskill(Answer,i,j,Answer[i][j])
#"""
for rows in Answer:
    print(rows)

