#!/usr/bin/env python
# coding: utf-8

# In[17]:


#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px


# In[38]:


#importing data
athletes = pd.read_excel('C:/Users/Sam/Desktop/new project/athletes.xlsx')
coaches = pd.read_excel('C:/Users/Sam/Desktop/new project/coaches.xlsx')
athletes.head()




# In[30]:


print(athletes.columns.to_list())
print(coaches.columns.to_list())


# In[31]:


print("The number of athletes that participated in Olympics 2020 is " + str(athletes.shape[0]))
print("The number of sports categories in Olympics 2020 is " + str(athletes.Discipline.nunique()))
print("The number of countries that participated in Olympics 2020 is " + str(athletes.NOC.nunique()))
print("The number of coaches present in Olympics 2020 is " + str(coaches.shape[0]))


# In[32]:


#Distribution of Athletes across different Sports
num_athletes_sportwise = athletes.pivot_table(index ='Discipline',values='Name',aggfunc=pd.Series.nunique)
num_athletes_sportwise.reset_index(inplace = True)
num_athletes_sportwise.rename(columns = {'Name':'Count of Athletes'}, inplace = True)
num_athletes_sportwise.sort_values(by =['Count of Athletes'],ascending=False, inplace = True)
fig = px.bar(num_athletes_sportwise,x = 'Discipline', y='Count of Athletes' )
fig.show()


# In[33]:


#Distribution of Athletes across Countries
num_athletes_countrywise = athletes.pivot_table(index ='NOC',values='Name',aggfunc=pd.Series.nunique)
num_athletes_countrywise.reset_index(inplace = True)
num_athletes_countrywise.rename(columns = {'Name':'Count of Athletes'}, inplace = True)
num_athletes_countrywise.sort_values(by =['Count of Athletes'],ascending=False, inplace = True)
fig = px.bar(num_athletes_countrywise,x = 'NOC', y='Count of Athletes' )
fig.show()


# In[34]:


#Distribution of Coaches across different Sport Categories
num_coaches_sportwise = coaches.pivot_table(index ='Discipline',values='Name',aggfunc=pd.Series.nunique)
num_coaches_sportwise.reset_index(inplace = True)
num_coaches_sportwise.rename(columns = {'Name':'Count of Coaches'}, inplace = True)
num_coaches_sportwise.sort_values(by =['Count of Coaches'],ascending=False, inplace = True)
fig = px.bar(num_coaches_sportwise,x = 'Discipline', y='Count of Coaches',width=800, height=400 )
fig.show()


# In[35]:


#Distribution of Coaches across different Countries
num_coaches_countrywise = coaches.pivot_table(index ='NOC',values='Name',aggfunc=pd.Series.nunique)
num_coaches_countrywise.reset_index(inplace = True)
num_coaches_countrywise.rename(columns = {'Name':'Count of Coaches'}, inplace = True)
num_coaches_countrywise.sort_values(by =['Count of Coaches'],ascending=False, inplace = True)
fig = px.bar(num_coaches_countrywise,x = 'NOC', y='Count of Coaches' )
fig.show()


# In[36]:



teams['sport_country'] = teams['Discipline']+"_"+teams['NOC'] 


# In[37]:


sport_country = teams.sport_country.unique()
athletes['sport_country']=athletes['Discipline']+"_"+athletes['NOC']
athletes['in_a_team'] = ['yes' if x in sport_country else 'no' for x in athletes['sport_country']]

df = athletes.in_a_team.value_counts().to_frame()
df.reset_index(inplace = True)
fig = px.pie(df, values='in_a_team', names='index', title='Athlete belongs to a team?',width = 400, height = 400)
fig.show()


# In[ ]:




