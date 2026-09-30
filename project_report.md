# WEEK 3 PROJECT REPORT

## Student Performance Data Cleaning & Analysis using Python and Pandas

### 1. Introduction
Data collected from real-world sources may contain missing values, duplicate records,
inconsistent category names, and other quality problems. Data wrangling is the process
of transforming such raw data into a clean and useful form.

This project demonstrates data wrangling using Python, Pandas, Matplotlib, and Seaborn.

### 2. Problem Statement
The given student dataset contains missing values, a duplicate record, and inconsistent
course names. The task is to clean the dataset, filter useful records, create new
columns, and visualize the results.

### 3. Objectives
- Read a CSV file using Pandas.
- Inspect the dataset.
- Identify and handle missing values.
- Remove duplicate records.
- Standardize inconsistent course names.
- Filter students according to conditions.
- Create Result and Performance columns.
- Save the cleaned dataset.
- Create basic visualizations.

### 4. Tools and Technologies
- Python
- Pandas
- Matplotlib
- Seaborn
- CSV dataset

### 5. Dataset Description
The dataset contains:
- Student ID
- Student Name
- Age
- Gender
- Course
- Marks
- City

The input file is intentionally made messy so that data-cleaning operations can be demonstrated.

### 6. Data Cleaning Process

#### Step 1: Read CSV
`pd.read_csv()` is used to load the dataset into a Pandas DataFrame.

#### Step 2: Check Missing Values
`df.isnull().sum()` identifies the number of missing values in each column.

#### Step 3: Remove Duplicates
`df.drop_duplicates()` removes repeated records.

#### Step 4: Handle Missing Values
- Age: missing values are filled with the median.
- Marks: missing values are filled with the mean.
- City: missing values are filled with the most frequent city.

#### Step 5: Standardize Course Names
Different labels such as `AI-DS` and `Data Science` are standardized to
`AI & Data Science`.

### 7. Filtering
The project filters:
- Students who passed.
- Students scoring 75 or above.

### 8. New Columns
Two new columns are created:
- **Result:** Pass if Marks >= 40, otherwise Fail.
- **Performance:** Excellent, Good, Average, or Needs Improvement based on marks.

### 9. Visualization
Three charts are created:
1. Student Marks Bar Chart
2. Course-wise Average Marks Bar Chart
3. Pass/Fail Distribution Chart

### 10. Expected Outcome
After cleaning, the dataset contains more consistent and analysis-ready records.
The generated CSV can be reused for further analysis.

### 11. Conclusion
This project demonstrates the basic data-wrangling workflow using Python and Pandas.
Missing values and duplicate records are handled, inconsistent values are standardized,
rows are filtered, new columns are created, and the final data is visualized.

The project fulfills the Week 3 assignment requirement of cleaning a messy dataset
in Pandas, handling missing values, filtering rows, and creating new columns.

### 12. Future Scope
The project can be extended by:
- Adding more student records.
- Using real institutional data.
- Performing advanced statistical analysis.
- Creating an interactive dashboard.
- Applying machine learning to predict student performance.
