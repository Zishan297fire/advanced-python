import seaborn as sns
import matplotlib as plt

tips = sns.load_dataset("tips")
print("First Five Rows:")
print(tips.head())
print("\nDataset Information:")
print(tips.info())

print("\nStatistical Summary:")
print(tips.describe())
plt.figure(figsize=(8, 5))
sns.barplot(data=tips, x="day", y="total_bill")
plt.title("Average Restaurant Bill by Day")
plt.show()
plt.figure(figsize=(8, 5))
sns.countplot(data=tips, x="day", hue="sex")
plt.title("Number of Customers by Day and Gender")
plt.show()
plt.figure(figsize=(8, 5))
sns.boxplot(data=tips, x="day", y="total_bill")
plt.title("Restaurant Bill Distribution by Day")
plt.show()
plt.figure(figsize=(8, 5))
sns.stripplot(data=tips, x="day", y="tip", jitter=True)
plt.title("Tips Given on Different Days")
plt.show()


# 5. SWARM PLOT
plt.figure(figsize=(8, 5))
sns.swarmplot(data=tips, x="day", y="total_bill")
plt.title("Customer Bills by Day")
plt.show()


# 6. JOINT PLOT
sns.jointplot(data=tips, x="total_bill", y="tip", kind="scatter")
plt.suptitle("Relationship Between Total Bill and Tip")
plt.show()


# 7. PAIR PLOT
sns.pairplot(tips, hue="sex")
plt.suptitle("Pair Plot of Restaurant Dataset")
plt.show()


# 8. POINT PLOT
plt.figure(figsize=(8, 5))
sns.pointplot(data=tips, x="day", y="tip", hue="sex")
plt.title("Average Tip by Day and Gender")
plt.show()


# 9. LINEAR REGRESSION PLOT (LM PLOT)
sns.lmplot(data=tips, x="total_bill", y="tip", hue="sex")
plt.title("Relationship Between Bill and Tip")
plt.show()

print("\nRestaurant Bill Explorer Completed!")
