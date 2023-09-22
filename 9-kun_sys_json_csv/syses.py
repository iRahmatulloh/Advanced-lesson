def solution(statues):
    rang = sorted(statues)
    x = 0
    if len(rang) - 1 == 0:
        return 0
    else:
        for i in range(len(rang) - 1):
            print(x)
            x += (rang[i + 1] - rang[i] - 1)
            print(x)
    return x

print(solution([0, 5]))