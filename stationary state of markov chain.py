#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np

#transition_matrix = np.array([[0.2,0.6,0.2],[0.1,0.6,0.3],[0.2,0.7,0.1]])
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
transition_matrix = []
print("Enter the entries in a single line (separated by space): ")
entries = list(map(float, input().split()))
transition_matrix = np.array(entries).reshape(R, C)
print("transition matrix :")
print(transition_matrix)

sumMatrix = np.sum(transition_matrix,axis=1, dtype='float')
for i in range (0,C-1):
    if sumMatrix[i] != [1]:
        print("Somewhere, something went wrong. Transition matrix, perhaps?")
        quit()
    
#Since the sum of each row is 1, transition matrix is row stochastic
eigenvals, eigenvects = np.linalg.eig(transition_matrix.T)

#Find the indexes of the eigenvalues that are close to one
close_to_1_idx = np.isclose(eigenvals,1)
target_eigenvect = eigenvects[:,close_to_1_idx]
target_eigenvect = target_eigenvect[:,0]

stationary_distrib = target_eigenvect / sum(target_eigenvect) 

print("stationary state: ")
print(stationary_distrib)


# # 

# In[ ]:




