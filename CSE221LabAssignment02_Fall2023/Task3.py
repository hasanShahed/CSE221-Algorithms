# -*- coding: utf-8 -*-
"""cse221_lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xOROa90hqnVVtNEnkwIBQ87UGTzSyrD9
"""

#Task3
def greedy(lis):
    grdy = []
    grdy.append(lis[0])
    end_time = lis[0][1]

    for end in lis:
        if end_time <= end[0]:
            end_time = end[1]
            grdy.append(end)


    out.write(str(len(grdy))+"\n")

    for i in grdy:
        out.write(str(i[0])+" "+str(i[1])+"\n")

inp = open('/content/inp3.txt','r')
out = open('/content/out3.txt','w')
read = inp.readlines()
stg = [i.strip("\n") for i in read]
lis = []
for i in stg[1:]:
    lis.append([int(j) for j in i.split(" ")])

time = int(read[0])
for i in range(time):
    for j in range(0, time-i-1):
        if lis[j][1] > lis[j+1][1]:
            temp = lis[j]
            lis[j] = lis[j+1]
            lis[j+1] = temp

        if lis[j][1] == lis[j+1][1]:
            if lis[j][0] > lis[j+1][0]:
                temp = lis[j]
                lis[j] = lis[j+1]
                lis[j+1] = temp
greedy(lis)
inp.close()
out.close()

