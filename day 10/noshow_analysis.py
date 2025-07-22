import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("noshowappointments.csv")
df_raw = df.copy()
print(df.columns)
df.head()

# Drop AppointmentID
df.drop(columns=['AppointmentID'], inplace=True, errors='ignore')

# Rename columns
df.rename(columns={
    'Hipertension':'Hypertension',
    'Handcap':'Handicap',
    'SMS_received':'SMSReceived',
    'No-show':'NoShow'
}, inplace=True)

df.head()

print("Nulls before:")
print(df_raw.isnull().sum())

print("Nulls before:")
print(df_raw.isnull().sum())

df.drop_duplicates(inplace=True)
df.drop_duplicates

df["Gender"] = df["Gender"].map({"F":0, "M":1})
df.head()

df["NoShow"] = (df["NoShow"] == "Yes").astype(int)
df.head()
df["ScheduledDay"] = pd.to_datetime(df["ScheduledDay"]) # convert day into datetime
df["AppointmentDay"] = pd.to_datetime(df["AppointmentDay"]).dt.normalize() 
df.head()

# Feature Engineering
df["WaitDays"] = (df["AppointmentDay"] - df["ScheduledDay"]).dt.days.clip(lower=0) ## lower=0 means remove any negative values
df["ApptDayOfWeek"] = df["AppointmentDay"].dt.day_name()
df.head()

print("\n✅ Cleaned Data Summary:")
print(df.info())

#1. Age Distribution
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
sns.histplot(df_raw["Age"], kde=True)
plt.title("Age Distribution - Before Cleaning")

plt.subplot(1,2,2)
sns.histplot(df["Age"], kde=True)
plt.title("Age Distribution - After Cleaning")
plt.show()

# 2. NoShow Rate by Gender
df["Gender"] = df["Gender"].map({0:"F", 1:"M"})
plt.figure(figsize=(8,4))
sns.barplot(x="Gender", y="NoShow", data=df)
plt.title("No-Show Rate by Gender (0=F, 1=M)")
plt.show()

# Histogram of wait days
plt.figure(figsize=(10,5))
sns.histplot(df["WaitDays"], bins=30, kde=True)
plt.title("Distribution of Wait Days")
plt.xlabel("Wait Days")
plt.ylabel("Count")
plt.show()

#3.Wait Days vs NoShow
plt.figure(figsize=(10,4))
sns.boxplot(x="NoShow", y="WaitDays", data=df)
plt.title("Wait Days vs NoShow")
plt.show()

#4. Day of Week vs NoShow
plt.figure(figsize=(10,4))
sns.barplot(x="ApptDayOfWeek", y="NoShow", data=df)
plt.title("No-Show Rate by Day of Week")
plt.xticks(rotation=45)
plt.show()

