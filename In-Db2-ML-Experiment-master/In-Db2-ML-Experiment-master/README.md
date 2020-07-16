# In-Db2-ML-Experiment
Comparing prediction performance of Python UDFs vs. Notebook Only approach

## Content:
This reposity contains the following:

- `pyudf.py`: The Python UDF
- `CreditCardML.ipynb`: Model selection and training
- `CreditCard-Notebook-Predict.ipynb`: Client side only predictions
- `CreditCard-UDF-Predict.ipynb`: Python UDF predictions
- `Experiment Results.ipynb`: Experiment results and visualizations

## Objective: 
-	Analyze the performance the current machine learning capabilities of Db2, namely the use of Python User Defined Functions (UDF) 
-	Compare the performance of Python UDF to a “Jupyter notebook only” approach

## Data:

The dataset, taken from Kaggle (https://www.kaggle.com/mlg-ulb/creditcardfraud), contains transactions made by credit cards in September 2013 by European cardholders. This dataset has 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions. Oversampling is used to balance the dataset before feeding it to a model for training.

## Method:

The experimental setup consists of 3 notebooks. Performance is measured using total runtime (i.e. the total time it takes from connecting and loading the data from Db2 to model prediction). Tests are done on predictions of 1,000, 5,000, 10,000, 50,000, and 100,000 rows of test data. Runtimes are averaged over 10 runs.

1.	Model selection and training – `CreditCardML.ipynb`
- Load data from Db2
- Data transformation – Split dataset into training and test set, removing redundant features, feature scaling, and oversampling of fraud class to balance training data 
- Copying testing data set to Db2 for later use
- Model Selection – Decision Tree Classifier. Performs best (highest training recall), so other models (Logistic Regression, Random Forest Classifier, SVC) not used
- Model Tuning – Using GridSearchCV, return model that performs best on validation set
- Save model and scaler for use on test data

2.	Client side only notebook – `CreditCard-Notebook-Predict.ipynb`
- Load test data from Db2
- Load saved model
- Predict on the test data using the model
- Return total runtime to user

3.	Python UDF notebook – `CreditCard-UDF-Predict.ipynb`
- Connect to Db2
- Execute SQL statement that calls the UDF that loads the saved model, and calls the model to make a prediction
- Return the predictions as a pandas object
- Return total runtime to user

## Results

It is found that the Python UDF reduces runtime by an average of 19% and is largely unaffected by the batch size. Detailed discussion and visualizations can be found in `Experiment Results.ipynb`
