#!/usr/bin/env python
# coding: utf-8

# # Predicting House Prices
# 
# You are working for a real estate company, and your goal is to build a predictive model to estimate house prices based on various features. You have a dataset containing information about houses, such as square footage, number of bedrooms, number of bathrooms, and other relevant attributes. You are tasked with the following:
# 
# Dataset: You can choose/download the dataset from Kaggle/UCI Repository or any other medium.

# # 1. Data Preparation:
# 
# a. Load the dataset using pandas.
# 
# b. Explore and clean the data. Handle missing values and outliers.
# 
# c. Split the dataset into training and testing sets.

# In[15]:


# a. Load the dataset using pandas.
import pandas as pd
df = pd.read_csv("data.csv")
df


# In[16]:


df.head()


# In[17]:


df.tail()


# In[18]:


df.isna().sum()


# In[20]:


df.hist()


# In[21]:


df.describe()


# In[22]:


df.head(1)


# In[31]:


feature = df.iloc[:,1:2]
feature


# In[26]:


target = df.iloc[:,:1]
target


# In[28]:


type(feature)


# In[29]:


type(target)


# In[32]:


df.corr()


# In[34]:


# c. Split the dataset into training and testing sets.
import sklearn
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(feature, target, test_size = 0.2, random_state = 2)


# In[35]:


df.shape


# # 2. Implement Simple Linear Regression:
# 
# a. Choose a feature (eg, square footage) as the independent variable (X) and house prices as the
# 
# dependent variable (y).
# 
# b. Implement a simple linear regression model using sklearn to predict house prices based on the selected feature.
# 
# c. Visualize the data and the regression line.

# In[37]:


from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()

#train the data
print('Training started....\n')
lin_reg.fit(xtrain, ytrain)
print('Training completed....\n')

#test the data
print('Testing invoked....\n')
ypred = lin_reg.predict(xtest)
print('Predicted total price....\n', ypred)
print('\nTesting is also completed.....\n')


# In[38]:


# Visualize the training dataset
import matplotlib.pyplot as plt
import seaborn as sns
plt.scatter(xtrain, ytrain, color = 'blue')
plt.plot(xtrain, lin_reg.predict(xtrain), color = 'red')
plt.title('Real estate house pricing(Training dataset)')
plt.xlabel('Area in units')
plt.ylabel('Total price')
plt.show()


# In[40]:


# Visualize the testing dataset
import matplotlib.pyplot as plt
import seaborn as sns
plt.scatter(xtest, ytest, color = 'green')
plt.plot(xtest, lin_reg.predict(xtest), color = 'red')
plt.title('Real estate house pricing(Testing dataset)')
plt.xlabel('Area in units')
plt.ylabel('Total price')
plt.show()


# # 3. Evaluate the Simple Linear Regression Model:
# 
# a. Use scikit-learn to calculate the R-squared value to assess the goodness of fit.
# 
# b. Interpret the R-squared value and discuss the model's performance. 

# In[42]:


import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score

print('Mean Squared Error: \t', mean_squared_error(ytest,ypred))
print('RMSE:\t',np.sqrt(mean_squared_error(ytest,ypred)))
print('Variance Score:\t', explained_variance_score(ytest,ypred))
print()
print('R-square:\t', r2_score(ytest,ypred))


# # 4. Implement Multiple Linear Regression:
# 
# a. Select multiple features (eg, square footage, number of bedrooms, number of bathrooms) as independent variables (X) and house prices as the dependent variable (y).
# 
# b. Implement a multiple linear regression model using scikit-learn to predict house prices based on the selected features.

# In[43]:


import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[44]:


multiple_df = pd.read_csv('data.csv')
multiple_df.head()


# In[45]:


multiple_df.isna().sum()


# In[49]:


# Converting string to numeric based data

# Label encoder
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
multiple_df['mainroad'] = le.fit_transform(multiple_df['mainroad'])
multiple_df['guestroom'] = le.fit_transform(multiple_df['guestroom'])
multiple_df['basement'] = le.fit_transform(multiple_df['basement'])
multiple_df['hotwaterheating'] = le.fit_transform(multiple_df['hotwaterheating'])
multiple_df['airconditioning'] = le.fit_transform(multiple_df['airconditioning'])
multiple_df['prefarea'] = le.fit_transform(multiple_df['prefarea'])
multiple_df['furnishingstatus'] = le.fit_transform(multiple_df['furnishingstatus'])
multiple_df.head()


# In[50]:


sns.pairplot(multiple_df)


# In[57]:


sns.boxplot(x=multiple_df['prefarea'],y=multiple_df['area'])


# In[58]:


sns.barplot(x=multiple_df['prefarea'],y=multiple_df['area'])


# In[61]:


feature1 = multiple_df.iloc[:,1:]
feature1


# In[62]:


target1 = multiple_df.iloc[:,:1]
target1


# In[68]:


from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(feature1, target1, test_size = 0.2, random_state = 1)

from sklearn.linear_model import LinearRegression
mul_reg = LinearRegression()

#train the data
print('Training started....\n')
mul_reg.fit(xtrain, ytrain)
print('Training completed....\n')

#test the data
print('Testing invoked....\n')
ypred = mul_reg.predict(xtest)
print('Predicted total price....\n', ypred)
print('\nTesting is also completed.....\n')


# # 5. Evaluate the Multiple Linear Regression Model:
# 
# a Calculate the Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE) to assess the model's accuracy.
# 
# b. Discuss the advantages of using multiple features in regression analysis.

# In[69]:


from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score

print('Mean Absolute Error: \t', mean_absolute_error(ytest,ypred))
print('Mean Squared Error: \t', mean_squared_error(ytest,ypred))
print('RMSE:\t',np.sqrt(mean_squared_error(ytest,ypred)))
print()
print('Variance Score:\t', explained_variance_score(ytest,ypred))
print('R-square:\t', r2_score(ytest,ypred))


# In[70]:


plt.figure(figsize = (10,6))
sns.heatmap(multiple_df.corr(),annot = True, vmin = -1, vmax = 1 )


# In[ ]:




