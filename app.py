#!/usr/bin/env python3

from services import *
from os import system
import torch


X = torch.tensor( X_, dtype = torch.float32 )
Y = torch.tensor( Y_, dtype = torch.float32 )

system( "clear" )
print("TENSORS")
print(X)
print(X.shape)
print(Y)
print(Y.shape)

#prepare the model
N = 2 * len( vocabulary ) + len( alphabet )
M = len( vocabulary )
D = 256

rate = 0.01




