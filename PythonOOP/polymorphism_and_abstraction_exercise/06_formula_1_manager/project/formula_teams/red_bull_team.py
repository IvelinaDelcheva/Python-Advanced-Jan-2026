from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    RACE_EXPENSES = 250_000

    @property
    def sponsors(self) -> dict:
        sponsors = {"Oracle": {1: 1_500_000,
                               2: 800_000},
                    "Honda": {8: 20_000,
                              10: 10_000}}
        return sponsors

    @property
    def expenses(self):
        return self.RACE_EXPENSES
