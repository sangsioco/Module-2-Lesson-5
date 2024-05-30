# Task 1 Code a function to calculate the average grade
def calculate_average_grade(grades):
    if not grades:
        return None
    total = sum(grades)
    return total / len(grades)

grades = [85, 92, 78, 90, 65, 88, 72, 95, 60, 83]
average_grade = calculate_average_grade(grades)
print("Average Grade:", average_grade)

# Task 2 Implement a function to find the highest and lowest grade
def find_highest_and_lowest_grade(grades):
    if not grades:
        return None, None
    highest_grade = max(grades)
    lowest_grade = min(grades)
    return highest_grade, lowest_grade

grades = [85, 92, 78, 90, 65, 88, 72, 95, 60, 83]
highest_grade, lowest_grade = find_highest_and_lowest_grade(grades)
print("Highest Grade:", highest_grade)
print("Lowest Grade:", lowest_grade)

# Task 3 Create a feature that categorizes grades into letter grades (A, B, C, etc.)
def categorize_grades(grades):
    if not grades:
        return {}
    letter_grades = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for grade in grades:
        if grade >= 90:
            letter_grades['A'] += 1
        elif grade >= 80:
            letter_grades['B'] += 1
        elif grade >= 70:
            letter_grades['C'] += 1
        elif grade >= 60:
            letter_grades['D'] += 1
        else:
            letter_grades['F'] += 1
    return letter_grades

grades = [85, 92, 78, 90, 65, 88, 72, 95, 60, 83]
letter_grades = categorize_grades(grades)
print("Letter Grades:")
for grade, count in letter_grades.items():
    print(f"{grade}: {count}")