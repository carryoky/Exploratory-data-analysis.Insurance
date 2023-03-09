# Exploratory-data-analysis.Insurance
Exploratory data analysis (EDA) is an especially important activity in the routine of a data analyst or scientist.It enables an in depth understanding of the dataset, define or discard hypotheses and create predictive models on a solid basis.It uses data manipulation techniques and several statistical tools to describe and understand the relationship between variables and how these can impact business.In fact, it’s thanks to EDA that we can ask ourselves meaningful questions that can impact business.

## Required libraries for EDA
Before starting, let’s see what are the fundamental libraries required to carry out the EDA. There are many useful libraries but here we will only see the ones that this template leverages.
```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
```
## Steps
### 1.Importing a working dataset
Importing a dataset is simple with Pandas through functions dedicated to reading the data. If our dataset is a .csv file, we can just use
```python
df = pd.read_csv('/home/sam/Downloads/insurance.csv')
```
### 2.Understanding the problem
In this first phase, our goal is to understand what we are looking at, but without going into detail.
```python
df.head()
df.info()
df.describe()
```
### 3.Preparation of the data
At this stage we want to start cleaning our dataset in order to continue the analysis.Let’s see how to apply these ideas to our dataset.

-All the variables appear to be physical-chemical measures. This means they could all be useful and help define the segmentation of the type of wine. We have no reason to remove columns
-To check for duplicate rows we can use .isduplicated().sum()— this will print us the number of duplicated rows in our dataset
```python
df.duplicated().sum()
df['sex'].unique()

df['region'].unique()

df['smoker'].unique()
df.isnull().sum()
```
### 4.Understanding of the variables
While in the previous point we are describing the dataset in its entirety, now we try to accurately describe all the variables that interest us. For this reason, this step can also be called univariate analysis.
```python
df.dtypes
df[df['age']==21].head()
df.corr()
```
### 5.Study of relationships between variables
Now the idea is to find interesting relationships that show the influence of one variable on the other, preferably on the target.
We can start exploring relationships with the help of Seaborn and pairplot.
```python
sns.pairplot(df)
```
Now let’s see how Seaborn can again help us expand our exploration thanks to the heatmap. We are going to create a correlation matrix with Pandas and to isolate the most correlated variables.
```python
sns.heatmap(df.corr())
```
## Conclusion
The process described so far is iterative in its nature. In fact, the exploratory analysis goes on until we have answered all the business questions.

It is impossible for me to show or demonstrate all the possible techniques of data exploration —we don’t have specific business requirements or valid real-world dataset. However, I can convey to the reader the importance of applying a template like the following to be efficient in the analysis.







