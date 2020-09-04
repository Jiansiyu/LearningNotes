'''
 CS 4501 Machine Learning for NLP
 Homework 1, Question 1
 author : Siyu Jian
          sj9va
'''

import torch

if __name__ == '__main__':

    matrix=([list([0.1,0.3,0.7,0.4,0.2]),
           list([0.8,1.0,0.6,0.1,0.9]),
           ])
    x=([1,0,2,1,1])
    tensorM=torch.FloatTensor(matrix)
    tensorX=torch.FloatTensor(x)
    result=torch.mv(tensorM,tensorX)
    print(result)