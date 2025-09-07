#The monotonically increasing subsequence problem is developed to identify the longest sequence of continuously increasing integers in a string
#Take a chance, apply for the rhodes scholarship
#talk to recommenders, and ask them for a potential recommendartion
#schedule a meeting with four, and talk to them about it
#if they tell me no. tell them I'll do it anyway
import matplotlib.pyplot as plt

# Sample data
precision = [0.9554, 0.9494, 0.9375, 0.9554, 0.9375, 0.9375, 0.9434, 0.9434, 0.9554, 0.9202]
recall = [0.9740, 0.9677, 0.9494, 0.9615, 0.9494, 0.9434, 0.9740, 0.9677, 0.9740, 0.9375]

# Compute averages
mean_recall = sum(recall) / len(recall)
mean_precision = sum(precision) / len(precision)

# Create scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(recall, precision, s=100, alpha=0.7, label='Data Points')
plt.scatter(mean_recall, mean_precision, color='red', s=150, label='Mean Point')

# Add labels and title
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Recall vs Precision Scatter Plot')
plt.grid(True)
plt.legend()

# Show plot
plt.show()

print(mean_recall)
print(mean_precision)