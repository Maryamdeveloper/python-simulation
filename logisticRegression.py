#load dataset
import pandas as pd
df=pd.read_excel('E:\python-simulation\data\patients.xlsx')
df['Status'].replace(['Excellent','Good','Fair','Poor'],[4,3,2,1],inplace=True);
df=pd.get_dummies(df,columns=['Gender','Smoker'],drop_first=True);   #changed the gender and smoke
# create correlation matrix
Corr=df.corr()
# create training data from independant variables like age,... this is our input [] because there are multiple col
x=df[['Age','Height','Weight','Gender_Male','Systolic']].values
# predict wether the person was smoker or not this is our output
y=df['Smoker_True'].values

# Logistic Regression
from sklearn.linear_model import LogisticRegression 
# () after the LogisticRegression meant that use default variables for that
model = LogisticRegression()
# training here is done and will solve the equation that we had for logistic regression and calculates the coefficients
model.fit(x, y)
# it will also call the const value intercept 
print(model.coef_, model.intercept_)
# we can not compare this coef because we had not normalized our data yet! and their scale is not the same
# now we can predict the label of this input
y_pred = model.predict( x )
# we had known earlier it will done prediction according to p(y=1)
# if we run model.predict_proba(x) it has 2 col and the 2nd one is the values of probabilities so we add [:, 1]
prob=model.predict_proba(x)
# so that we can choose all rows and col 2nd with index 1  we can observe that it will give p(y=1) values
# and those under 0.5 are predicted as 0 and 1 above it
probab = model.predict_proba(x)[:, 1]  # probability of "y=1" for each sample (row) in "X"
# evaluate the accuarcy of our model tp/total (86/100) this is not good for imbalanced ones 
model.score( x, y) # accuracy
# this sum will give us the total of those that are 1 class paitent and we can observe 34 our data is imbalnced
sum(y)

from sklearn.metrics import balanced_accuracy_score  # average of sensitivity & specificity 
balanced_accuracy_score(y,y_pred)
# change the threshold that our model has considered
y_pred = model.predict_proba(x)[:, 1] > 0.35
balanced_accuracy_score(y,y_pred)

# Cross-Validation to evaluate the model better 
from sklearn.model_selection import cross_val_score
import numpy as np
model = LogisticRegression()
# inputs are model,data,label,which score to compare
scores = cross_val_score( model, x, y, scoring="balanced_accuracy", cv=3   )
print('balanced_accuracy:',np.mean(scores))

# Standardization & Normalization to know which coef gets more vcalue & is more important in our model prediction
from scipy.stats import zscore
# we have the above synatx in scikit learn too which has longer procedure
# from sklearn.preprocessing import StandardScaler
# this will bring values between 0,1
from sklearn.preprocessing import MinMaxScaler
import copy
X2 = copy.copy(x)    # I use "copy" because if you change "X", "X2" will not be changed
# standardize mean of values in col is 0 and their std is 1
x_new = np.array(x, dtype=int)
x = zscore(x_new)    # zscore(X, axis=1) calculates zscore in rows
# normalize
scaler = MinMaxScaler()
x = scaler.fit(x).transform(x)
model = LogisticRegression()
scores = cross_val_score( model, x, y, scoring="balanced_accuracy", cv=3   )
# we can see acc comes down and had no effects on making it better
print('balanced_accuracy:',np.mean(scores))
# compare coefficients now
model = LogisticRegression()
model.fit(x, y)
# we can see systolic and smoker has an effective relationship with each other
coef = model.coef_
# we turn it back to normal because the accuracy results were better before standardization & normalization
x = copy.copy(X2)

# polynomialFeatures
from sklearn.pipeline import Pipeline
# note that we use pipeline when our analysis has multiple steps
# here 1-create the polynomial features(these new independant variables that are created from power or multiply them)
# 2-fit the model
from sklearn.preprocessing import PolynomialFeatures
# power of new variables that are created at max
degrees = [1,2,3,4,5,6,7,8,9]
for i in range(9):  #or even range(len(degrees)) iterate this loop 9 times
    polynomial_features = PolynomialFeatures(degree=degrees[i], include_bias=False)
    model = LogisticRegression() # default, solver = 'lbfgs', max_iterint = 100
    # solver parameter means the algorithm used to solve this equation default is lbfgs
    # model = LogisticRegression(solver='liblinear')
    # max number of iteration to make the time that will solve the problem more and improve it
    # model = LogisticRegression(solver='liblinear', max_iter=1000)
    pipeline = Pipeline(
        [   
            ("features", polynomial_features),
            ("model", model),
        ])
    print('degree: ',degrees[i])
    # here we might have convegence warning meaning that this model had not been solved by new parameters
    scores = cross_val_score( pipeline, x, y, scoring="balanced_accuracy", cv=3   )
    print('score:',np.mean(scores))

# Optimization
# this will choose the optimized values of logistic regression parameters
# grid search cv is a function that in the input of it gets algorithm then we say put different values 
# for an specific parameter compare them and give us the optimized value of these params
from sklearn.model_selection import GridSearchCV
pipeline = Pipeline(
    [   
        ("features", PolynomialFeatures( include_bias=False)),
        ("model", LogisticRegression()),
    ])
# which parameters to compare we should create an object of type dictionary
# ditionary is created using {}
param_grid = {
    'features__degree': [1, 2, 3, 4],
    'model__solver': ('liblinear', 'lbfgs'),
    'model__max_iter': [10, 100, 1000]
    }
# this will do cross validation itself
gs = GridSearchCV(pipeline, param_grid, scoring='balanced_accuracy', cv=3)
gs.fit(x, y)
# {'features__degree': 1, 'model__max_iter': 100, 'model__solver': 'lbfgs'}
# 'features__degree': 1 means not to use polynomial feat
print(gs.best_params_)
# best balanced accuracy
print(gs.best_score_)

# Summary
from sklearn.linear_model import LogisticRegression
import numpy as np
model = LogisticRegression()

from sklearn.model_selection import cross_val_score
# if you data is larger make the amount of cv bigger but take in mind that test part has enough test samples
scores = cross_val_score( model, x, y, scoring="balanced_accuracy", cv=3   )
print('score:',np.mean(scores))

# if you had divided your data to x_train & x_test and do not want to use cross validation
from sklearn.metrics import balanced_accuracy_score 
model.fit( X_train , y_train)
y_pred = model.predict( X_test )
balanced_accuracy_score( y_test , y_pred )
