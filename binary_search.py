def binary_search(seq, value):
    """Binary search algorithm"""

    low, high = 0, len(seq) - 1
    while low <= high:
        mid = (low + high) // 2
        if seq[mid] == value:
            return mid
        elif seq[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    nums = [i * 2 + 1 for i in range(10)]
    print(nums)

    value = 17
    print(binary_search(nums, value))
