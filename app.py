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
        torch.nn.Linear( N, D ), # N = X[i]
        torch.nn.ReLU( inplace = True ),
        torch.nn.Dropout( p = 0.2 ),         #dropuot randomly zeroes some of the elements of the input tensor with probability p
        
        torch.nn.Linear( D, D ),             #first from four deep layers
        torch.nn.ReLU( inplace = True ),
        
        torch.nn.Linear( D, D ),             #2
        torch.nn.ReLU( inplace = True ),
        torch.nn.Dropout( p = 0.5 ),
        
        torch.nn.Linear( D, D ),             #3
        torch.nn.ReLU( inplace = True ),
        torch.nn.Dropout( p = 0.5 ),
        
        torch.nn.Linear( D, D ),             #4
        torch.nn.ReLU( inplace = True ),
        
        torch.nn.Linear( D, M ),             #output neurons
        torch.nn.LogSoftmax( dim = 1 )
)

loss = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam( model.parameters(),  lr = rate )
#print( model )

epochs = 100
for i in range ( epochs ):
    optimizer.zero_grad()

    Yp = model( X )

    step_loss = loss( input = Yp, target = Y )

    step_loss.backward()
    optimizer.step()
    if i % 10 == 0:
        print ('epoch [{}], Loss: {:.2f}'.format( i, step_loss.item() ))

text_kb = input( "Hi! Input 2 words ant a letter >>>\n" )
textAsWordsKb = text_kb.split( " " )
Xw1 = wordToOneHotVector(textAsWordsKb[0])
Xw0 = wordToOneHotVector(textAsWordsKb[1])
Xc0 = characterToOneHotVector(textAsWordsKb[2])

Xkb = torch.tensor([Xw1+Xw0+Xc0],dtype=torch.float32)
#print(Xkb)
Ypr = model.forward(Xkb).detach()

iy = Ypr.argmax()
print( oneHotVectorToWord( [0] * iy + [1] + (len(vocabulary) - iy - 1)  * [0]) )






