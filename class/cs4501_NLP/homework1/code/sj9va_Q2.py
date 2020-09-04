'''
 CS 4501 Machine Learning for NLP
 Homework 1, Question 2
 author : Siyu Jian
          sj9va
'''

import torch
torch.set_printoptions(precision=20)
if __name__ == '__main__':
    initialM=torch.empty(4,4)
    torch.nn.init.orthogonal_(initialM,gain=1)
    transposM=initialM.t()
    print(initialM)
    print(transposM)
    print(initialM.mm(initialM.t()))
