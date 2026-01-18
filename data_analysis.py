import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "student_scores.csv")
data = pd.read_csv(csv_path)

print("Dataset:\n", data)

math_avg = data["Math_Score"].mean()
science_avg = data["Science_Score"].mean()
english_avg = data["English_Score"].mean()

subjects = ["Math", "Science", "English"]
averages = [math_avg, science_avg, english_avg]

plt.figure()
plt.bar(subjects, averages)
plt.title("Average Scores by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Score")
plt.show()

plt.figure()
plt.scatter(data["Math_Score"], data["Science_Score"])
plt.title("Math vs Science Scores")
plt.xlabel("Math Score")
plt.ylabel("Science Score")
plt.show()

correlation = data.corr()

plt.figure()
plt.imshow(correlation)
plt.colorbar()
plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=45)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title("Correlation Heatmap")
plt.show()
