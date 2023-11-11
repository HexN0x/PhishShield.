
from sklearn.tree import _tree
def tree_to_json(tree):
    tree_ = tree.tree_
    feature_names = range(30)
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]
    def recurse(node):
        tree_json = dict()
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            tree_json['type'] = 'split'
            threshold = tree_.threshold[node]
            tree_json['threshold'] = "{} <= {}".format(feature_name[node], threshold)
            tree_json['left'] = recurse(tree_.children_left[node])
            tree_json['right'] = recurse(tree_.children_right[node])
        else:
            tree_json['type'] = 'leaf'
            tree_json['value'] = tree_.value[node].tolist()
        return tree_json

    return recurse(0)

def forest_to_json(forest):
    forest_json = dict()
    
    # Calculate the number of features based on the first tree
    n_features = forest.estimators_[0].tree_.n_features
    
    forest_json['n_features'] = n_features
    forest_json['n_classes'] = forest.n_classes_
    forest_json['classes'] = forest.classes_.tolist()
    forest_json['n_outputs'] = forest.n_outputs_
    forest_json['n_estimators'] = forest.n_estimators
    forest_json['estimators'] = [tree_to_json(estimator) for estimator in forest.estimators_]
    return forest_json

