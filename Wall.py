class Wall:
    def __init__(self):
        pass
    
    def wall_update(self,Strength, wall_attacked, wall):
        wall[wall_attacked] = Strength
        return wall