import numpy as np
import time
from tkinter import *
from ttkbootstrap import *
from tkinter import ttk, messagebox

class mainWindow:
     # Allow The User To Select The Sorts. 
     sort = {'insertion': False, 'selection': False, 'quick': False,
               'merge': False, 'bubble': False}

     def __init__(user, mainRoot, displayTitle) -> None:
          user.mainRoot = mainRoot
          user.mainRoot.resizable(width=False, height=False)
          user.mainRoot.title(displayTitle)
          Label(user.mainRoot, text='Cam\'s Sorting Algorithm Visualizer').grid(
               row=0, columnspan=6, pady=10, padx=10)
          #  User Button Selections
          user.bs = ttk.Button(user.mainRoot, text='Bubble Sort', style='info.TButton', padding=7, width=16,
                              command=user.bubble)
          user.bs.grid(column=0, row=1, padx=5, pady=5)
          user.Is = ttk.Button(user.mainRoot, text='Insertion Sort', style='info.TButton', padding=7, width=16,
                              command=user.insertion)
          user.Is.grid(column=1, row=1, padx=5, pady=5)
          user.ss = ttk.Button(user.mainRoot, text='Selection Sort', style='info.TButton', padding=7, width=16,
                              command=user.selection)
          user.ss.grid(column=2, row=1, padx=5, pady=5)
          user.ms = ttk.Button(user.mainRoot, text='Merge Sort', style='info.TButton', padding=7, width=16,
                              command=user.merge)
          user.ms.grid(column=3, row=1, padx=5, pady=5)         
          user.qs = ttk.Button(user.mainRoot, text='Quick Sort', style='info.TButton', padding=7, width=16,
                              command=user.quick)
          user.qs.grid(column=4, row=1, padx=5, pady=5)          
          user.start = ttk.Button(user.mainRoot, text='Start Sort', padding=7, width=16,
                              command=user.start)
          user.start.grid(column=5, row=2, padx=5, pady=5)

          ttk.Label(user.mainRoot, text='Speed & Array Size:').grid(row=2,column=0 ,padx=5, pady=5)
          user.arraysize=ttk.Scale(user.mainRoot,from_=6,to=120,length=380,style='success.Horizontal.TScale',value=10,
               command=lambda x:user.slide_function())
          user.arraysize.grid(row=2,column=1,columnspan=3)
          
          ttk.Button(user.mainRoot, text='Shuffle', style='info.Outline.TButton', padding=7, width=16,
                                   command=user.shuffle).grid(column=5, row=1, padx=6, pady=6)
          ttk.Button(user.mainRoot, text='Exit', style='danger.Outline.TButton', padding=7, width=16,
                                   command=user.mainRoot.destroy).grid(column=5, row=3, padx=6, pady=6)
          # Program Canvas
          user.Canvas=Canvas(user.mainRoot, width=800-5, height=400,highlightbackground="blue",highlightthickness=2,
               bg='black')
          user.Canvas.grid(row=4, padx=5, pady=10, columnspan=6)

          #  User Button Selections
          user.X = 10
          user.selectedSpeed = 0.2
          user.Colors=['dodgerblue' for c in range(user.X)]
          C = user.X
          user.info=np.linspace(5,400, C, dtype = np.uint16)
          np.random.shuffle(user.info)
          user.display(C, user.info, user.Colors)
        
     
     def display(user,C: int, h: list, colorRect: list):
          '''
          C = Number of Rectangles In Sort
          h = The Array Rectangle Heights
          colorRect = The Colours For The Array Of Each Rectangle'''
          user.Canvas.delete('all')
          displayWidth = (1520) / (3 * C - 1)
          displayGap = displayWidth / 2

          for j in range(C):
               user.Canvas.create_rectangle(7 + j * displayWidth + j * displayGap, 0, 7 + (j + 1) * displayWidth + j * displayGap, h[j],fill = colorRect[j])
          user.mainRoot.update_idletasks()

     def slide_function(select):
          select.X = int(select.arraysize.get())
          select.info = np.linspace(5,405,select.X,dtype = np.uint16)
          select.selectedSpeed = 5 / select.arraysize.get()
          select.Colors = ['dodgerblue' for _ in range(select.X)]
          select.shuffle()
          
     def shuffle(select):
          select.Canvas.delete('all')
          select.info = np.linspace(5,405,select.X,dtype = np.uint16)
          np.random.shuffle(select.info)
          select.display(select.X,select.info,select.Colors)


     # Button Functions For Each Sorting Algorithms
     #Bubble 
     def bubble(select):
          if select.sort['bubble'] is False:
               select.sort['bubble'] = True
               select.bs.config(style ='success.TButton')
               for c in select.sort:
                    if c != 'bubble':
                         select.sort[c] = False
               select.qs.config(style = 'info.TButton')               
               select.ms.config(style = 'info.TButton')
               select.ss.config(style = 'info.TButton')
               select.Is.config(style = 'info.TButton')
          else:
               select.sort['bubble'] = False
               select.bs.config(style = 'info.TButton')
     #Merge 
     def merge(select):
          if select.sort['merge'] is False:
               select.sort['merge'] = True
               select.ms.config(style='success.TButton')
               for a in select.sort:
                    if a != 'merge':
                         select.sort[a] = False
               select.qs.config(style = 'info.TButton')               
               select.bs.config(style = 'info.TButton')
               select.ss.config(style = 'info.TButton')
               select.Is.config(style = 'info.TButton')
          else:
               select.sort['merge'] = False
               select.ms.config(style='info.TButton')
     #Selection
     def selection(select):
          if select.sort['selection'] is False:
               select.sort['selection'] = True
               select.ss.config(style = 'success.TButton')
               for d in select.sort:
                    if d != 'selection':
                         select.sort[d] = False
               select.qs.config(style = 'info.TButton')               
               select.bs.config(style = 'info.TButton')
               select.ms.config(style = 'info.TButton')
               select.Is.config(style = 'info.TButton')
          else:
               select.sort['selection'] = False
               select.ss.config(style = 'info.TButton')

     def quick(select):
          if select.sort['quick'] is False:
               select.sort['quick'] = True
               select.qs.config(style='success.TButton')
               for b in select.sort:
                    if b != 'quick':
                         select.sort[b] = False
               select.ms.config(style = 'info.TButton')               
               select.bs.config(style = 'info.TButton')
               select.ss.config(style = 'info.TButton')
               select.Is.config(style = 'info.TButton')
          else:
               select.sort['quick'] = False
               select.qs.config(style = 'info.TButton')
     #Insertion
     def insertion(select):
          if select.sort['insertion'] is False:
               select.sort['insertion'] = True
               select.Is.config(style='success.TButton')
               for e in select.sort:
                    if e != 'insertion':
                         select.sort[e] = False
               select.qs.config(style = 'info.TButton')               
               select.bs.config(style = 'info.TButton')
               select.ss.config(style = 'info.TButton')
               select.ms.config(style = 'info.TButton')
          else:
               select.sort['insertion'] = False
               select.Is.config(style='info.TButton')
 
     # Sorting Algorithms
     def start(select):
          # Bubble Sort Outlined
          if select.sort['bubble'] is True:
               for c in range(select.X - 1):
                    for y in range(select.X - 1 - c):
                         select.display(select.X,select.info,['purple' if a == y or a == y + 1 else 'green' if a > select.X - 1 - c else 'dodgerblue' for a in range(select.X)])
                         time.sleep(select.selectedSpeed)
                         if select.info[y] > select.info[y+1]:
                              select.display(select.X,select.info,['red' if a == y or a == y + 1 else 'green' if a > select.X - 1 - c else 'dodgerblue' for a in range(select.X)])
                              time.sleep(select.selectedSpeed)
                              select.info[y],select.info[y + 1] = select.info[y + 1],select.info[y]
                              select.display(select.X,select.info,['lime' if a == y or a == y + 1 else 'green' if a>select.X - 1 - c else 'dodgerblue' for a in range(select.X)])
                              time.sleep(select.selectedSpeed)
               select.display(select.X,select.info,['lime' for _ in range(select.X)])
          # Insertion Sort Outlined
          elif select.sort['insertion'] is True:
               for y in range(1,len(select.info)):
                    c = y - 1
                    foundKey = select.info[y]
                    select.display(select.X,select.info,['purple' if a == c or a == c + 1 else 'green' if a <= y else'dodgerblue' for a in range(select.X)])
                    time.sleep(select.selectedSpeed)
                    while c >= 0 and select.info[c] > foundKey:
                         select.info[c + 1] = select.info[c]
                         select.display(select.X,select.info,['yellow' if a == c else 'green' if a <= y else'dodgerblue' for a in range(select.X)])
                         time.sleep(select.selectedSpeed)
                         c-=1
                    select.info[c + 1] = foundKey
               select.display(select.X,select.info,['lime' for _ in range(select.X)])
          # Selection Sort Outlined
          elif select.sort['selection'] is True:
               for c in range(len(select.info) - 1):
                    indexMin = c 
                    # loop to find the minimum element and its index
                    for y in range(c + 1,len(select.info)):
                         select.display(select.X,select.info,['yellow' if a == indexMin or a == c else 'green' if a <= c else 'dodgerblue' for a in range(select.X)])
                         time.sleep(select.selectedSpeed)
                         if select.info[indexMin] > select.info[y]:
                              select.display(select.X,select.info,['red' if a == indexMin or a == y else 'green' if a <= c else 'dodgerblue' for a in range(select.X)])
                              time.sleep(select.selectedSpeed)
                              indexMin = y
                    if indexMin != c:
                         select.info[c], select.info[indexMin] = select.info[indexMin],select.info[c]
                         select.display(select.X,select.info,['lime' if a == indexMin or a == c else 'green' if a <= c else 'dodgerblue' for a in range(select.X)])
                         time.sleep(select.selectedSpeed)
               select.display(select.X,select.info,['lime' for _ in range(select.X)])
          # Merge Sort Outlined
          elif select.sort['merge'] is True:
               select.mergesort(select.info,0,select.X - 1)
               select.display(select.X,select.info,['lime' for _ in range(select.X)])
          elif select.sort['quick'] is True:
               select.quicksort(select.info,0,select.X - 1)
               select.display(select.X,select.info,['lime' for _ in range(select.X)])
          else:
               # No Selected Algorithm Message
               messagebox.showerror("Algorithm Visualizer", "Sorry! You Need To Select A Sorting Algorithm :)")
               
     # Merge Sort Algorithm
     def mergesort(select, array, frontIndex, lastIndex):
          if frontIndex < lastIndex:
               midpoint = (frontIndex + lastIndex) // 2
               select.mergesort(array,frontIndex,midpoint)
               select.mergesort(array,midpoint + 1,lastIndex)
               select.display(select.X,select.info,['dodgerblue' for _ in range(select.X)])
               position = midpoint + 1
               if array[midpoint] <= array[midpoint + 1]:
                    return 
               while frontIndex <= midpoint and position <= lastIndex:
                    select.display(select.X,select.info,['yellow' if x == frontIndex or x == position else 'dodgerblue' for x in range(select.X)])
                    time.sleep(select.selectedSpeed)
                    if array[frontIndex] <= array[position]:
                         select.display(select.X,select.info,['lime' if x == frontIndex or x == position else 'dodgerblue' for x in range(select.X)])
                         time.sleep(select.selectedSpeed)
                         frontIndex+=1
                    else:
                         select.display(select.X,select.info,['red' if x == frontIndex or x == position else 'dodgerblue' for x in range(select.X)])
                         time.sleep(select.selectedSpeed)
                         temp=array[position]
                         index = position
                         while index != frontIndex:
                              array[index] = array[index-1]
                              index-=1
                         array[frontIndex] = temp
                         select.display(select.X,select.info,['lime' if x == frontIndex or x == position else 'dodgerblue' for x in range(select.X)])
                         time.sleep(select.selectedSpeed)
                         frontIndex+=1
                         midpoint+=1
                         position+=1
               # Merge Sort Display
               select.display(select.X,select.info,['dodgerblue' for _ in range(select.X)])
               time.sleep(select.selectedSpeed)
     
     # Quick Sort Algorithm
     def partition(selectSelf, array, frontIndex,backIndex):
          pivot = array[frontIndex]
          pivotIndex = frontIndex
          left = frontIndex
          while frontIndex < backIndex:
               while frontIndex < len(array) and array[frontIndex] <= pivot:
                    frontIndex+=1
                    selectSelf.display(selectSelf.X,selectSelf.info,['purple' if x == pivotIndex else 'yellow' if x == frontIndex else "dodgerblue" for x in range(selectSelf.X)])
                    time.sleep(selectSelf.selectedSpeed)
               while array[backIndex] > pivot:
                    backIndex-=1
               if frontIndex < backIndex:
                    selectSelf.display(selectSelf.X,selectSelf.info,['red' if x == frontIndex or x == backIndex else "dodgerblue" for x in range(selectSelf.X)])
                    time.sleep(selectSelf.selectedSpeed)
                    array[frontIndex], array[backIndex] = array[backIndex], array[frontIndex]
                    selectSelf.display(selectSelf.X,selectSelf.info,['lime' if x == frontIndex or x == backIndex else "dodgerblue" for x in range(selectSelf.X)])
                    time.sleep(selectSelf.selectedSpeed)
          array[backIndex], array[left] = array[left], array[backIndex]
          return backIndex

     def quicksort(select, array, frontIndex, backIndex):
          if frontIndex < backIndex:
               pos = select.partition(array, frontIndex, backIndex)
               select.quicksort(array, frontIndex, pos - 1)
               select.quicksort(array, pos + 1, backIndex)
     #Main
if __name__ == '__main__':
     win = Style(theme='darkly').master
     obj = mainWindow(win, 'Sorting Algorithm Visualizer')
     win.mainloop()