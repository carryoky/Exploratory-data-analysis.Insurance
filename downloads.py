#!/usr/bin/env python
# coding: utf-8

# In[49]:


import pandas as pd
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
df = pd.read_csv('/home/sam/Downloads/insurance.csv')
df.head()


# In[5]:


df.info()
df.describe()


# In[6]:


df.duplicated().sum()


# In[9]:


df['sex'].unique()

df['region'].unique()

df['smoker'].unique()


# In[22]:


df.isnull().sum()


# In[23]:


df.dtypes


# In[24]:


df[df['age']==21].head()


# In[50]:


import warnings
warnings.filterwarnings('ignore')
df.corr()


# In[51]:


import warnings
warnings.filterwarnings('ignore')
sns.heatmap(df.corr())


# In[32]:


df.age.describe()


# In[33]:


sns.pairplot(df)


# In[40]:


import matplotlib.pyplot as plt
sns.catplot(x="age", y="charges", data=df, kind="bar", aspect=2.0)
plt.title("Bar graph plot for age vs charges")
plt.show()


# In[53]:


df.nunique()


# In[57]:


sns.displot(df, x="age")


# In[ ]:




