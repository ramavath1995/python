heights = input("Enter all students heights separated by space: ").split()

total = 0
for i in heights:
    total += int(i)

average = total / len(heights)
print(f"Average of {len(heights)} students is {average}")
