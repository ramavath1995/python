odd_total = 0
even_total = 0

for i in range(0, 201):
    if i % 2 == 0:
        even_total += i
    else:
        odd_total += i

print(f"All Even number total is {even_total}")
print(f"All Odd number total is {odd_total}")
