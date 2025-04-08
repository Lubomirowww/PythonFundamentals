class Weapon:

    def __init__(self, bullet):
        self.bullet = bullet



    def shoot(self):
        if self.bullet > 0:
            self.bullet -= 1
            return  "Shooting..."
        else:
             return "No Bullets left....."


    def __repr__(self): #репрезентира информация от нашия клас
        return f"Remaining bullets {self.bullet}"

weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)