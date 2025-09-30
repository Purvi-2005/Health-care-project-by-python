   #project name
# description of project
#data precaurment 
#data sample (landscape)
#data regularities
#cleaning steps
#metrices (m1,m2)
#plots (p1,p2)
# insight & proves
#summary

#pip install virtualenv
#python -m venv venv
#venv\Scripts\activate.bat
# pip install matplotlib





import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# 1. Load data
df = pd.read_csv("healthcare_dataset.csv")
print("First Fifty rows of dataset.")
print(df.head(50), "\n")
print("=== Cleaned Columns ====")
print(df.columns, "\n")


# Fixing Gender column
#df['Gender'] = df['Gender'].map({0 : 'Male', 1 : 'Female'})

# Fixing Admission Type column
#df['Admission Type'] = df['Admission Type'].map({0 : "Urgent", 1 : "Emergency",2:"Elective"})

# Fixing Medication column
#df['Medication'] = df['Medication'].map({0 : "Paracetamol", 1 : "Ibuprofen",2 : "Aspirin",3 : "Penicillin",4 : "Lipitor"})

# Basic Stats
print("==== Summary Stats =====")
print(df.describe(), "\n")

print("==== Value Count ====")
print("Gender : \n ",df['Gender'].value_counts(), "\n")
print(" Blood Type \n ", df['Blood Type'].value_counts(), "\n")
print("Medical Condition: \n ", df['Medical Condition'].value_counts(), "\n")
print("Insurance Provider: \n ",df['Insurance Provider'].value_counts(), "\n")

print("Medication: \n ", df['Medication'].value_counts(), "\n")
print("Test Results: \n ", df['Test Results'].value_counts(), "\n")

#print(" Admission Type: \n ", df[' Admission Type'].value_counts(), "\n")

# Vizulization

#plot 1 : Age Distribution
plt.figure(figsize=(6, 4))
plt.subplot(2, 2, 1)
sns.histplot(df['Age'], bins=15, kde=True, color="skyblue")
plt.title("Age Distribution of Patients")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

#plot 2: gender vs test results
plt.figure(figsize=(6, 4))
plt.subplot(2, 2, 2)
sns.boxplot(x="Gender", y="Test Result",data=df,palette="pastel")
sns.boxplot(x="Gender", y="Test Result",data=df,palette="pastel")
plt.title("Test Result by Gender ")
plt.show()


#plot 3: Blood Type Count 
plt.figure(figsize=(6, 4)) 
plt.subplot(2, 2, 3)
sns.countplot(x="Blood Type", data=df, palette="pastel")
plt.title(" Blood Type  Distribution ")

#plot 4: Medical Condition by gender
plt.figure(figsize=(7, 4))
plt.subplot(2, 2, 4)
sns.countplot(x=" Medical Condition", hue= "Gender", data=df, palette="coolwarm")
plt.title(" Medical Condition by gender")
plt.show()
