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
#import numpy
#dataset = numpy.loadtxt("pima-indians-diabetes.data.csv", delimiter=",")
# split into input (X) and output (Y) variables
#print(dataset[:,1:4])
#X = dataset[:,0:8]
#Y = dataset[:,8]

from pymongo import MongoClient
client = MongoClient("mongodb://sell4bids:KPChH7D2uF2gjN9Q@176.9.139.247:27017")
db = client['sell4bids']
collection = db.rasaqueries
data = {
            'title': 'zeeshan',
            'date':
             }
result = collection.insert_one(data)

print('One post: {0}'.format(result.inserted_id))
scotts_posts = collection.find({'author': 'Scott'})

for n in scotts_posts:
 print(n)