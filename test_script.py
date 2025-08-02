import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 3, 4, 5, 6]
})

# Compute correlation matrix
correlation_matrix = data.corr()

# Plot heatmap (won't display in Jenkins, but code runs)
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, linewidths=0.5)
plt.title('Correlation Matrix')
plt.savefig('correlation_matrix.png')  # Save plot as an image file

print("Script ran successfully and saved correlation_matrix.png")

