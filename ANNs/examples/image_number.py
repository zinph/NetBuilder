"""
Created on Fri Feb  5 16:32:41 2016

@author: andresberejnoi
"""
import numpy as np
from ..NeuralNet import network


shapes = {0: np.array([ [-0.5,-0.5,0.5,0.5,-0.5,-0.5],
                        [-0.5,0.5,-0.5,-0.5,0.5,-0.5],
                        [-0.5,0.5,-0.5,-0.5,0.5,-0.5],
                        [-0.5,0.5,-0.5,-0.5,0.5,-0.5],
                        [-0.5,0.5,-0.5,-0.5,0.5,-0.5],
                        [-0.5,-0.5,0.5,0.5,-0.5,-0.5]]),

          1: np.array([ [-0.5,-0.5,0.5,0.5,-0.5,-0.5],
                        [-0.5,-0.5,0.5,0.5,-0.5,-0.5],
                        [-0.5,-0.5,0.5,0.5,-0.5,-0.5],
                        [-0.5,-0.5,0.5,0.5,-0.5,-0.5],
                        [-0.5,-0.5,0.5,0.5,-0.5,-0.5],
                        [-0.5,-0.5,0.5,0.5,-0.5,-0.5]]),

          2: np.array([ [-0.5,-0.5,0.5,0.5,-0.5,-0.5],
                        [-0.5,0.5,-0.5,-0.5,0.5,-0.5],
                        [-0.5,-0.5,-0.5,-0.5,0.5,-0.5],
                        [-0.5,-0.5,-0.5,0.5,-0.5,-0.5],
                        [-0.5,-0.5,0.5,-0.5,-0.5,-0.5],
                        [-0.5,0.5,0.5,0.5,0.5,-0.5]]),

          3: np.array([ [-0.5,0.5,0.5,0.5,0.5,-0.5],
                        [-0.5,-0.5,-0.5,-0.5,0.5,-0.5],
                        [-0.5,0.5,0.5,0.5,0.5,-0.5],
                        [-0.5,0.5,0.5,0.5,0.5,-0.5],
                        [-0.5,-0.5,-0.5,-0.5,0.5,-0.5],
                        [-0.5,0.5,0.5,0.5,0.5,-0.5]]),

          4: np.array([ [-0.5,0.5,-0.5,-0.5,0.5,-0.5],
                        [-0.5,0.5,-0.5,-0.5,0.5,-0.5],
                        [-0.5,0.5,0.5,0.5,0.5,-0.5],
                        [-0.5,-0.5,-0.5,-0.5,0.5,-0.5],
                        [-0.5,-0.5,-0.5,-0.5,0.5,-0.5],
                        [-0.5,-0.5,-0.5,-0.5,0.5,-0.5]]),

          5: np.array([ [-0.5,0.5,0.5,0.5,0.5,-0.5],
                        [-0.5,0.5,-0.5,-0.5,-0.5,-0.5],
                        [-0.5,0.5,0.5,0.5,0.5,-0.5],
                        [-0.5,-0.5,-0.5,-0.5,0.5,-0.5],
                        [-0.5,-0.5,-0.5,-0.5,0.5,-0.5],
                        [-0.5,0.5,0.5,0.5,0.5,-0.5]]),

          6: np.array([ [-0.5,0.5,0.5,0.5,0.5,-0.5],
                        [-0.5,0.5,-0.5,-0.5,0.5,-0.5],
                        [-0.5,0.5,0.5,0.5,0.5,-0.5],
                        [-0.5,0.5,-0.5,-0.5,0.5,-0.5],
                        [-0.5,0.5,-0.5,-0.5,0.5,-0.5],
                        [-0.5,0.5,0.5,0.5,0.5,-0.5]]),

          7: np.array([ [-0.5,0.5,0.5,0.5,0.5,0.5],
                        [-0.5,0.5,-0.5,-0.5,0.5,-0.5],
                        [-0.5,-0.5,-0.5,0.5,-0.5,-0.5],
                        [-0.5,0.5,0.5,0.5,-0.5,-0.5],
                        [-0.5,0.5,-0.5,-0.5,-0.5,-0.5],
                        [0.5,-0.5,-0.5,-0.5,-0.5,-0.5]]),

          8: np.array([ [-0.5,0.5,0.5,0.5,0.5,-0.5],
                        [-0.5,0.5,-0.5,-0.5,0.5,-0.5],
                        [-0.5,0.5,0.5,0.5,0.5,-0.5],
                        [-0.5,0.5,-0.5,-0.5,0.5,-0.5],
                        [-0.5,0.5,-0.5,-0.5,0.5,-0.5],
                        [-0.5,0.5,0.5,0.5,0.5,-0.5]]),

          9: np.array([ [-0.5,0.5,0.5,0.5,0.5,-0.5],
                        [-0.5,0.5,-0.5,-0.5,0.5,-0.5],
                        [-0.5,0.5,0.5,0.5,0.5,-0.5],
                        [-0.5,-0.5,-0.5,-0.5,0.5,-0.5],
                        [-0.5,-0.5,-0.5,-0.5,0.5,-0.5],
                        [-0.5,0.5,0.5,0.5,0.5,-0.5]]),
}

