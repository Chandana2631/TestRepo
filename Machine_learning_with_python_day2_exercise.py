#!/usr/bin/env python
# coding: utf-8

# # Predicting Housing Prices with Regularized Regression
# 
# You work for a real estate analytics firm, and your task is to build a predictive model to estimate house prices based on various features. You have a dataset containing information about houses, such as square footage, number of bedrooms, number of bathrooms, and other relevant attributes. In this case study, you'll explore the application of Lasso and Ridge regression to improve the predictive performance of the model:
# 
# 1. Data Preparation:
# 
# a. Load the dataset using pandas.
# 
# b. Explore and clean the data. Handle missing values and outliers.
# 
# c. Split the dataset into training and testing sets.
# 
# 2. Implement Lasso Regression:
# 
# a. Choose a set of features (independent variables, X) and house prices as the dependent variable (y).
# 
# b. Implement Lasso regression using scikit-learn to predict house prices based on the selected features.
# 
# c. Discuss the impact of L1 regularization on feature selection and coefficients.
# 
# 3. Evaluate the Lasso Regression Model:
# 
# a. Calculate the Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE) for the Lasso regression model.
# 
# b. Discuss how the Lasso model helps prevent overfitting and reduces the impact of irrelevant features.
# 
# 4. Implement Ridge Regression:
# 
# a. Select the same set of features as independent variables (X) and house prices as the dependent
# 
# variable (y) b. Implement Ridge regression using scikit-learn to predict house prices based on the selected
# 
# . Explain how 12 regularization in Ridge regression differs from L1 regularization in Lasso
# 
# 5. Evaluate the Ridge Regression Model:
# 
# a. Calculate the MAE, MSE, and RMSE for the Ridge regression model.
# 
# b. Discuss the benefits of Ridge regression in handling multicollinearity among features and its Impact on the model's coefficients.
# 
# 6. Model Comparison:
# 
# a. Compare the results of the Lasso and Ridge regression models.
# 
# b. Discuss when it is preferable to use Lasso, Ridge, or plain linear regression.
# 
# 7. Hyperparameter Tuning:
# 
# a. Explore hyperparameter tuning for Lasso and Ridge, such as the strength of regularization, and discuss how different hyperparameters affect the models.
# 
# 8. Model Improvement:
# 
# a. Investigate any feature engineering or data preprocessing techniques that can enhance the performance of the regularized regression models.
# 
# 9. Conclusion:
# 
# a. Summarize the findings and provide insights into how Lasso and Ridge regression can be valuable tools for estimating house prices and handling complex datasets.
# 
# 10. Presentation:
# 
# a. Prepare a presentation or report summarizing your analysis, results, and recommendations, particularly focusing on the advantages and limitations of using regularized regression techniques in real estate prediction.
# 
# In this case study, you are required to demonstrate your ability to preprocess data, implement Lasso and Ridge regression models, evaluate their performance, and make recommendations for improving the models. This case study should assess your knowledge of regularized regression techniques and how to select and tune hyperparameters for these models.

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


#Load the dataset
data=pd.read_csv("Housing.csv")
data


# In[3]:


data.isna().sum()


# In[8]:


x=data.iloc[:,1:4]
x.head()


# In[9]:


y=data.iloc[:,:1]
y.head()


# In[10]:


import sklearn
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=2)


# In[11]:


data.shape


# In[19]:


#Lasso Regression
from sklearn.linear_model import Lasso
print("*******ridge Regression*******")
ll=Lasso(alpha=0.01)

print()
print("Training Started....\n")
ll.fit(xtrain,ytrain)
print()
ll_pred=ll.predict(xtest)
print("predicted values",ll_pred)
print("Lasso Train_score:\t",ll.score(xtrain,ytrain))
print()
print("Lasso Test Score: \t",ll.score(xtest,ytest))
print()
print('Lasso R-Square: \t',r2_score(ytest,ll_pred))


# In[22]:


from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score
print("Mean Absolute Error: \t",mean_absolute_error(ytest,ll_pred))
print()
print("Mean Squared Error: \t",mean_squared_error(ytest,ll_pred))
print()
print("RMSE: \t",np.sqrt(mean_squared_error(ytest,ll_pred)))
print()
print("Variance Score: \t",explained_variance_score(ytest,ll_pred))
print()


# In[20]:


from sklearn.linear_model import LinearRegression
base_reg=LinearRegression()
print("*******Base Regression*******")
print()
print("Training Started....\n")
base_reg.fit(xtrain,ytrain)
print()
base_pred=base_reg.predict(xtest)

from sklearn.metrics import r2_score
print("Base Train_score:\t",base_reg.score(xtrain,ytrain))
print()
print("Base Test Score: \t",base_reg.score(xtest,ytest))
print()
print('R-Square: \t',r2_score(ytest,ll_pred))


# In[15]:


from sklearn.linear_model import Ridge
print("*******ridge Regression*******")
rr=Ridge(alpha=0.01)

print()
print("Training Started....\n")
rr.fit(xtrain,ytrain)
print()
rr_pred=rr.predict(xtest)
print("predicted values",rr_pred)
print("Ridge Train_score:\t",rr.score(xtrain,ytrain))
print()
print("Ridge Test Score: \t",rr.score(xtest,ytest))
print()
print('Ridge R-Square: \t',r2_score(ytest,rr_pred))


# In[23]:


from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score
print("Mean Absolute Error: \t",mean_absolute_error(ytest,rr_pred))
print()
print("Mean Squared Error: \t",mean_squared_error(ytest,rr_pred))
print()
print("RMSE: \t",np.sqrt(mean_squared_error(ytest,rr_pred)))
print()
print("Variance Score: \t",explained_variance_score(ytest,rr_pred))
print()
#print("R-Square: \t",r2_score(ytest,ypred))


# # Diagnosing and Remedying Heteroscedasticity and Multicollinearity
# 
# You are working as a data analyst for a company that aims to predict employee performance based on
# 
# various factors such as experience, education level, and the number of projects completed. You've built a linear regression model, but you suspect it may be suffering from issues related to heteroscedasticity and multicollinearity. Your task is to diagnose and address these problems:
# 
# 1. Initial Linear Regression Model:
# 
# a. Describe the dataset and the variables you're using for predicting employee performance.
# 
# b. Implement a simple linear regression model to predict employee performance.
# 
# c. Discuss why linear regression is a suitable choice for this prediction problem.
# 
# 2. Identifying Heteroscedasticity:
# 
# a. Explain what heteroscedasticity is in the context of linear regression.
# 
# b. Provide methods for diagnosing heteroscedasticity in a regression model.
# 
# c. Apply these diagnostic methods to your model's residuals and report your findings.
# 
# 3. Remedying Heteroscedasticity:
# 
# a. Discuss the potential consequences of heteroscedasticity on your regression model.
# 
# b. Suggest ways to address heteroscedasticity, such as transforming variables or using weighted least squares regression.
# 
# c. Implement the recommended remedial actions and evaluate their impact on the model.
# 
# 4. Detecting Multicollinearity:
# 
# a. Explain what multicollinearity is and how it can affect a linear regression model.
# 
# b. Use correlation matrices or variance inflation factors (VIFS) to identify multicollinearity in your predictor variables.
# 
# c. Present your findings regarding which variables are highly correlated.
# 
# 5. Mitigating Multicollinearity:
# 
# a. Discuss the potential issues associated with multicollinearity and its impact on model interpretability.
# 
# b. Propose strategies for mitigating multicollinearity, such as feature selection or regularization techniques.
# 
# c. Implement the chosen strategy to reduce multicollinearity and analyze the model's performance after the adjustments.
# 
# 6. Model Evaluation:
# 
# a. Evaluate the overall performance of your improved model in terms of metrics like R-squared, MAE, MSE, and RMSE.
# 
# b. Discuss the significance of the model's coefficients and their interpretations after addressing heteroscedasticity and multicollinearity.
# 
# 7. Conclusion:
# 
# a Summarize the impact of identifying and addreccing heteroscedacticity and multicollinearityon the predictive accuracy and interpretability of your employee performance model.
# 
# b. Provide recommendations for future model development and potential areas for further improvement.
# 
# In this case study, you are expected to demonstrate your knowledge of linear regression, the ability to diagnose and address heteroscedasticity and multicollinearity issues, and how these actions can enhance the quality of a predictive model. This case study should assess your expertise in applying statistical techniques and data analysis in real-world scenarios.

# In[ ]:




