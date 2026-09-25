def matchingStrings(strings, queries):
    frequency = {}

    for s in strings:
        frequency[s] = frequency.get(s, 0) + 1

    result = []

    for q in queries:
        result.append(frequency.get(q, 0))

    return result


n = int(input())

strings = []

for _ in range(n):
    strings.append(input().strip())

q = int(input())

queries = []

for _ in range(q):
    queries.append(input().strip())

answers = matchingStrings(strings, queries)

for answer in answers:
    print(answer)
