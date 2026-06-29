students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

# Find all unique scores and sort them
scores = sorted(set(score for name, score in students))

# Second lowest score
second_lowest = scores[1]

# Print names in alphabetical order
for name, score in sorted(students):
    if score == second_lowest:
        print(name)