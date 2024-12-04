import numpy as np

# Creating an array of scores
student_scores = np.array([85, 90, 78, 92, 88])

# 1. Converting to float type
float_scores = student_scores.astype(float)
print("Scores as float type:", float_scores)

# 2. Adding 5 points to a copy of the original scores
modified_scores = student_scores.copy()
modified_scores += 5
print("Modified scores (after adding 5):", modified_scores)
print("Original scores remain intact:", student_scores)

# 3. Identifying scores 85 or higher
high_scores_indices = np.where(student_scores >= 85)[0]
print("Indices with scores of 85 or higher:", high_scores_indices)

# 4. Array properties and summary statistics
print("Array shape:", student_scores.shape)
print("Number of dimensions:", student_scores.ndim)
print("Total number of elements:", student_scores.size)
print("Size of each item in bytes:", student_scores.itemsize)
print("Array data type:", student_scores.dtype)

# Sorting and statistical operations
print("Sorted scores:", np.sort(student_scores))
print("Highest score:", student_scores.max())
print("Lowest score:", student_scores.min())
print("Total score sum:", student_scores.sum())
print("Average score:", student_scores.mean())

# Slicing operations
print("Scores from index 0, 2, 4:", student_scores[::2])
print("Scores from 2nd to 4th element:", student_scores[-3:-1])
print("Scores from index 1 to 3:", student_scores[1:4])
