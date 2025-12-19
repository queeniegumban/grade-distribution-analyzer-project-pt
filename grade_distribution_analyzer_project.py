# ---------------------------------------
# Grade Distribution Analyzer
# Simple, beginner-friendly version
# ---------------------------------------

grades = []  # list to store all grades entered by the user

print("Enter grades (type done to stop):")

# Input loop: keep asking for grades until the user types "done"
while True:
    g = input("Grade: ")  # ask user for a grade
    if g == "done":       # stop the loop if "done" is typed
        break
    grades.append(int(g))  # convert input to integer and save it in the list

# Initialize counters for each grade category
a = b = c = d = f = 0

# Loop through all grades and sort them into categories
for g in grades:
    if g >= 90:
        a += 1  # count A grades
    elif g >= 80:
        b += 1  # count B grades
    elif g >= 70:
        c += 1  # count C grades
    elif g >= 60:
        d += 1  # count D grades
    else:
        f += 1  # count F grades

# Display overall results
print("\nTotal Students:", len(grades))          # total number of students
print("Average Grade:", sum(grades) / len(grades))  # average grade
print("Highest Grade:", max(grades))            # highest grade
print("Lowest Grade:", min(grades))             # lowest grade

# Display grade distribution
print("\nGrade Distribution:")
print("A:", a)
print("B:", b)
print("C:", c)
print("D:", d)
print("F:", f)
