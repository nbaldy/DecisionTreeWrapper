This was a project originally created for Artificial Intelligence and Heuristic Programming at the University of Akron

Special thanks to scikit-learn.org's documentation. The Decision trees implemented here are Classification and Regression tree CART Algorithms from the sklearn package.
Additionally, the book "Hands-On Machine Learning with Scikit-Learn and TensorFlow" by Aurélien Géron was a tremendous help in getting started with this code.

This project creates a decision tree using sk-learn, and allows the user to create a DecisionTree using their own .csv, save the tree, load the tree, and perform more examples using the trees

 Drawbacks/Future Modifications:
           Expects .csv file with the first row being attribute titles
           Cannot choose from test set to try tree


Methods:
load_data: returns a Pandas Dataframe from the csv file
LearnNewTree: interactively guides user to enter all required files
              Returns array containing the tree, list of attributes, and the target attribute
SaveTree: Pickles the array containing tree, attributes and target
           Will interactively guide user to enter all required files
           Returns true if successful, o.w. print error and return false
MakeDecision: Allows for one test case
           Takes the tree, a list of attributes, and the target name
           Prompts user to enter the feature for each attribute
           Returns the target
showTree: Creates a .dot file showing the tree using graphviz
main: A Wrapper, handling errors and walking the user through tree creation 
