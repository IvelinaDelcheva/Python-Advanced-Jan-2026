from collections import deque

# Parse robots
robots_input = input().split(";")
robots = []

for r in robots_input:
    name, time = r.split("-")
    robots.append({
        "name": name,
        "process_time": int(time),
        "busy_until": 0
    })

# Parse start time
h, m, s = map(int, input().split(":"))
current_time = h * 3600 + m * 60 + s

# Read products
products = deque()
while True:
    product = input()
    if product == "End":
        break
    products.append(product)

# Simulation
while products:
    current_time += 1
    product = products.popleft()

    assigned = False
    for robot in robots:
        if robot["busy_until"] <= current_time:
            robot["busy_until"] = current_time + robot["process_time"]

            hh = (current_time // 3600) % 24
            mm = (current_time % 3600) // 60
            ss = current_time % 60

            print(f"{robot['name']} - {product} [{hh:02d}:{mm:02d}:{ss:02d}]")
            assigned = True
            break

    if not assigned:
        products.append(product)
