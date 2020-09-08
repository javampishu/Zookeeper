init_sum = int(input())
year = 0

while init_sum < 700000:
    year_deposit = init_sum * 0.071
    init_sum = init_sum + year_deposit
    year += 1

print(year)
