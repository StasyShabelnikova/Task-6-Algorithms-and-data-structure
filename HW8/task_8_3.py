def find_max_length(nums):
    prefix_sum = 0
    max_len = 0
    first_index = {0: -1}

    for i, num in enumerate(nums):
        if num == 0:
            prefix_sum -= 1
        else:
            prefix_sum += 1

        if prefix_sum in first_index:
            max_len = max(max_len, i - first_index[prefix_sum])
        else:
            first_index[prefix_sum] = i

    return max_len