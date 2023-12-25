# -*- coding: utf-8 -*-
"""cse221_Lab3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ETS5FRPYAveXdGAKqwZsOfjQvDMD3_qW
"""

#Task 5
inp = open("/content/input5.txt","r")
out = open("/content/output5.txt","w")

read = inp.readlines()

def partition(arr,low,high):
  pivot = arr[high]
  i = low - 1
  for j in range (low, high):
    if arr[j] <= pivot:
      i = i + 1
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
  temp_1 = arr[i+1]
  arr[i+1] = arr[high]
  arr[high] = temp_1
  return i + 1

def quick_Sort(arr, low, high):
  if low < high:
    pi = partition(arr, low, high)
    quick_Sort(arr, low, pi-1)
    quick_Sort(arr, pi+1, high)
  return arr

stg = read[1].strip("\n")
list_1 = [int(i) for i in stg.split(" ")]

var = quick_Sort(list_1, 0, len(list_1)-1)

for i in range(int(read[0])):
  out.write(str(var[i])+" ")

inp.close()
out.close()

