from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, classification_report
import numpy as np
import json
import dump

X_train = np.load('../dataset/X_train.npy')
y_train = np.load('../dataset/y_train.npy')
print('X_train:{0}, y_train:{1}'.format(X_train.shape, y_train.shape))

clf = RandomForestClassifier()
print('Cross Validation Score: {0}'.format(np.mean(cross_val_score(clf, X_train, y_train, cv=10))))

clf.fit(X_train, y_train)

X_test = np.load('../dataset/X_test.npy')
y_test = np.load('../dataset/y_test.npy')

pred = clf.predict(X_test)
print('Accuracy: {}'.format(accuracy_score(y_test, pred)))

#print(forest_to_json(clf))
json.dump(dump.forest_to_json(clf), open('../../static/classifier.json', 'w'))

# print Number Tree in Random Forest Classification 
n_trees = clf.n_estimators
print("Number of trees in the random forest: {}".format(n_trees))

# -------------------------

# Create confusion matrix
conf_matrix = confusion_matrix(y_test, pred)
print("Confusion Matrix:")
print(conf_matrix)

# Generate classification report
class_report = classification_report(y_test, pred)
print("Classification Report:")
print(class_report)