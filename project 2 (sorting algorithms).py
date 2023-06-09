# -*- coding: utf-8 -*-
"""DATA_311 A#2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fgc5UInbWtCRbUR2AYVFk3LVDgWrOL_7


"""
#The goal of the assignment was to use differnt sorting algorithms in order to sort given values, display it, measure how much time it takes, and save sorted data in the text file



import numpy as np
import sys
import random
import numpy as np
import time

sys.setrecursionlimit(1000000)
sys.getrecursionlimit()


def insert_sort (a):
  start = time.time()
  for i in range(1, len(a)):
    val, pos = a[i], i
    while pos > 0 and a[pos-1]>val:
      a[pos] = a[pos-1]
      pos = pos-1
    a[pos]=val
    end = time.time()
    time_measure = end - start
  return a, time_measure


def bubble_sort(a):
  start = time.time()
  while(True):
    swap_detected = False
    for i in range (0, len(a)-1):
      if a[i] > a[i+1]:
        a[i], a[i+1] = a[i+1], a[i]
        swap_detected = True
    end = time.time()
    time_measure = end - start
    if not swap_detected:
      break
    
  return a, time_measure


def merge_sort(a):
  start = time.time()
  if len(a) > 1:
    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]

    merge_sort(left)
    merge_sort(right)
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        a[k] = left[i]
        i = i+1
      else:
        a[k] = right[j]
        j = j+1
      k = k+1
    while i < len(left):
      a[k] = left[i]
      i = i+1
      k = k+1
    while j < len(right):
      a[k] = right[j]
      j = j+1
      k = k+1
  end = time.time()
  time_measure = end - start
  return a, time_measure


def quicksortHelper(a, lo, hi):
  if lo >= hi: return
  p = partition(a, lo, hi)
  quicksortHelper(a, lo, p)
  quicksortHelper(a, p + 1, hi)

def partition(a, lo, hi):
 pivot = a[lo] 
 i, j = lo, hi
 while True:
  while a[i] < pivot: i = i + 1
  while a[j] > pivot: j = j - 1
  if i >= j: return j
  a[i], a[j] = a[j], a[i]
  i, j = i + 1, j - 1

def quick_sort(a):
  start = time.time()
  quicksortHelper(a, 0, len(a)-1)
  end = time.time()
  time_measure = end - start
  return a, time_measure



def sortArray(size, order, algorithm, outputfile):
  a = []
  if (size==10 or size==100 or size==1000 or size==10000 or size==100000) and (order == 'ascending' or order == 'descending' or order == 'random') and (algorithm =='Insertion Sort' or algorithm == 'Bubble Sort' or algorithm =='Merge Sort' or algorithm == 'Quick Sort'):
   if order == 'ascending':
     for i in range(size):
      a.append(random.randint(0,size))
      a = sorted(a)
   elif order == 'descending':
     for i in range(size):
      a.append(random.randint(0,size))
      a = sorted(a, reverse=True)
   elif order == 'random':
     for i in range(size):
      a.append(random.randint(0, size))
  
   if algorithm == 'Insertion Sort':
    output = insert_sort(a)
   elif algorithm == 'Bubble Sort':
    output = bubble_sort(a)
   elif algorithm =='Merge Sort':
    output = merge_sort(a)
   elif algorithm == 'Quick Sort':
     output = quick_sort(a)

  
   outputfile_ = open(outputfile, 'w')
   for i in output:
     outputfile_.write("%s\n" % i)
   outputfile_.close()
  else:
    sys.exit('Invalid input, please make sure that:  \n 1) size equals either 10, 100, 1000, 10000, 100000 \n 2) The order is either ascending, descending or random \n 3) The algorithm used is either Insertion Sort, Bubble Sort, Merge Sort or Quick Sort ')
                                                 
    
  return output

#Here is an example of input, please remember to put the r + pathway of the .txt file as the outputfile
print(sortArray(10, 'ascending', 'Quick Sort', r"C:\Users\cypri\OneDrive\Desktop\testing.txt"))

