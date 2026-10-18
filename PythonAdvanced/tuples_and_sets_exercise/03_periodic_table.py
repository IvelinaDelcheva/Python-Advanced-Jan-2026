# n = int(input())
# unique_chemicals = set()
#
# for _ in range(n):
#     chemical_compounds = input().split()
#     for chemical in chemical_compounds:
#         unique_chemicals.add(chemical)

unique_chemicals = set(chemical for _ in range(int(input())) for chemical in input().split())

print(*unique_chemicals, sep='\n')