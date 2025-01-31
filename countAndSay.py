def count_and_say(n):
    if not isinstance(n, int):
        raise TypeError('n must be an integer')
    if n <= 0:
        raise ValueError('n must be a positive integer')

    if n == 1:
        return "1"

    current = "1"
    for i in range(1, n):
        result = ""
        count = 1
        for j in range(len(current)):
            if j < len(current) - 1 and current[j] == current[j+1]:
                count += 1
            else:
                result += str(count) + current[j]
                count = 1
        current = result

    return current



