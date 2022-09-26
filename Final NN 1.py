# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 21:43:43 2020

@author: Hafidz MD
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Set Input Data
data = pd.read_excel (r'D:\Studies\NTUT Magister\Neural Network\Neural Network Final Project.xlsx', sheet_name = 'Data') 
problem = pd.read_excel (r'D:\Studies\NTUT Magister\Neural Network\Neural Network Final Project.xlsx', sheet_name = 'Problem') 
dp = problem.iloc[0:1,0:1]
df = pd.DataFrame(data, columns= ['Data_X','Data_Y'])

#print(dp)

datax = pd.DataFrame(data, columns= ['Data_X'])
datay =  pd.DataFrame(data, columns= ['Data_Y'])

#Convert To Array
px = np.array (datax)
py = np.array (datay)

#print(np.shape(py))
#print(py[0])

'''
#Plotting The Data      
plt.xlabel('Time')
plt.ylabel('Data')
plt.title('Final Project NN')

plt.scatter (px,py,color  = 'blue')
'''
Y = len(py)

#First Layer
lw11 = np.random.rand(2,1)

n1 = [0] * Y
a1 = [0] * Y

for t in range (Y) :
      
   
    n1[t] = n1[t] + np.dot(lw11,px[t]) 
    a1[t] = a1[t] + np.tanh (n1[t])
  
#print(a1[74])
#print (np.shape (a1))


#Second Layer
lw21 = np.random.rand(3,2)
lw22 = np.random.rand(3,3)

n2  = [0] * Y
a21 = [0] * Y
a22 = [0] * Y
a2  = [0] * Y

for t in range (Y) :
    
    a21[t] = a21[t] + np.dot(lw21,a1[t])
    a22[t] = a22[t] + np.dot(lw22, a21[t]) 
    n2[t]  = n2[t]  + a21[t] + a22[t]
    a2[t]  = a2[t] + np.tanh(n2[t])

#print(a2[t])
#print (np.shape(a2))


#Third Layer
lw32 = np.random.rand(2,3)

n3 = [0] * Y
a3 = [0] * Y

for t in range (Y) :
    
    n3[t] = n3[t] + np.dot (lw32,a2[t])
    a3[t] = a3[t] +  np.tanh(n3[t])
    
#print (a3[t])
#print (np.shape(a3))


#Seventh Layer
lw72 = np.random.rand(2,3)

n7 = [0] * Y
a7 = [0] * Y

for t in range (Y) :
    
    n7[t] = n7[t] + np.dot (lw32,a2[t])
    a7[t] = a7[t] +  np.tanh(n7[t])
    
#print (a7[t])
#print (np.shape(a7))

#Fourth Layer
lw43 = np.random.rand (1,2)
lw44 = np.random.rand (1,1)
lw47 = np.random.rand (1,2)

a43 = [0] * Y
a44 = [0] * Y
a47 = [0] * Y
a4 = [0] * Y
n4  = [0] * Y
n4in = [0] *Y
a4in = [0] *Y

for t in range (Y) :
    
    a43[t] = a43[t] + np.dot(lw43,a3[t-1])
    a43[0] = a43[0] - a43[0]
    a47[t] = a47[t] + np.dot(lw47,a7[t])
    
    n4in[t] = n4in[t] + a43[t] + a47[t]
    a4in [t] = a4in[t] + np.tanh(n4in[t])
    
    a44[t] = a44[t] + np.dot(lw44,a4in[t-1])
    a44[0] = [0]
    
    n4[t] = n4[t] + a43[t] + a44[t] + a47[t]
    a4[t] = a4[t] +  np.tanh(n4[t])
    
#print(a4[t]) 
#print (np.shape(a44[74]))

#Fifth Layer
lw54 = np.random.rand (2,1)

n5 = [0] * Y
a5 = [0] * Y

for t in range (Y) :
    
    n5[t] = n5[t] + np.dot(lw54,a4[t])
    a5[t] = a5[t] +  np.tanh(n5[t])
   
    
#print (a5[t])
#print (np.shape(a5))

#Sixth Layer
lw62 = np.random.rand (4,3)
lw65 = np.random.rand (4,2)

a65 = [0] * Y
a62 = [0] * Y
a6 = [0] * Y
n6 = [0] * Y

for t in range (Y) :
    
    a65[t] = a65[t] + np.dot(lw65,a5[t]) + np.dot (lw65,a5[t-1])
    a65[0] = a65[0] + np.dot(lw65,a5[t]) + 0
    a62[t] = a62[t] + np.dot(lw62,a2[t])
    n6[t] =  n6[t] + a65[t] + a62[t]
    a6[t] = a6[t]  + np.tanh(n6[t])

#print (a6[t])
#print (np.shape(a6))

#Eighth Layer
lw87 = np.random.rand (3,2)

a8 = [0] * Y
n8 = [0] * Y

for t in range (Y) : 
    
    n8[t] = n8[t] + np.dot(lw87,a7[t])
    a8[t] = a8[t] + np.tanh(n8[t])

#print (a7[t])
#print (np.shape(a7[1]))

#Ninth Layer
lw94 = np.random.rand (2,1)
lw98 = np.random.rand (2,3)

a94 = [0] * Y
a98 = [0] * Y
a9 = [0] * Y
n9 = [0] * Y

for t in range (Y) :
    
    a94[t] = a94[t] + np.dot (lw94,a4[t])
    a98[t] = a98[t] + np.dot (lw98, a8[t-1])
    a98[0] = a98[0] - a98[0]
    n9[t] = n9[t] + a94[t] + a98[t]
    a9[t] = a9[t] + np.tanh(n9[t])
    
#print (a9[t])
#print (np.shape(a9[t]))

#Tenth Layer
lw106 = np.random.rand(1,4)
lw109 = np.random.rand (1,2)

a106 = [0] * Y
a109 = [0] * Y
a10  = [0] * Y
n10  = [0] * Y

for t in range (Y) :

    a106[t] = a106[t] + np.dot (lw106, a6[t])
    a109[t] = a109[t] + np.dot (lw109, a9[t])
    n10[t] = n10[t] + a106[t] + a109[t] 
    a10[t] = n10[t]    
  
#print (a10[t])   
#print (np.shape(a10))
#plt.scatter (a10,py, color = 'green')
#plt.scatter (px,py, color = 'blue')


#Error
e = [0] * Y
e2 = [0] * Y

for t in range (Y) :
    
    e[t] = e[t] + (((py[t]) - a10[t]))
 

#print (e[1])
#print (np.shape(e))
plt.scatter (px,e, color = 'green')
plt.scatter (px,py, color = 'blue')


#Backpropagation
#Sensitivity









