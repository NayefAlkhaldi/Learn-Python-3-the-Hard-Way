class Entity(object):
    def __init__(self, health, ap): # ap -> attack power
        self.health = health
        self.max_health = health
        self.ap = ap
    
    def attack(self, health):
        damage = round(health - self.ap)
        print(f"YOUR HEALTH: {damage}")
        return damage

    def heal(self, method):
        print(f"ENEMY HEALS BY: {method}..")
        if self.health < self.max_health-self.ap:
            self.health += round(self.ap/2)
        else:
            self.health = self.max_health
        print(f"CURRENT ENEMY'S HEALTH: {self.health}")