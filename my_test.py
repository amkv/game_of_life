# -*- coding: utf-8 -*-

import sys
import os
import numpy as np
from pandas import read_csv as read
from sklearn import preprocessing
from sklearn import metrics


def main(argv):
    # if len(argv) < 2:
    #     sys.exit(0)
    # my_file = open(argv[1], 'r')
    #
    # data = read(my_file, delimiter=",")
    #
    # x = data.values[:, 1:802]
    # y = data.values[:, 0:1]
    # # clf = RandomForestClassifier()
    # # clf.fit(x, y)
    # normalized_X = preprocessing.normalize(x)
    # standardized_X = preprocessing.scale(x)
    #
    # from sklearn import metrics
    # from sklearn.linear_model import LogisticRegression
    # model = LogisticRegression()
    # model.fit(x, y)
    # print(model)
    # # make predictions
    # expected = y
    # predicted = model.predict(x)
    # # summarize the fit of the model
    # print(metrics.classification_report(expected, predicted))
    # print(metrics.confusion_matrix(expected, predicted))
    from sklearn import datasets
    from sklearn.model_selection import cross_val_predict
    from sklearn import linear_model
    import matplotlib.pyplot as plt

    lr = linear_model.LinearRegression()
    boston = datasets.load_boston()
    y = boston.target

    # cross_val_predict returns an array of the same size as `y` where each entry
    # is a prediction obtained by cross validation:
    predicted = cross_val_predict(lr, boston.data, y, cv=10)

    fig, ax = plt.subplots()
    ax.scatter(y, predicted)
    ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
    ax.set_xlabel('Measured')
    ax.set_ylabel('Predicted')
    plt.show()




if __name__ == "__main__":
    os.system('clear')
    main(sys.argv)

