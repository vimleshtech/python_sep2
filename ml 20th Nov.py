import pandas #dataframe

from pandas.tools.plotting import scatter_matrix #plog 
import matplotlib.pyplot as plt #plot/visualization (graph)

from sklearn import model_selection   #selecte the logic/algo
from sklearn.metrics import classification_report # grouping/ categorization
from sklearn.metrics import confusion_matrix#fold(no of test) test 
from sklearn.metrics import accuracy_score #
from sklearn.linear_model import LogisticRegression #
#regression :  score ~ hours (linear regression : one dependent and one independent)
#logistics : one dependent (output) and multiple independent (input)

from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
cols = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=cols)


# box and whisker plots
#dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
#dataset.plot(kind='line', subplots=True, layout=(2,2), sharex=False, sharey=False)
#dataset.plot(kind='bar', subplots=True, layout=(2,2), sharex=False, sharey=False)
#dataset.plot(kind='line', subplots=False, layout=(2,2), sharex=False, sharey=False)
#dataset.plot(kind='pie', subplots=True, layout=(2,2), sharex=False, sharey=False)

#plt.show()


# histograms
#dataset.hist()
#plt.show()
# scatter plot matrix
#scatter_matrix(dataset)
#plt.show()


#


#train data   : historical or research data
#test data    : to be tested /validated

# Split-out validation dataset
array = dataset.values   # convert dataframe to list 
X = array[:,0:4]         # slicker , get first four(numerical) columns form list
#: - all rows , 0:4 : 4 columns

Y = array[:,4]

validation_size = 0.20
seed = 7#pick and get row on every 7th index
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)


# Test options and evaluation metric
seed = 7
scoring = 'accuracy'


# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))

# evaluate each model in turn
results = []
names = []
for name, model in models:
     
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	
	results.append(cv_results)	
	names.append(name)
	
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)

     
















