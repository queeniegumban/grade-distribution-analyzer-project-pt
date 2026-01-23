# ----------------------------
# Grade Distribution Analyzer
# ----------------------------

grades = []  # list where all input grades will be stored

print("Enter grades (type done to stop):")  # instruction for the user

# Keep asking for grades until the user types "done"
while True:
    g = input("Grade: ")      # ask the user to enter a grade
    if g == "done":           # stop when user types "done"
        break
    grades.append(int(g))    # change the input to a number and save it

# Variables to count each letter grade
a = b = c = d = f = 0

# Go through each grade and place it in a category
for g in grades:
    if g >= 90: 
        a += 1   # count A
    elif g >= 80: 
        b += 1   # count B
    elif g >= 70: 
        c += 1   # count C
    elif g >= 60: 
        d += 1   # count D
    else: 
        f += 1   # count F

# Show basic statistics
print("\nStudents:", len(grades))                 # total number of grades
print("Average:", sum(grades) / len(grades))     # average value
print("High:", max(grades), "Low:", min(grades)) # highest and lowest grade

# Show how many students are in each letter group
print("A:", a, "B:", b, "C:", c, "D:", d, "F:", f)
