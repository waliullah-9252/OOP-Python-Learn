num = [23,43,55,22,15,24,66]
odds=[]
for n in num:
    if n % 2 == 1 and n % 5 == 0:
        odds.append(n)

print(odds)

# odds_num = [n for n in num if n % 2 == 1]
odds_num = [n for n in num if n % 2 == 1 if n % 5 == 0]
print(odds_num)

players = ['Virat','Tamim','Rohit']
ages = [35,34,38]
age_comb = []
for player in players:
    print(player)
    for age in ages:
        print(player,age)
        age_comb.append([player,age])
print(age_comb)
age_comb2 = [[player,age] for player in players for age in ages]
print(age_comb2)
