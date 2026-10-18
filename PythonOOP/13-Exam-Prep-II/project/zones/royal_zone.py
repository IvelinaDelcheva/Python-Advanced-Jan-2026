from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    INITIAL_VOLUME = 10

    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)

    def zone_info(self):
        pirate_ships_count = 0
        for s in self.ships:
            if s.__class__.__name__ == 'PirateBattleship':
                pirate_ships_count += 1
        rz_stats = ["@Royal Zone Statistics@",
                    f"Code: {self.code}; Volume: {self.volume}"
                    f"Battleships currently in the Royal Zone: {len(self.ships)},"
                    f" {pirate_ships_count} out of them are Pirate Battleships."]
        all_ships = self.get_ships()
        if all_ships:
            rz_stats.append(f"#{', '.join(str(s) for s in all_ships)}#")

        return '\n'.join(rz_stats)
