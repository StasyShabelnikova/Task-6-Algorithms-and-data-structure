def max_subarray_sum(arr, k):
    if k <= 0 or len(arr) < k:
        return None

    prefix = [0] * (len(arr) + 1)

    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]

    max_sum = float("-inf")

    for right in range(k, len(arr) + 1):
        left = right - k
        current_sum = prefix[right] - prefix[left]
        max_sum = max(max_sum, current_sum)

    return max_sum