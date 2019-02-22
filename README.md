<i>This was a project originally created for Artificial Intelligence and Heuristic Programming at the University of Akron

<b>Versions: Python 3.5.6 - Sklearn 0.20.0 - Pandas 0.23.4 - Numpy 1.15.2</b>

Special thanks to scikit-learn.org's documentation. The Decision trees implemented here are Classification Tree with the CART Algorithm from the sklearn package.
Additionally, the book "Hands-On Machine Learning with Scikit-Learn and TensorFlow" by Aurélien Géron was a tremendous help in getting started with this code.

This project creates a decision tree using sk-learn, and allows the user to create a DecisionTree using their own .csv, save the tree, load the tree, and perform more examples using the trees
</i>

<b><i>Note: data must be in csv format. N/A values are dropped</i></b>


<b>Recent Modifications:</b>

- Support non-numeric data

  > Change load_data method to encode non-numeric attributes using pd.get_dummies

  > TARGET is encoded using labelencoder

- Change TargetCol obtaining to require valid column title

- Remove showTree, as not needed for project

- Add getMetrics, as needed for project

- Naming of Tree variables clarified (Array to TreeInfo)

- Remove Regression Tree functionality (unneeded for project)


Limitations, not planned on improving:

- Expects .csv file with the first row being attribute titles

- Drops N/A values


<b> Planned Improvements: </b>
- The makeDecision is awful and I don't know why

- Add Regression Tree back in

- Visualize tree

- MakeDecision accept text fields (?)

- Better MakeDecision function


<b>Methods:</b>

<b>getDataInfo: </b>
            Takes data, returns a list of attributes and their possible values
            If attributes are object-type, lists each possible value,
            If numerical, lists the range
            Returns a dictionary {"attribute" : [pos_values]}
            
<b>loadData: </b>
            Takes a filename, returns a Pandas Dataframe from the csv file
            uses Panda.get_dummies to one-hot encode non-numerical attributes
            returns the data and encoded attribute information

<b>LearnNewTree: </b>
            interactively guides user to enter all required files
            Returns array containing the tree, list of attributes, and the target attribute

<b>SaveTree: </b>
            Pickles the array containing tree, attributes and target
           Will interactively guide user to enter all required files
           Returns true if successful, o.w. print error and return false

<b>MakeDecision: </b>
            Allows for one test case
           Takes the tree, a list of attributes, and the target name
           Prompts user to enter the feature for each attribute
           Note that these are One-Hot encoded attributes, 
           so non-numerical data will prompt for each possibility. 
           Only one can be "Hot" from each set.
           Returns the target

<b>getMetrics: </b>
            Runs sklearn's built-in accuracy_score function with the test set
            to develop metrics


<b>main: </b>
            A Wrapper, handling errors and walking the user through tree creation
