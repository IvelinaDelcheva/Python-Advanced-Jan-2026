from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    INITIAL_VOLUME = 8

    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)

    def zone_info(self):
        royal_ships_count = 0
        for s in self.ships:
            if s.__class__.__name__ == 'RoyalBattleship':
                royal_ships_count += 1
        pz_stats = ["@Pirate Zone Statistics@",
                    f"Code: {self.code}; Volume: {self.volume}"
                    f"Battleships currently in the Pirate Zone: {len(self.ships)},"
                    f" {royal_ships_count} out of them are Royal Battleships."]
        all_ships = self.get_ships()
        if all_ships:
            pz_stats.append(f"#{', '.join(str(s) for s in all_ships)}#")

        return '\n'.join(pz_stats)
