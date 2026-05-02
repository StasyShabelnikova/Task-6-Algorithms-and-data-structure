def Pascal_triangle(n):
    if n == 0:
        return []
    result = [[1]]
    if n > 0:
        for i in range (1, n):
            last_str = result[-1]
            new_str = [1] * (len(last_str) + 1)
            for j in range (1, len(new_str)-1):
                new_str[j] = last_str[j-1] + last_str[j]
            result.append(new_str)
    return result