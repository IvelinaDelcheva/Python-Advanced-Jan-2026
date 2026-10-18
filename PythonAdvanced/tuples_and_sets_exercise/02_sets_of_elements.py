n, m = map(int, input().split())


n_set = {int(input()) for _ in range(n)}
m_set = {int(input()) for _ in range(m)}

print(*n_set.intersection(m_set), sep='\n')
