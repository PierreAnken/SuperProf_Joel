class BaseTank:

    def __init__(
            self,
            tank_model,
            tank_type,
            tank_health=200,
            tank_armor=(10, 5, 0),
            canon_damage=30,
            canon_penetration=10,
            canon_precision=80
    ):
        self.tank_model = tank_model
        self.tank_type = tank_type
        self.tank_health = tank_health
        self.tank_armor = tank_armor
        self.canon_damage = canon_damage
        self.canon_penetration = canon_penetration
        self.canon_precision = canon_precision
        self.alive = True


