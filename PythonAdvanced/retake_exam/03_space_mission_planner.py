def check_mission_feasibility(crew_size: int, budget: float, *args):
    confirmed = []
    suspended = []
    remaining_budget = budget

    for mission in args:
        name = mission[0]
        cr_size = mission[1]
        m_budget = mission[2]

        if cr_size > crew_size or m_budget > remaining_budget:
            suspended.append(list(mission))
        else:
            confirmed.append(list(mission))
            remaining_budget -= m_budget

    result = []
    if len(confirmed) == len(args):
        result.append("All missions are feasible within crew and budget limits.")

    if confirmed:
        sorted_missions = list(sorted(confirmed))
        result.append("Confirmed Missions:")
        for s_m in sorted_missions:
            result.append(f"${s_m[0]}, crew size: {s_m[1]}, budget: {s_m[2]:.2f}")

    if suspended:
        sorted_suspended = list(sorted(suspended, key=lambda m: (m[1], m[2]), reverse=True))
        result.append("Suspended Missions:")
        for s_m in sorted_suspended:
            result.append(f"!{s_m[0]}, crew size: {s_m[1]}, budget: {s_m[2]:.2f}")

    return '\n'.join(result)


print(check_mission_feasibility(
    3, 20_000_000.0,
    ("Voyager 1", 2, 5_000_000.0),
    ("Hubble 2", 4, 3_000_000.0),
    ("Lunar 4", 3, 6_000_001.0),
    ("Apollo 11", 3, 9_000_000.1),
    ("Hubble 3", 4, 2_000_000.0),
    ("Lunar 5", 3, 4_000_001.0)
))

