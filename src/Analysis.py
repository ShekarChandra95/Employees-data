import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/attendance.csv")

# Convert date
df['date'] = pd.to_datetime(df['date'])

# Attendance count
status_count = df['status'].value_counts()
print(status_count)

# Plot attendance status
plt.figure()
status_count.plot(kind='bar')
plt.title("Attendance Status Distribution")
plt.xlabel("Status")
plt.ylabel("Count")
plt.savefig("images/status_distribution.png")

# Department-wise absence
absent_df = df[df['status'] == 'Absent']
dept_absent = absent_df['department'].value_counts()

plt.figure()
dept_absent.plot(kind='bar')
plt.title("Department-wise Absenteeism")
plt.xlabel("Department")
plt.ylabel("Absent Count")
plt.savefig("images/department_absent.png")

print("Analysis Completed")