class number(object):
    """
    This class provides methods for creating simulated image inputs for a neural network.
    The purpose is that it can generate inputs to train a neural network in pattern recognition of numbers.    
    """
    def __init__(self,number = 0, resolution = 36, noise = 0.0):
        """Initializer"""
        self.shape = number
        self.res = resolution
        self.noise = noise
        
        
        

#test script below
from trainingShapes import shapes2

inputs1 = [shape.flatten() for shape in shapes.values()]            #creates a list of the values in the dictionary
inputs2 = [shape.flatten() for shape in shapes2.values()]

inputs = inputs1 + inputs2
#inputs = inputs1

'''
targets = [np.array([1,0,0,0,0,0,0,0,0,0]),             #we want a zero
           np.array([0,1,0,0,0,0,0,0,0,0]),             #we want a 1
           np.array([0,0,1,0,0,0,0,0,0,0]),
           np.array([0,0,0,1,0,0,0,0,0,0]),
           np.array([0,0,0,0,1,0,0,0,0,0]),
           np.array([0,0,0,0,0,1,0,0,0,0]),
           np.array([0,0,0,0,0,0,1,0,0,0]),
           np.array([0,0,0,0,0,0,0,1,0,0]),
           np.array([0,0,0,0,0,0,0,0,1,0]),
           np.array([0,0,0,0,0,0,0,0,0,1])]
'''


targets = [np.array([0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5]),             #we want a zero
           np.array([-0.5,0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5]),             #we want a 1
           np.array([-0.5,-0.5,0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5]),
           np.array([-0.5,-0.5,-0.5,0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5]),
           np.array([-0.5,-0.5,-0.5,-0.5,0.5,-0.5,-0.5,-0.5,-0.5,-0.5]),
           np.array([-0.5,-0.5,-0.5,-0.5,-0.5,0.5,-0.5,-0.5,-0.5,-0.5]),
           np.array([-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,0.5,-0.5,-0.5,-0.5]),
           np.array([-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,0.5,-0.5,-0.5]),
           np.array([-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,0.5,-0.5]),
           np.array([-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,0.5])]


trainingSet = list(zip(inputs,targets+targets))
#trainingSet = list(zip(inputs,targets))

topology = [36,50,50,10]
net = network(topology,0.01,0.01)
#net.save("recog_number_weights.csv", transpose=True, keep_bias=False)

#random_out = net.feedforward(inputs[1])

epochs = 10000
tolerance = 1E-5

net.train(trainingSet,epochs,tolerance)
#print()
#print(random_out)

