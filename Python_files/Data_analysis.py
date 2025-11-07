import numpy as np
import pandas as pd

np.random.seed(42)

# use np.arange (not np.arrange)
hours_studied = np.arange(1, 21)

# generate exam scores with a bit of noise
exam_score = 40 + 100 * hours_studied + np.random.normal(0, 10, 20)

# use curly braces {} for dict, not parentheses ()
df = pd.DataFrame({
    'Hours_Studied': hours_studied,
    'Exam_Score': exam_score
})

print(df.head())
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate the data
np.random.seed(42)
hours_studied = np.arange(1, 21)
exam_score = 40 + 5 * hours_studied + np.random.normal(0, 5, 20)

# Put it in a DataFrame
df = pd.DataFrame({
    'Hours_Studied': hours_studied,
    'Exam_Score': exam_score
})

# Plot the data
plt.figure(figsize=(8, 5))  # size of the chart
plt.scatter(df['Hours_Studied'], df['Exam_Score'], color='blue', label='Data points')
plt.title('Exam Score vs Hours Studied')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.legend()
plt.grid(True)
plt.show()