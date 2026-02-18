Data Engineer Certification Sample Practical Exam
HappyPaws, creates fun and educational apps for pet owners.

HappyPaws wants to help pet owners understand their pets better by tracking their activities and health through the app.

The data engineering team is responsible for making sure all the pet data from thousands of users is organized and safe, so pet owners can get tips to keep their pets happy and healthy.

Task
HappyPaws has collected three datasets over the past year:

"pet_activities.csv" which logs daily activities of pets,
"pet_health.csv" which records vet visits and health issues, and
"users.csv" which contains information about the pet owners.
Each dataset contains unique identifiers for pets and/or their owners.

The engineers developing the app currently write code to cross reference all of these data sources.

They want to make things easier by having a single table with all data included.

Your manager has asked you to write a Python function that cleans and merges these datasets into a single dataset.

The final dataset should provide a comprehensive view of each pet's activities, health records, and owner information.

To test your code, your manager will run only the code all_pet_data('pet_activities.csv', 'pet_health.csv', 'users.csv')
Your all_pet_data() function must return a DataFrame, with columns as described below.
All columns must accurately match the descriptions provided below, including names.
Data
The data that has been provided has the following structure

image

The function that you write must return data as described below. There should be a unique row for each activity/health visit.

Where missing values are permitted, they should be in the default Python format.

Column Name	Description
pet_id	Unique identifier for each pet. There should not be any missing values.
date	The date of the activity recorded or the date of the health visit, in date format. There should not be any missing values.
activity_type	The type of activity, one of 'Walking', 'Playing', 'Resting' or for rows that relate to a health visit, the value 'Health'. Missing values are permitted.
duration_minutes	The duration of the activity in minutes. For rows that relate to health visits, this should be 0. Missing values for other activities are permitted.
issue	The health issue identified or check-up note. For rows that relate to activities, this should be a missing value. Missing values for health activities are permitted.
resolution	The outcome or advice given for the issue. For rows that relate to activities, this should be a missing value. Missing values for health activities are permitted.
owner_id	Unique identifier for the pet owner. All pets must have an owner.
owner_age_group	The age group of the owner (e.g., 18-25, 26-35, etc.). Missing values are permitted.
pet_type	The type of pet (e.g., Dog, Cat). Missing values are permitted.