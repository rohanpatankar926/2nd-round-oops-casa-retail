from Vallah import Vallah

class Test:
    def __init__(self):
        pass
    
    def main(self):
        self.wall = {'N':0, 'S':0, 'E':0, 'W':0}

        self.total_days = int(input("Enter total number of days of nomadic attacks --> "))
        self.answer = 0
        for i in range(self.total_days):
            self.attack_per_day = int(input("Per day attacks --> "))

            for j in range(self.attack_per_day):
                self.wall_attacked = input("Enter wall attacked (N,S,E,W) --> ")
                self.strength = int(input("Stregth of weapon X --> "))
                self.answer = self.answer + Vallah().attack(self.strength, self.wall_attacked, self.wall)
        print (self.answer)

if __name__=="__main__":
    Test().main()        