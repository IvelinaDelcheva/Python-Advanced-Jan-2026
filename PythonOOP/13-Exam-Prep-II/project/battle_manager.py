from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:
    def __init__(self):
        self.zones: list = []
        self.ships: list = []

    def add_zone(self, zone_type: str, zone_code: str):
        zone_class = {"RoyalZone": RoyalZone, "PirateZone": PirateZone}

        if zone_type not in zone_class.keys():
            raise Exception("Invalid zone type!")

        zone_to_add = next((z for z in self.zones if z.code == zone_code), None)
        if zone_to_add:
            raise Exception("Zone already exists!")

        self.zones.append(zone_class[zone_type](zone_code))
        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        ship_class = {'RoyalBattleship': RoyalBattleship, 'PirateBattleship': PirateBattleship}

        if ship_type not in ship_class.keys():
            raise Exception(f"{ship_type} is an invalid type of ship!")

        self.ships.append(ship_class[ship_type](name, health, hit_strength))
        return f"A new {ship_type} was successfully added."

    def add_ship_to_zone(self, zone, ship):
        if zone.volume < 1:
            return f"Zone {zone.code} does not allow more participants!"

        if ship.health <= 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        ship_zone_types = {
            'Pirate': ["PirateZone", "PirateBattleship"],
            'Royal': ["RoyalZone", "RoyalBattleship"],
            'PirazteZRoyalS': ["PirateZone", "RoyalBattleship"],
            'RoyalZPirateS': ["RoyalZone", "PirateBattleship"]
        }

        zone_ship = [zone.__class__.__name__, ship.__class__.__name__]

        if zone_ship == ship_zone_types["Pirate"] or zone_ship == ship_zone_types["Royal"]:
            ship.is_attacking = True
        elif zone_ship == ship_zone_types["PirazteZRoyalS"] or zone_ship == ship_zone_types["RoyalZPirateS"]:
            ship.is_attacking = False

        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1

        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        remove_ship = next((s for s in self.ships if s.name == ship_name), None)
        if remove_ship is None:
            return "No ship with this name!"

        if not remove_ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(remove_ship)
        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone):

        if len(zone.ships) < 2:
            return "Not enough participants. The battle is canceled."

        attacker = next((s for s in zone.ships if s.is_attacking), None)
        target = next((s for s in zone.ships if not s.is_attacking), None)

        if attacker is None or target is None:
            return "Not enough participants. The battle is canceled."

        zone_type = 'Pirate' if zone.__class__.__name__ == 'PirateZone' else 'Royal'
        zone_battleships = [s for s in zone.ships if s.is_attacking and zone_type in s.__class__.__name__]
        most_powerful = list(sorted(zone_battleships, key=lambda s: -s.hit_strength))
        attack_ship = most_powerful[0]

        health_battleships = [s for s in zone.ships if not s.is_attacking and zone_type not in s.__class__.__name__]
        healthiest = list(sorted(health_battleships, key=lambda s: -s.health))
        target = healthiest[0]

        attack_ship.attack()
        target.take_damage(attack_ship)

        if target.health <= 0:
            zone.ships.remove(target)
            self.ships.remove(target)
            return f"{target.name} lost the battle and was sunk."

        if attack_ship.ammunition <= 0:
            zone.ships.remove(attack_ship)
            self.ships.remove(attack_ship)
            return f"{attack_ship.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."

    def get_statistics(self):
        battle_stats = []
        if self.ships:
            battle_stats.append(f"Available Battleships: {len(self.ships)}")
            battle_stats.append(f"#{', '.join(s.name for s in self.ships)}#")
        battle_stats.append("***Zones Statistics:***")
        battle_stats.append(f"Total Zones: {len(self.zones)}")
        for z in self.zones:
            battle_stats.append(z.zone_info())

        return '\n'.join(battle_stats)


battle_manager = BattleManager()

# Add zones
print(battle_manager.add_zone("RoyalZone", "001"))
print(battle_manager.add_zone("PirateZone", "002"))
print()

# Add battleships
print(battle_manager.add_battleship("RoyalBattleship", "RoyalOne", 50, 50))
print(battle_manager.add_battleship("RoyalBattleship", "RoyalTwo", 80, 45))
print(battle_manager.add_battleship("PirateBattleship", "PirateOne", 50, 50))
print(battle_manager.add_battleship("PirateBattleship", "PirateTwo", 70, 60))
print(battle_manager.add_battleship("RoyalBattleship", "RoyalThree", 100, 100))
print(battle_manager.add_battleship("PirateBattleship", "PirateThree", 90, 90))
print()

# Retrieve battleships and zones
royal_zone = battle_manager.zones[0]
pirate_zone = battle_manager.zones[1]

royal_one = battle_manager.ships[0]
royal_two = battle_manager.ships[1]
pirate_one = battle_manager.ships[2]
pirate_two = battle_manager.ships[3]

# Add ships to zones
print(battle_manager.add_ship_to_zone(royal_zone, royal_one))
print(battle_manager.add_ship_to_zone(royal_zone, pirate_one))
print(battle_manager.add_ship_to_zone(pirate_zone, royal_two))
print(battle_manager.add_ship_to_zone(pirate_zone, pirate_two))
print()

# Remove a battleship
print(battle_manager.remove_battleship("RoyalTwo"))
print(battle_manager.remove_battleship("Nonexistent"))
print()

# Start battle in RoyalZone
print(battle_manager.start_battle(royal_zone))
print()

# Start battle in PirateZone
print(battle_manager.start_battle(pirate_zone))
print()

# Start another battle in RoyalZone
print(battle_manager.start_battle(royal_zone))
print()

# Retrieve updated statistics
print(battle_manager.get_statistics())
print()

# Remove a battleship
print(battle_manager.remove_battleship("RoyalThree"))
