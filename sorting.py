def insertion_sort(seq) -> None:
    """Insertion sort algorithm"""
    
    for i in range(1, len(seq)):
        # compare current element to every element before it
        for j in range(i, 0, -1):
            if seq[j] < seq[j-1]:
                seq[j], seq[j-1] = seq[j-1], seq[j]  # swap the elements


def merge_sort(seq, start: int, end: int) -> None:
    """Merge sort algorithm"""

    # if len of seq is 1 or 0, then it's already sorted
    if start < end - 1:
        # else len of seq is longer than 1
        mid = (start + end) // 2
        # divide the sequence into two halves
        # recursively call merge sort on them
        merge_sort(seq, start, mid)
        merge_sort(seq, mid, end)
        # merge the two halves
        i, j = start, mid
        merged = []
        while True:
            if seq[i] <= seq[j]:
                merged.append(seq[i])
                i += 1
            else:
                merged.append(seq[j])
                j += 1
            if i == mid:
                merged.extend(seq[j:end])
                break
            if j == end:
                merged.extend(seq[i:mid])
                break
        seq[start:end] = merged


def selection_sort(seq) -> None:
    """Selection sort algorithm"""
    for i in range(len(seq)):
        min_idx = i
        for j in range(i, len(seq)):
            if seq[j] < seq[min_idx]:
                min_idx = j
        seq[i], seq[min_idx] = seq[min_idx], seq[i]


if __name__ == '__main__':
    nums = [9, 8, 9, 8, 3, 2, 1, 1, 2, 4, 9, 7, 7, 8, 8, 5, 5, 3]
    x = nums.copy()
    y = nums.copy()
    z = nums.copy()    

    insertion_sort(x)
    merge_sort(y, 0, len(y))
    selection_sort(z)
    
    print(nums, 'original list')
    print(sorted(nums), 'sorted by python')
    print(x, 'insertion sort')
    print(y, 'merge sort')
    print(z, 'selection sort')
