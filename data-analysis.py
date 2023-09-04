'''
Created by @aruryss

GitHub: https://github.com/aruryss/CodeGirlSummer2023Analytics
'''
import pandas as pd
import seaborn as sns
import matplotlib
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
plt.style.use('ggplot')
matplotlib.rcParams['figure.figsize'] = (12, 8)

# Reading data into respective data sets
df_part = pd.read_csv(r'https://raw.githubusercontent.com/aruryss/CodeGirlSummer2023Analytics/main/datasets/participants.csv')
df_reg = pd.read_csv(r'https://raw.githubusercontent.com/aruryss/CodeGirlSummer2023Analytics/main/datasets/registered.csv')
df_inf = pd.read_csv(r'https://raw.githubusercontent.com/aruryss/CodeGirlSummer2023Analytics/main/datasets/influencers.csv')

#Filling missing values
df_reg.fillna('NA')
df_part.fillna('NA')

#Cleaning Data (time of registration timestamps) for Registered dataframe
df_reg['New_Timestamp'] = pd.to_datetime(df_reg['Timestamp']).astype('int64')/(864*10**11)
df_reg = df_reg.sort_values(by=['New_Timestamp'])

#Cleaning Data (time of registration timestamps) for Participant dataframe
df_part['New_Timestamp'] = pd.to_datetime(df_part['Timestamp']).astype('int64')/ (864*10**11)
df_part = df_part.sort_values(by=['New_Timestamp'])

#Cleaning Data (time of repost) for Influencer dataframe
df_inf['New_Timestamp'] = pd.to_datetime(df_inf['Timestamp']).astype('int64')/ (864*10**11)
df_inf = df_inf.sort_values(by=['New_Timestamp'])

#Dropping original Timestamp
df_reg.drop(['Timestamp'], axis=1)
df_part.drop(['Timestamp'], axis=1)
df_inf.drop(['Timestamp'], axis=1)

#Influencer engagement calculation
posts = ['post1', 'post2', 'post3', 'post4', 'post5', 'post6']
df_inf['Engagement'] = df_inf[posts].mean(axis=1)

#Dropping columns with amount of likes per post
df_inf.drop(columns=posts, inplace=True)
print(df_inf)

#HeatMap: Correlation between attributes of participants
df_num = df_part
for col in df_num.columns:
    if(df_num[col].dtype == 'object'):
        df_num[col] = df_num[col].astype('category')
        df_num[col] = df_num[col].cat.codes

correlation_matrix = df_num.corr(method = 'pearson', numeric_only=True)
sns.heatmap(correlation_matrix, annot = True)
plt.title('Correlation matrix between all participant attibutes')
plt.xlabel('Participant Attibutes')
plt.ylabel('Participant Attibutes')
plt.show()

#HeatMap: Correlation between attributes of applicants
df_num = df_reg
for col in df_num.columns:
    if(df_num[col].dtype == 'object'):
        df_num[col] = df_num[col].astype('category')
        df_num[col] = df_num[col].cat.codes

correlation_matrix = df_num.corr(method = 'pearson', numeric_only=True)
sns.heatmap(correlation_matrix, annot = True)
plt.title('Correlation matrix between all applicant attibutes')
plt.xlabel('Applicant Attibutes')
plt.ylabel('Applicant Attibutes')
plt.show()

#HeatMap: Correlation between attributes of instagram influencers
df_num = df_inf
for col_name in df_num.columns:
    if(df_num[col].dtype == 'object'):
        df_num[col] = df_num[col].astype('category')
        df_num[col] = df_num[col].cat.codes

correlation_matrix = df_num.corr(method = 'pearson', numeric_only=True)
sns.heatmap(correlation_matrix, annot = True)
plt.title('Correlation matrix between all influencer attibutes')
plt.xlabel('Influencer Attibutes')
plt.ylabel('Influencer Attibutes')
plt.show()

#Amount of applicants from each educational background
print('There are following amount of applicants from this educational background')
print(df_reg['Education'].value_counts().to_frame())
print('Most applicants are from: ' + str(df_reg['Education'].value_counts().idxmax()))

