import csv
import numpy as np
import scipy as sp
from sklearn import tree, svm
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.cross_validation import train_test_split
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score


def main(fdir_train):
    #read data
    data = []
    label = []
    with open(fdir_train,'rb')as f:
        reader = csv.reader(f)
        for row in reader:
            temp = []
            for l in range(0,len(row)-1):
                temp.append(float(row[l]))
            data.append(temp)
            if row[len(row)-1]=='R':
                label.append(0)
            else:
                label.append(1)

    x = np.array(data)
    y = np.array(label)

    return x,y

def decision_tree(x,y):

    #train decision tree
    print "#############Decision Tree#############"
    clf = tree.DecisionTreeClassifier(criterion='entropy')
    scores = cross_val_score(clf,x,y,cv=10,scoring='f1_macro')
    print np.mean(scores)

def SVM(x,y):

    print "#############SVM#############:"
    clf = svm.LinearSVC()
    scores = cross_val_score(clf,x,y,cv=10,scoring = 'f1_macro')
    print np.mean(scores)

def Naive_Bayes(x,y):

    print "#############Naive Bayes#############:"
    clf = GaussianNB()
    scores = cross_val_score(clf,x,y,cv=10,scoring = 'f1_macro')
    print np.mean(scores)

def Logistic_Regression(x,y):

    print "#############Logistic Retression#############:"
    clf = LogisticRegression()
    scores = cross_val_score(clf,x,y,cv=10,scoring = 'f1_macro')
    print np.mean(scores)

if __name__ == '__main__':
    #read data
    fdir_train = './sonar.csv'
    x, y = main(fdir_train)

    #Decision Tree
    decision_tree(x,y)

    #SVM
    SVM(x,y)

    #Naive Bayes
    Naive_Bayes(x,y)

    #Logistic Regression
    Logistic_Regression(x,y)
