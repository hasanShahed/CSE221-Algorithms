# -*- coding: utf-8 -*-
"""cse221_lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xOROa90hqnVVtNEnkwIBQ87UGTzSyrD9
"""

#Task2_1
inp = open('/content/inp2_1.txt','r')
out = open('/content/out2_1.txt','w')

read = inp.readlines()
a = int(read[0].replace('\n',''))
b = int(read[2].replace('\n',''))
arr_1 = read[1].split(' ')
arr_1[a-1] = arr_1[a-1].replace('\n','')
arr_2 = read[3].split(' ')
arr_2[b-1] = arr_2[b-1].replace('\n','')
arr = []
for i in arr_1:
  arr.append(int(i))
for i in arr_2:
  arr.append(int(i))
arr.sort()
for i in arr:
  temp = str(i)+' '
  out.write(temp)
inp.close()
out.close()

#Task2_2
inp = open('/content/inp2_2.txt','r')
out = open('/content/out2_2.txt','w')

read = inp.readlines()
a = int(read[0].replace('\n',''))
b = int(read[2].replace('\n',''))
arr_1 = read[1].split(' ')
arr_1[a-1] = arr_1[a-1].replace('\n','')
arr_2 = read[3].split(' ')
arr_2[b-1] = arr_2[b-1].replace('\n','')
arr = []
p1 = 0
p2 = 0
while p1 != a and p2 != b:
  if arr_1[p1]<arr_2[p2]:
    arr.append(arr_1[p1])
    p1 += 1
  elif arr_1[p1] == arr_2[p2]:
    arr.append(arr_1[p1])
    arr.append(arr_2[p2])
    p1 += 1
    p2 += 1
  else:
    arr.append(arr_2[p2])
    p2 += 1
while p1 < a:
  arr.append(arr_1[p1])
  p1 += 1
while p2 < b:
  arr.append(arr_2[p2])
  p2 += 1
for i in arr:
  temp = str(i)+' '
  out.write(temp)

inp.close()
out.close()