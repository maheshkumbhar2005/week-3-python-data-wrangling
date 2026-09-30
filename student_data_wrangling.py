# Week 3: Python & Data Wrangling Project
# Project: Student Performance Data Cleaning & Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Read CSV
df = pd.read_csv("messy_students.csv")

print("\n--- Original Dataset ---")
print(df)

# 2. Basic inspection
print("\n--- Dataset Information ---")
print(df.info())

print("\n--- Missing Values ---")
print(df.isnull().sum())

# 3. Remove duplicate rows
df = df.drop_duplicates()

# 4. Handle missing values
# Fill Age with the median age
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Marks with the mean marks
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Fill missing City with the most frequent city
df["City"] = df["City"].fillna(df["City"].mode()[0])

# 5. Standardize course names
df["Course"] = df["Course"].replace({
    "AI-DS": "AI & Data Science",
    "AI-ML": "AI & Machine Learning",
    "Data Science": "AI & Data Science"
})

# 6. Create a new Result column
df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

# 7. Create a new Performance column
def performance(marks):
    if marks >= 75:
        return "Excellent"
    elif marks >= 60:
        return "Good"
    elif marks >= 40:
        return "Average"
    else:
        return "Needs Improvement"

df["Performance"] = df["Marks"].apply(performance)

# 8. Filter rows
passed_students = df[df["Result"] == "Pass"]
high_scorers = df[df["Marks"] >= 75]

print("\n--- Cleaned Dataset ---")
print(df)

print("\n--- Passed Students ---")
print(passed_students[["Name", "Course", "Marks", "Result"]])

print("\n--- High Scorers (75+) ---")
print(high_scorers[["Name", "Marks", "Performance"]])

# 9. Save cleaned dataset
df.to_csv("cleaned_students.csv", index=False)

# 10. Basic analysis
print("\n--- Summary Statistics ---")
print(df[["Age", "Marks"]].describe())

print("\nAverage Marks:", round(df["Marks"].mean(), 2))
print("Number of Students:", len(df))
print("Number of Passed Students:", len(passed_students))
print("Pass Percentage:", round((len(passed_students) / len(df)) * 100, 2), "%")

# 11. Visualization - Marks by Student
plt.figure(figsize=(10, 5))
sns.barplot(data=df, x="Name", y="Marks")
plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("student_marks.png", dpi=150)
plt.show()

# 12. Visualization - Course-wise average marks
course_avg = df.groupby("Course", as_index=False)["Marks"].mean()

plt.figure(figsize=(9, 5))
sns.barplot(data=course_avg, x="Course", y="Marks")
plt.title("Average Marks by Course")
plt.xlabel("Course")
plt.ylabel("Average Marks")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("course_average_marks.png", dpi=150)
plt.show()

# 13. Visualization - Result distribution
plt.figure(figsize=(6, 5))
sns.countplot(data=df, x="Result")
plt.title("Pass/Fail Distribution")
plt.xlabel("Result")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("result_distribution.png", dpi=150)
plt.show()

print("\nProject completed successfully.")
