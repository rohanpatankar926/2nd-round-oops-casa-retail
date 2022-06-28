from Wall import Wall

class Vallah:
    def __init__(self):
        pass
    
    def attack(self,strength, wall_attacked, wall):
        self.wall_height = wall[wall_attacked]
        self.ctr = 0
        if self.wall_height<strength:
            self.ctr = self.ctr+1
            Wall().wall_update(strength, wall_attacked, wall)

        return self.ctr