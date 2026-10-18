from collections import deque

bullet_price = int(input())
gun_barrel = int(input())
bullets = deque(map(int, input().split()))
locks = deque(map(int, input().split()))
intelligence_value = int(input())

bullets_used = 0

while bullets:
    if bullets_used % gun_barrel == 0 and bullets_used != 0:
        if bullets:
            print('Reloading!')

    if not bullets or not locks:
        break

    current_bullet = bullets.pop()
    current_lock = locks[0]

    if current_lock >= current_bullet:
        locks.popleft()
        bullets_used += 1
        print('Bang!')
    elif current_bullet > current_lock:
        bullets_used += 1
        print('Ping!')

bullets_cost = bullet_price * bullets_used
money_earned = intelligence_value - bullets_cost

if not locks:
    print(f'{len(bullets)} bullets left. Earned ${money_earned}')
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")