#Plot of acceptance rate per educational institution
acceptance_rates = {}
institutions = ['NIS', 'Ordinary School', 'BIL', 'NU', 'AITU', 'Binom', 'SDU']
for i in institutions:
    count1 = df_part['Education'].str.count(i)
    count1 = count1.fillna(0)
    count2 = df_reg['Education'].str.count(i)
    count2 = count2.fillna(0)
    acceptance_rates[i] = count1.sum() / count2.sum() * 100

df_ar = pd.DataFrame(list(acceptance_rates.items()), columns=['Institution', 'Acceptance Rate'])
print(df_ar)
custom_colors = ['#ffadad', '#ffd6a5', '#fdffb6', '#caffbf', '#9bf6ff', '#a0c4ff', '#bdb2ff']
plt.bar(df_ar['Institution'], df_ar['Acceptance Rate'], color = custom_colors)
plt.xlabel('Educational Institutions')
plt.ylabel('Acceptance Rate of Each Insitution (%)')
plt.title('Acceptance Rates by Institution')
plt.tight_layout()
plt.show()

#Plot of application amounts per day
df_reg['Traffic'] = df_reg['Traffic'].fillna('')
df_reg_insta = df_reg[df_reg['Traffic'].str.contains('Instagram')]
grouped = df_reg_insta.groupby(df_reg_insta['New_Timestamp'].astype(int)).size().reset_index(name='Count')
specific_influencer = df_inf['Influencer']

#New_Timestamp values taken from influencers' dataframe
sameke_index = 19538 #19538.546539
okdaraANDaizhokiya_index = 19542 #Aizhokiya = 19542.575012; OkDara = 19542.814595

fig, ax = plt.subplots()
for index, row in grouped.iterrows():
    x_position = row['New_Timestamp']
    if abs(row['New_Timestamp'] - sameke_index) < 1e-6:
        bar_color = '#ffc8dd'
    elif(abs(row['New_Timestamp'] - okdaraANDaizhokiya_index) < 1e-6):
        bar_color = '#cdb4db'
    else:
        bar_color = '#bde0fe'
    bar = ax.bar(x_position, row['Count'], color=bar_color)
    # Annotate the count value on top of each bar
    for rect in bar:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

ax.set_ylabel('Amount of Registered Participants')
ax.set_xlabel('Days')
ax.set_title('Applications by Date')
ax.set_xticks(grouped['New_Timestamp'])
ax.set_xticklabels([])

#Patches on the plot for each highlighted bar
sameke_patch = plt.Line2D([0], [0], marker='o', color='w', label="same.ke's repost", markerfacecolor='#ffc8dd', markersize=10)
okdaraANDaizhokiya_patch = plt.Line2D([0], [0], marker='o', color='w', label="ok.dara and aizhokiya reposts", markerfacecolor='#cdb4db', markersize=10)
other_patch = plt.Line2D([0], [0], marker='o', color='w', label='other days', markerfacecolor='#bde0fe', markersize=10)
ax.legend(handles=[sameke_patch, okdaraANDaizhokiya_patch, other_patch])

plt.tight_layout()
plt.show()

#Plot of acceptance rate per learning track
track_rates = {}
tracks = ['Frontend', 'Backend']
for i in tracks:
    count1 = df_reg['Track-chose'].str.count(i)
    count1 = count1.fillna(0)
    count2 = (df_reg['Track-chose'] == i) & (df_reg['Track-final'] == i)
    count2 = count2.fillna(0)
    track_rates[i] = count2.sum() / count1.sum() * 100

df_tr = pd.DataFrame(list(track_rates.items()), columns=['Track', 'Acceptance Rate'])
custom_colors = [ '#9bf6ff', '#bdb2ff']
plt.figure(figsize=(12, 8))
plt.bar(df_tr['Track'], df_tr['Acceptance Rate'], color = custom_colors)
plt.xlabel('Tracks')
plt.ylabel('Acceptance Rate of Each Track (%)')
plt.title('Acceptance Rates by Track')
plt.tight_layout()
plt.show()
print(df_tr)