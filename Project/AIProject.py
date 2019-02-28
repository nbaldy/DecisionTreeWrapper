
# coding: utf-8

# In[ ]:


###################################
# Drawbacks:
#  Expects .csv file with the first row being attribute titles
#  Drops NA


# In[ ]:


import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import accuracy_score
from collections import OrderedDict
from sklearn.preprocessing import LabelEncoder


####################
# getAttributes (helper to loadData)
# Takes a panda dataframe
# Creates an ORDERED dictionary containing
# {colName: [possible_values]} for text attributes
# or {colName:[range]} for numerical attributes
####################
def getAttributes(data):
    attributes = OrderedDict()
    for col in data.columns:
        if data[col].dtype != object:
            attributes[col] = [data[col].min(), data[col].max()]
        else:
            attributes[col] = list(data[col].unique())
    return attributes


#########################
# loadData (Helper to LearnNewTree)
# Deletes duplicates, one-hot encodes data
# Returns data (Pandas DF) and feature list (Dict)
#############################
def loadData(filename):
    data = pd.read_csv(filename).dropna()
    print("Choose Target column:")
    print(list(data))
    targetCol = input(">> ")
    while targetCol not in list(data):
        print(list(data))
        targetCol = input(">> ")

    attributes = getAttributes(data.drop(targetCol, axis=1).copy())
    le = -1
    if data[targetCol].dtype == object:
        le = LabelEncoder()
        le.fit(data[targetCol].unique())
        data[targetCol] = le.transform(data[targetCol])

    data = pd.get_dummies(data)

    return (attributes, data, targetCol, le)


################################
# getMetrics (Helper to  LearnNewTree)
# Takes the test set, the targetCol, and the tree
# Computes the accuracy using sklearn's accuracy_score
# Returns the accuracy score
###############################
def getMetrics(myTree, myTests, targetCol):
    X = myTests.drop(targetCol, axis=1).copy()
    y = myTests[targetCol]
    predictions = myTree.predict(X)
    accuracy =  accuracy_score(y, predictions)
    return accuracy


#####################
# LearnNewTree (1)
# Will interactively guide user to enter all required files
# Returns array containing the tree, attribute list, target attribute,
#                              target attribute, and encoded attributes
#####################
def LearnNewTree():
    dataPath = input("Enter name of data file: ")
    while dataPath != "" and dataPath[-4:] != ".csv":
        isCSV = input("Is this a CSV?: ").lower()
        if isCSV.find("y") != -1: dataPath += ".csv"
        else: dataPath = input("Sorry, we need a .CSV file.\nEnter New File: ")

    try:
        attributes, data, targetCol, le  = loadData(dataPath)
        train_set, test_set = train_test_split(data, test_size = 0.2, random_state = 42)

        X = train_set.drop(targetCol, axis=1).copy()
        y = train_set[targetCol].copy()

    except Exception as e:
        print("Exception: " ,e)
        print('Sorry, data invalid. Is {} a valid csv datafile?'.format(dataPath))
        return -1

    try:
        depth = input("Max Depth, or -1 to use none\n>> ")
        while not depth.isnumeric() and not depth[1:].isnumeric():
            depth = input("Max Depth, or -1 to use none\nPlease enter an integer\n>> ")
        if int(depth) > 0:
            myTree = DecisionTreeClassifier(max_depth = int(depth), random_state = 42)
        else:
            myTree = DecisionTreeClassifier(random_state = 42)

        myTree.fit(X, y)
        print("Tree Created")

        performance = getMetrics(myTree, test_set, y.name)
        print("Tree Accuracy Score: ", performance)

        if le != -1:
            return ([myTree, attributes, y.name, performance, list(X), le])
        return ([myTree, attributes, y.name, performance, list(X)])

    except Exception as e:
        print("Exception: " ,e)
        print("Sorry, Tree build failed")
        return -1


#####################
# SaveTree (2)
# Pickles the array containing tree, attributes and target
# Will interactively guide user to enter all required files
# Returns true if successful, o.w. print error and return false
#####################
def SaveTree(myTreeInfo):
    treeFile = ""
    while treeFile == "":
        treeFile = input("Tree File Name: ")
    try:
        pickle.dump(myTreeInfo, open(treeFile+".pickle", "wb"))
        return True

    except Exception as e:
        print("Oops, ", e)
        return false


#####################
# LoadTree (4)
# Unpickles the array containing the tree, attributes and target
# Will interactively guide user to enter all required files
# Returns the tree, attributes, and target
#####################
def LoadTree():
    try:
        treeFile = ""
        while treeFile == "":
            treeFile = input("Tree File Name: ")
        myTreeInfo = pickle.load(open(treeFile+".pickle", "rb"))
        return myTreeInfo

    except Exception as e:
        print("LoadTree file {} is invalid".format(treeFile))
        return -1



########################
# MakeDecision (3)
# Allows for one test case
# Takes the tree, a list of attributes, and the target name
# Prompts user to enter the feature for each attribute
# (Note that these are one-hot encoded attributes)
# Returns the target
########################
def MakeDecision(myTreeInfo):
    try:
        tree, attrSet, encodedAttr = myTreeInfo[0], myTreeInfo[1], myTreeInfo[4]
        featureSet = OrderedDict()
        for enc in encodedAttr:
            featureSet[enc] = [0]
        for attr in attrSet:
            userIn = ""
            if type(attrSet[attr][0]) == str:
                while userIn not in attrSet[attr]:
                    userIn = input("{}: Possible values are {}\n>> ".format(attr, attrSet[attr]))
                featureSet[attr+"_"+userIn] = [1]
            else:
                while True:
                    userIn = input("{}: Range is {}\n>> ".format(attr, attrSet[attr]))
                    try:
                        featureSet[attr] = [float(userIn)]
                        break
                    except:
                        print("Please ensure data is numerical")
                        continue
        prediction =  tree.predict(pd.DataFrame(featureSet))
        if len(myTreeInfo) == 6:
            encoder = myTreeInfo[5]
            prediction = encoder.inverse_transform(prediction)
        return prediction

    except Exception as e:
        print("Whoops! ", e)
        return -1

###############################
#define Main Method -
# Guide User through building tree
# Handle errors
################################
def main():
    try:
        myTreeInfo = -1 #empty Tree
        while(True):
            if myTreeInfo == -1:
                userIn = input("(1) to learn new decision tree\n"
                               "(4) to load previous decision tree\n"
                               "(5) to quit\n"
                               ">> "
                              )
            else:
                userIn = input("(1) to learn new decision tree\n"
                               "(2) to save current tree\n"
                               "(3) to apply tree to new cases\n"
                               "(4) to load previous decision tree\n"
                               "(5) to quit\n"
                               ">> "
                              )

            if userIn.find("1") != -1:
                print("\nLearning New Tree\n")
                myTreeInfo = LearnNewTree()

            elif userIn.find("2") != -1:
                print("\nSaving Tree\n")
                SaveTree(myTreeInfo)

            elif userIn.find("3") != -1:
                print("\nApply Decision Tree\n")
                while(userIn.find("3") != -1):
                    print("Decision: ", MakeDecision(myTreeInfo))
                    userIn = input(  "(3) to continue decision-making\n"
                                     "(5) to quit\n"
                                     ">> "
                                  )

            elif userIn.find("4") != -1:
                print("\nLoading Tree\n")
                myTreeInfo = LoadTree()
                if myTreeInfo != -1:
                    print("Tree Accuracy Score: ", myTreeInfo[3])

            elif userIn.find("5") != -1:
                print("\nQuitting program...\n")
                break

            else:
                print("Sorry, command not recognized. Please try again.")
                continue
        print("Thank you for learning with our Decision Tree")
        print("Program exiting...")
    except Exception as e:
        print(e)
        print("Program terminating...")
        return(1)

#Run Main Method
if __name__== "__main__":
       myTreePicture = main()
