<i>This was a project originally created for Artificial Intelligence and Heuristic Programming at the University of Akron

<b>Versions: Python 3.5.6 - Sklearn 0.20.0 - Pandas 0.23.4 - Numpy 1.15.2</b>

Special thanks to scikit-learn.org's documentation. The Decision trees implemented here are Classification Tree with the CART Algorithm from the sklearn package.
Additionally, the book "Hands-On Machine Learning with Scikit-Learn and TensorFlow" by Aurélien Géron was a tremendous help in getting started with this code.

This project creates a decision tree using sk-learn, and allows the user to create a DecisionTree using their own .csv, save the tree, load the tree, and perform more examples using the trees
</i>

<b><i>Note: data must be in csv format. N/A values are dropped</i></b>

<B> NOT WORKING </B> 
MakeDecision. UUUUUURGH. MY EYES. I'VE BEEN LOOKING AT IT FOR HOURS AND ALL I FEEL IS PAIN. 
The dictionaries are messing up ordering and prediction doesn't seem to support DataFrames in terms of correct ordering of labels. 
So, I probably need to use a different data structure. Trying OrderedDictionaries but it's not working. 
I'll look at it tomorrow. 

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


<b> Improvements I hope to make: </b>

- Add Regression Tree back in

- Visualize tree

- Better MakeDecision function

- Target and attributes use different encoding and that's probably a bad



<b>Methods:</b>

<b>getAttributes: </b>
            Takes data, returns a list of attributes and their possible values
            If attributes are object-type, lists each possible value,
            If numerical, lists the range
            Returns a dictionary {attribute_name : list_of_values}
            
<b>loadData: </b>
            Takes a filename, returns a formatted Pandas Dataframe from the csv file
            Prompts for Target Column, and uses getAttributes to get attribute list
            uses Panda.get_dummies to one-hot encode non-numerical attributes
            uses LabelEncoder to encode non-numerical target attributes
            Uses getMetrics to obtain accuracy score
            returns the encoded data,  attribute information and target column

<b>getMetrics: </b>
            Takes the tree, test set, and targetCol, returns the accuracy score of the tree
            Returns the value of sklearn's built-in accuracy_score function with the test set
            
<b>LearnNewTree: </b>
            Prompts for user input, returns tree information
            Interactively guides user to enter all required files
            Uses loadData to obtain attribute list, formatted Dataframe, and target 
            Creates the decision tree of user-selected max depth
            Returns array containing the tree, list of attributes, target column, and performance 

<b>SaveTree: </b>
           Takes the treeInformation, prompts for save filename, boolean return indicates save success
           Pickles the array containing tree, attributes, target and performance
           Will interactively guide user to enter all required files
           Returns true if successful, o.w. print error and return false

<b>LoadTree: </b>
           Prompts for filename, returns tree information
           Unpickles the array containing tree, attributes, target and performance
           Returns array containing the tree, list of attributes, target column, and performance 
           
<b>MakeDecision: </b>
           Takes tree information, prompts for one test case, returns prediction
           Prompts user to enter the feature for each attribute
           Returns the predicted value

<b>main: </b>
            A Wrapper function for the DecisionTree making, 
            
            - Formats the menue and walks user through tree creation
            
            - handles errors
