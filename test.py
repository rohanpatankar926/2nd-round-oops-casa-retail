from Vallah import Vallah

wall = {'N':0, 'S':0, 'E':0, 'W':0}

total_days = int(input("Enter total number of days of nomadic attacks --> "))
answer = 0
for i in range(total_days):
    attack_per_day = int(input("Per day attacks --> "))

    for j in range(attack_per_day):
        wall_attacked = input("Enter wall attacked (N,S,E,W) --> ")
        strength = int(input("Stregth of weapon X --> "))
        answer = answer + Vallah().attack(strength, wall_attacked, wall)
print(answer)

