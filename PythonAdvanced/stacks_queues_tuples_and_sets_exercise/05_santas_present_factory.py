from collections import deque

materials = [int(material) for material in input().split()]
magic_level = deque(int(magic) for magic in input().split())

required = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

crafted_presents = {}

while materials and magic_level:
    last_material = materials[-1]
    first_magic = magic_level[0]

    if last_material == 0 and first_magic == 0:
        materials.pop()
        magic_level.popleft()
        continue

    if last_material == 0:
        materials.pop()
        continue

    if first_magic == 0:
        magic_level.popleft()
        continue

    total_magic = last_material * first_magic
    if total_magic in required:
        crafted_presents[required[total_magic]] = crafted_presents.get(required[total_magic], 0) + 1
        materials.pop()
        magic_level.popleft()
    elif total_magic < 0:
        total_magic = materials.pop() + magic_level.popleft()
        materials.append(total_magic)
    elif total_magic not in required and total_magic > 0:
        magic_level.popleft()
        materials[-1] += 15

pairs = [{'Doll', 'Wooden train'}, {'Teddy bear', 'Bicycle'}]
success = False
for pair in pairs:
    if pair.issubset(crafted_presents):
        success = True
        break

materials_left = f"Materials left: {', '.join(str(material) for material in reversed(materials))}" \
    if materials else  ""
magic_left = f"Magic left: {', '.join(str(magic) for magic in magic_level)}" \
    if magic_level else ""

if success:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials_left:
    print(materials_left)
if magic_left:
    print(magic_left)
print('\n'.join(sorted(f"{toy_name}: {amount}" for toy_name, amount in crafted_presents.items())))
