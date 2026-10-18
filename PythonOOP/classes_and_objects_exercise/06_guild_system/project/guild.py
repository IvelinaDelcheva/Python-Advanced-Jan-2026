from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: list[Player] = []

    def assign_player(self, _player: Player) -> str:
        if _player in self.players:
            return f"Player {_player.name} is already in the guild."
        if _player.guild != Player.guild:
            return f"Player {_player.name} is in another guild."
        _player.guild = self.name
        self.players.append(_player)
        return f"Welcome player {_player.name} to the guild {_player.guild}"

    def kick_player(self, player_name: str) -> str:
        for player in self.players:
            if player.name == player_name:
                player.guild = Player.guild
                self.players.remove(player)
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self) -> str:
        _result = [f'Guild: {self.name}']
        for g_player in self.players:
            _result.append(f'{g_player.player_info()}')
        return '\n'.join(_result)



