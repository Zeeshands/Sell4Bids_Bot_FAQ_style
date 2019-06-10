from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets

iris=datasets.load_iris()

#print (iris)
#print(iris['target_names'])

#model = DecisionTreeClassifier()
#model.fit(iris.data,iris.target)
#print(model.predict([[5.9, 3 , 5.1, 1.8]]))

print(iris)
print(iris.data[:,0])
