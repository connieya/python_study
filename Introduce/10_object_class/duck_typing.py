class Parrot:
    def fly(self):
        print("Parrot flying")


class Airplane:
    def fly(self):
        print("Airplane flying")


class Whale:
    def swim(self):
        print("Whale swimming")


def lift_off(entity):
    entity.fly()


parrot = Parrot()
airplane = Airplane()
whale = Whale()

lift_off(parrot)  # Parrot flying
lift_off(airplane)  # Parrot flying
lift_off(whale)  # 'Whale' object has no attribute 'fly'
