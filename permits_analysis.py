import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load the dataset, make it into a DataFrame(df)
df = pd.read_csv('college park residential and commercial permits 2013-2023 .csv')
#Print the DataFrame(df) and information about it
print(df)
print(df.head())
print(df.info())
#For a full overview of all columns, including categorical
print(df.describe(include='all')) 
print(df.nunique())
print(df['Permit Type'].value_counts())

#Median cost. First convert to numeric and remove commas
df['Expected Construction Cost'] = df['Expected Construction Cost'].replace(',', '', regex=True).astype(float)
#Calculate the median
median_cost = df['Expected Construction Cost'].median()
median_cost


#Put into datetime type
df['Permit Issuance Date'] = pd.to_datetime(df['Permit Issuance Date'])

#Bar plot of permits by year. First extract year
df['Permit Case Year'] = df['Permit Issuance Date'].dt.year
# Bar Plot
permits_by_year = df['Permit Case Year'].value_counts().sort_index()
permits_by_year.plot.bar(title= 'Permits Issued Per Year', x = 'Permit Case Year', ylabel = 'Number of Permits')
plt.tight_layout()
plt.show()

#Zoning Shifts using Permit Type
#Count permits by perit type for each year
zoning_proxy = df.groupby(['Permit Case Year', 'Permit Type']).size().unstack(fill_value=0)

#Seaborn Plot: First reset index and prepare for Seaborn plot
zoning_long = zoning_proxy.reset_index().melt(id_vars='Permit Case Year', var_name='Permit Type', value_name='Permit Count')

#Seaborn Plot
plt.figure(figsize=(12,6))
sns.lineplot(data=zoning_long, x='Permit Case Year', y='Permit Count', hue='Permit Type', marker='o')
plt.title('Permit Type Trends Over Time')
plt.xlabel('Year')
plt.ylabel('Permit Count')
plt.legend(title='Permit Type', bbox_to_anchor=(1.6, 1), loc='upper right')
plt.tight_layout()
plt.show()
