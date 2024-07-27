import numpy

# Load the CSV file into NumPy
data = numpy.genfromtxt('grades.csv', delimiter=',', skip_header=1)

# Print the dataset
print("Dataset:")
print(data[:10])
print()

# Calculate and print statistics for each exam
print("Statistics for each exam:")
means = numpy.mean(data, axis=0)
medians = numpy.median(data, axis=0)
std_devs = numpy.std(data, axis=0)
mins = numpy.min(data, axis=0)
maxs = numpy.max(data, axis=0)

num_exams = data.shape[1]
for i in range(num_exams):
    print(f"Exam {i+1}:")
    print(f"Mean: {means[i]:.2f}")
    print(f"Median: {medians[i]:.2f}")
    print(f"Standard Deviation: {std_devs[i]:.2f}")
    print(f"Minimum: {mins[i]:.2f}")
    print(f"Maximum: {maxs[i]:.2f}")
    print()

# Calculate and print statistics for all exams
print("Overall statistics for all exams:")
all_grades = data.flatten()

overall_mean = numpy.mean(all_grades)
overall_median = numpy.median(all_grades)
overall_std_dev = numpy.std(all_grades)
overall_min = numpy.min(all_grades)
overall_max = numpy.max(all_grades)

print(f"Mean: {overall_mean:.2f}")
print(f"Median: {overall_median:.2f}")
print(f"Standard Deviation: {overall_std_dev:.2f}")
print(f"Minimum: {overall_min:.2f}")
print(f"Maximum: {overall_max:.2f}")
print()

# Print the number of students who passed and failed each exam
passing_grade = 60
print("Pass/fail counts for each exam:")
for i in range(num_exams):
    num_passed = numpy.sum(data[:, i] >= passing_grade)
    num_failed = data.shape[0] - num_passed
    print(f"Exam {i+1}:")
    print(f"Number Passed: {num_passed}")
    print(f"Number Failed: {num_failed}")
    print()

# Print the overall pass percentage across all exams
num_passed_overall = numpy.sum(all_grades >= passing_grade)
num_total_grades = all_grades.size

pass_percentage = (num_passed_overall / num_total_grades) * 100

print(f"Pass Percentage: {pass_percentage:.2f}%")