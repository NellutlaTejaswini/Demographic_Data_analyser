import pandas as pd

# Load the dataset into a Pandas DataFrame
# Replace 'your_dataset.csv' with the actual filename or path to your dataset
df = pd.read_csv('your_dataset.csv')

# How many people of each race are represented in this dataset?
race_counts = df['race'].value_counts()

# What is the average age of men?
average_age_men = df[df['sex'] == 'Male']['age'].mean()

# What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100

# What percentage of people with advanced education make more than 50K?
higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
percentage_higher_education_rich = (higher_education['salary'] == '>50K').mean() * 100

# What percentage of people without advanced education make more than 50K?
lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
percentage_lower_education_rich = (lower_education['salary'] == '>50K').mean() * 100

# What is the minimum number of hours a person works per week?
min_work_hours = df['hours-per-week'].min()

# What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
num_min_workers = df[df['hours-per-week'] == min_work_hours]
rich_percentage_min_workers = (num_min_workers['salary'] == '>50K').mean() * 100

# What country has the highest percentage of people that earn >50K and what is that percentage?
highest_earning_country = df[df['salary'] == '>50K']['native-country'].value_counts().idxmax()
highest_earning_country_percentage = (df[(df['native-country'] == highest_earning_country) & (df['salary'] == '>50K')].shape[0] / df[df['native-country'] == highest_earning_country].shape[0]) * 100

# Identify the most popular occupation for those who earn >50K in India.
top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

# Print the results
print("Race Counts:")
print(race_counts)
print("\nAverage Age of Men:", round(average_age_men, 1))
print("\nPercentage with Bachelors:", round(percentage_bachelors, 1))
print("\nPercentage with Advanced Education and Earning >50K:", round(percentage_higher_education_rich, 1))
print("\nPercentage without Advanced Education and Earning >50K:", round(percentage_lower_education_rich, 1))
print("\nMinimum Work Hours per Week:", min_work_hours)
print("\nPercentage of Min Workers Earning >50K:", round(rich_percentage_min_workers, 1))
print("\nHighest Earning Country:", highest_earning_country)
print("\nPercentage of People Earning >50K in", highest_earning_country, ":", round(highest_earning_country_percentage, 1))
print("\nMost Popular Occupation for >50K Earners in India:", top_IN_occupation)
