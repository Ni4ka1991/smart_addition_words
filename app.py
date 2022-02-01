#!/usr/bin/env python3

from services import *
from os import system
import torch


X = torch.tensor( X_, dtype = torch.float32 )
Y = torch.tensor( Y_, dtype = torch.float32 )

#prepare the model
N = 2 * len( vocabulary ) + len( alphabet )
M = len( vocabulary )
D = 256

rate = 0.01

model = torch.nn.Sequential(
        #input neurons
        torch.nn.Linear( N, D ) # N = X[i]
        torch.nn.ReLU( inplace = True )
        torch.nn.Dropout( p = 0.2 )         #dropuot randomly zeroes some of the elements of the input tensor with probability p
        
        torch.nn.Linear( D, D )             #first from four deep layers
        torch.nn.ReLU( inplace = True )
        
        torch.nn.Linear( D, D )             #2
        torch.nn.ReLU( inplace = True )
        torch.nn.Dropout( p = 0.5 )
        
        torch.nn.Linear( D, D )             #3
        torch.nn.ReLU( inplace = True )
        torch.nn.Dropout( p = 0.5 )
        
        torch.nn.Linear( D, D )             #4
        torch.nn.ReLU( inplace = True )
        
        torch.nn.Linear( D, M )             #output neurons
        torch.nn.LogSoftmax( dim = 1 )



