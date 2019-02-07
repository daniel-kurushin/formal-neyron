# formal-neyron
Very simple neuron example for students

This program is aided to demonstrate basics of neural networking.

Class Neuron can be "teached" to recognize pattern X with 
vector D. Inputs are 1/0, output 1/0.

One can change sigma or __call__ methods to manipulate
neuron functionality.

Possible tasks are:

D = [
    [[1,1,0],0],
    [[0,1,1],1],
    [[1,1,0],0],
]

D = [
    [[0,0,0],0],
    [[0,1,1],3],
    [[1,1,1],7],
]

Impossible task is:
D = [
    [[1,1],0],
    [[0,1],1],
    [[1,0],1],
    [[0,0],0],
]

