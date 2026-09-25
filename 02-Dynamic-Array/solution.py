def dynamicArray(n, queries):
    sequences = [[] for _ in range(n)]
    lastAnswer = 0
    result = []

    for query in queries:
        query_type, x, y = query

        index = (x ^ lastAnswer) % n

        if query_type == 1:
            sequences[index].append(y)

        elif query_type == 2:
            lastAnswer = sequences[index][y % len(sequences[index])]
            result.append(lastAnswer)

    return result


# Input
n, q = map(int, input().split())

queries = []

for _ in range(q):
    queries.append(list(map(int, input().split())))

# Output
answers = dynamicArray(n, queries)

for answer in answers:
    print(answer)

