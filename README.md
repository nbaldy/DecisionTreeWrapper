<i>This was a project originally created for Artificial Intelligence and Heuristic Programming at the University of Akron

<b>Versions: Python 3.5.6 - Sklearn 0.20.0 - Pandas 0.23.4 - Numpy 1.15.2</b>

Special thanks to scikit-learn.org's documentation. The Decision trees implemented here are Classification Tree with the CART Algorithm from the sklearn package.
Additionally, the book "Hands-On Machine Learning with Scikit-Learn and TensorFlow" by Aurélien Géron was a tremendous help in getting started with this code.

This project creates a decision tree using sk-learn, and allows the user to create a DecisionTree using their own .csv, save the tree, load the tree, and perform more examples using the trees
</i>

<b><i>Note: data must be in csv format. N/A values are dropped</i></b>

**Supports non-numeric data, though it must OneHotEncode attributes and uses LabelEncoder for target if they are text fields**
- *I don't like using two different encoding sysems, but labelEncoder isn't good to use for attributes, as it causes unintentional relations between text fields (ex: "Blue" =1, "Grey" = 2, "Yellow" = 3; "Yellow" is closer to "Grey")*
- *I had trouble with multiple targets, so I didn't want to OneHot encode target. Also, I can inverse-encode it for usability easier. There's probably a better way and I'll get around to it eventually*


**Methods:**
* loadData:
  * Takes a filename, returns a formatted Pandas Dataframe from the csv file
  * Uses Panda.get_dummies to one-hot encode non-numerical attributes
  * Uses LabelEncoder to encode non-numerical target attributes
  * Uses getMetrics to obtain accuracy score
  * Returns the encoded data, target column, and encoder or -1


*	getMetrics:
  * Takes the tree, test set, and targetCol, returns the accuracy score of the tree
  * Returns the value of sklearn's built-in accuracy_score function with the test set


 * LearnNewTree:
  * Prompts for user input, returns tree information
  * Interactively guides user to enter all required files
  * Uses loadData to obtain attribute list, formatted Dataframe, and target
  * Creates the decision tree of user-selected max depth
  * Returns array containing the tree, list of attributes, and encoding information
     * encoded information in the form
        * (True, labelEncoder) if non-numerical
        * (False, sorted target classes) if numerical

* SaveTree:
  * Takes the treeInformation, prompts for save filename, boolean return indicates save success
  * Pickles the array containing tree, attributes, target and performance
  * Will interactively guide user to enter all required files
  * Returns true if successful, o.w. print error and return false


* LoadTree:
  * Prompts for filename, returns tree information
  * Unpickles the array containing tree, attributes, target and performance
  * Calls MakeDecision until user chooses to quit
  * No Return


* MakeDecision:
  * Takes tree information, interactively guides user through decision making
  * Starts at first node in decision tree
  * Asks if data is less than or greater than threshold
  * Goes until reaches leaf node
  * Prints final decision


* **main:**
  * A Wrapper function for the DecisionTree making,
  * Formats the menu and walks user through tree creation
  * Handles errors
