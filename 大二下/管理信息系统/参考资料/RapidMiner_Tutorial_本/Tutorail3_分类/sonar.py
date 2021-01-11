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

    #split train and test data set
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

    return x_train, x_test, y_train, y_test,x,y

def decision_tree(x_train,x_test,y_train,y_test,x,y):

    #train decision tree
    print "#############Decision Tree#############"
    clf = tree.DecisionTreeClassifier(criterion='entropy')
    #print "##############clf##########"
    #print (clf)
    clf.fit(x_train,y_train)

    #write the tree structure into document
    with open("tree.dot",'w')as f:
        f = tree.export_graphviz(clf,out_file=f)

    #The value characterizes the feature weight
    #print "#############feature weight##########"
    #print clf.feature_importances_

    #print test result
    answer = clf.predict(x_test)
    print "test result:"
    print "answer:"
    print answer
    print "y_test"
    print y_test

    #precision,recall,fmeasure
    answer = clf.predict_proba(x_test)[:,1]
    print "report:"
    print classification_report(y_test, answer, target_names=['R','M'])

    ##cross validation
    #scores = cross_val_score(clf,x,y,cv=5,scoring='f1_macro')
    #print "cross validation"
    #print np.mean(scores)

def SVM(x_train,y_train,x_test,y_test,x,y):

    print "#############SVM#############:"
    clf = svm.LinearSVC()
    clf.fit(x_train,y_train)
    answer = clf.predict(x_test)
    print "test result:"
    print "answer:"
    print answer
    print "y_test"
    print y_test

    #precision,recall,fmeasure
    print "report:"
    print classification_report(y_test, answer, target_names=['R','M'])

    ##cross validation
    #scores = cross_val_score(clf,x,y,cv=5,scoring = 'f1_macro')
    #print "cross validation"
    #print np.mean(scores)

def Naive_Bayes(x_train,y_train,x_test,y_test,x,y):

    print "#############Naive Bayes#############:"
    clf = GaussianNB()
    clf.fit(x_train,y_train)
    answer = clf.predict(x_test)
    print "test result:"
    print "answer:"
    print answer
    print "y_test"
    print y_test

    #precision,recall,fmeasure
    print "report:"
    print classification_report(y_test, answer, target_names=['R','M'])
    
    ##cross validation
    #scores = cross_val_score(clf,x,y,cv=5,scoring = 'f1_macro')
    #print "cross validation"
    #print np.mean(scores)

def Logistic_Regression(x_train,y_train,x_test,y_test,x,y):

    print "#############Logistic Retression#############:"
    clf = LogisticRegression()
    clf.fit(x_train,y_train)
    answer = clf.predict(x_test)
    print "test result:"
    print "answer:"
    print answer
    print "y_test"
    print y_test

    #precision,recall,fmeasure
    print "report:"
    print classification_report(y_test, answer, target_names=['R','M'])
    
    ##cross validation
    #scores = cross_val_score(clf,x,y,cv=5,scoring = 'f1_macro')
    #print "cross validation"
    #print np.mean(scores)

if __name__ == '__main__':
    fdir_train = './sonar.csv'
    x_train, x_test, y_train, y_test, x, y = main(fdir_train)

    #Decision Tree
    decision_tree(x_train,x_test,y_train,y_test,x,y)

    #SVM
    SVM(x_train,y_train,x_test,y_test,x,y)

    #Naive Bayes
    Naive_Bayes(x_train,y_train,x_test,y_test,x,y)

    #Logistic Regression
    Logistic_Regression(x_train,y_train,x_test,y_test,x,y)
