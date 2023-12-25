# -*- coding: utf-8 -*-
"""21301436_Mehedi Hasan Shahed_13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IU8Is8wBH2Wa7TTDp0KLrvu65CM9IKaR
"""

#Mehedi Hasan Shahed
#21301436
#Section:13

from queue import Queue
q = Queue()
inp = open('/content/input1.txt','r')
out = open('/content/output1.txt','w')

read = inp.readline()
stg = read.strip()
temp = [int(i) for i in stg.split(' ')]
adj_lst = {}

for i in range(0,temp[0]):
  adj_lst[i] = []

for i in range(temp[1]):
  temp_1 = inp.readline()
  stg = temp_1.strip()
  lst = [int(j) for j in stg.split(' ')]
  x = lst[0]
  y = lst[1]
  adj_lst[x].append(y)
  adj_lst[y].append(x)

key = temp[2]
visited = {}
parent = {}
trav_out = []

for i in adj_lst:
  visited[i] = False
  parent[i] = None

source = key
visited[source] = True
q.put(source)

while q.empty() == False:
  u = q.get(0)
  trav_out.append(u)
  for i in adj_lst[u]:
    if not visited[i]:
      visited[i] = True
      parent[i] = u
      q.put(i)

for i in range(0,temp[0]):
  temp_2 = i
  path = []
  while temp_2 is not None:
    path.append(temp_2)
    temp_2 = parent[temp_2]

  if len(path) == 1 and i != key:
    path = [-1]
  path = path[::-1]
  for i in path:
    out.write(str(i)+' ')
  out.write('\n')

out.close()
