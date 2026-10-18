from collections import deque


bees = deque(int(x) for x in input().split())
bee_eaters = [int(x) for x in input().split()]

while bees and bee_eaters:
    bee_group = bees[0]
    bee_eaters_gr = bee_eaters[-1]

    died_bee_eat = bee_group // 7
    left_bees = bee_group % 7

    if died_bee_eat < bee_eaters_gr:
        bee_eaters[-1] -= died_bee_eat
        bees.popleft()
    elif died_bee_eat > bee_eaters_gr:
        bees.append(bees.popleft() - bee_eaters.pop() * 7)
    elif died_bee_eat == bee_eaters_gr:
        bees.popleft()
        bee_eaters.pop()
        if left_bees:
            bees.append(left_bees)


print("The final battle is over!")
if not bees and not bee_eaters:
    print("But no one made it out alive!")
elif bees:
    print(f"Bee groups left: {', '.join(str(bee) for bee in bees)}")
elif bee_eaters:
    print(f"Bee-eater groups left: {', '.join(str(bee_eat) for bee_eat in bee_eaters)}")