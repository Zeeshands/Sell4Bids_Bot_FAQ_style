'''
import keras
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense

if __name__ == '__main__':
 model = Sequential([Dense(16,input_shape=(1,),activation='relu'),
                   Dense(32,activation='relu'),
                   Dense(2,activation='softmax')])
 model.summary()
 '''
import numpy
dataset = numpy.loadtxt("pima-indians-diabetes.data.csv", delimiter=",")
# split into input (X) and output (Y) variables
print(dataset[:,1:4])
#X = dataset[:,0:8]
#Y = dataset[:,8]

