start_atoms = int(input())
fin_atoms = int(input())
i = 0

while start_atoms > fin_atoms:
    start_atoms = start_atoms // 2
    i = i + 1

days = i * 12
print(days)
