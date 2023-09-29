# %%
import numpy as np
from sklearn import datasets, tree
from sklearn.model_selection import train_test_split


def accuracy(y_true, y_pred):   
    accuracy = np.sum(y_true == y_pred)/len(y_true)   
    return accuracy
data = datasets.load_breast_cancer()
X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=123)

# %%
clf = tree.DecisionTreeClassifier(max_depth = 10)
clf.fit(X_train, y_train)


y_pred1 = clf.predict(X_train)
acc1 = accuracy(y_train, y_pred1)
print("Training Accuracy: ", acc1)
# %%
