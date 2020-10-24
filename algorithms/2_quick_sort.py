# 2_quick_sort.py
from typing import List
import random


def swap(list: List, l_idx, r_idx) -> List:
    temp = list[l_idx]
    list[l_idx] = list[r_idx]
    list[r_idx] = temp
    return list


def ascending_comparer(l, r) -> bool:
    return l > r


def descending_comparer(l, r) -> bool:
    return l < r


def bubble_sort_impl(values, ascending=True, keys: List = None):
    comparer = ascending_comparer if ascending else descending_comparer
    end = len(values) - 1
    for i in range(end):
        j_range = range(end-i) if ascending else range(end-1, i-1, -1)
        for j in j_range:
            if comparer(values[j], values[j+1]):
                swap(values, j, j+1)
                if keys:
                    swap(keys, j, j+1)
    if keys:
        return values, keys
    return values


def choosePivot(list: List) -> int:
    # startIdx, midIdx, endIdx
    idxs = [0, int(len(list)/2), len(list)-1]
    idxs_values = [list[idx] for idx in idxs]
    values, keys = bubble_sort_impl(idxs_values, False, idxs)
    return keys[1]


def qsort_impl(list: List, start=None, end=None, ascending=True):

    if None in (start, end):
        start = 0
        end = len(list)

    dif = end - start
    if dif <= 1:
        return

    if dif == 2:
        if (ascending and (list[start] < list[end-1])) or (not ascending and (list[start] > list[end-1])):
            return list
        else:
            return swap(list, start, end-1)

    def value(idx): return list[idx]
    pivotIdx = start + choosePivot(list[start:end])
    pivot = value(pivotIdx)
    last_idx = end-1
    swap(list, pivotIdx, last_idx)

    while True:
        l_idx, r_idx = None, None
        for l in range(start, last_idx):  # exclude pivot
            if list[l] >= pivot:
                l_idx = l
                break
        for r in range(last_idx-1, start-1, -1):
            if list[r] < pivot:
                r_idx = r
                break
        # reaches the end
        if (l_idx is None) or (r_idx is None):
            return list  # ends here
        # crosses
        if l_idx >= r_idx:
            break
        swap(list, l_idx, r_idx)
    pivotIdx = l_idx
    swap(list, pivotIdx, last_idx)

    # print(list)

    qsort_impl(list, start, pivotIdx, ascending)
    qsort_impl(list, pivotIdx+1, end, ascending)
    return list


def bubble_sort(list: List, ascending=True, copy: bool = True):
    return bubble_sort_impl(list[:] if copy else list, ascending)


def qsort(list: List, ascending=True, copy: bool = True):
    return qsort_impl(list[:] if copy else list, ascending)


def compare_reversal(l: List, r: List) -> bool:
    l_ = l[:]
    r_ = r[:].reverse()
    return l_ == r_


def compare_lists(l: List, r: List) -> bool:
    l_sorted = l[:]
    l_sorted.sort()
    r_sorted = r[:]
    r_sorted.sort()
    return l_sorted == r_sorted


def main():
    #numbers = [2, 2, 2, 2, 1, 5, 6, 7, 7, 7, 2, 2, 2, 2, 2, 1, 4]
    #numbers = [random.randint(0, 10) for i in range(10)]
    numbers = [7, 1, 1, 10, 6, 6, 9, 1, 1, 2]
    print(f"Input : {numbers}")

    bubble_asc = bubble_sort(numbers)
    bubble_dsc = bubble_sort(numbers, ascending=False)
    quick_asc = qsort(numbers)
    quick_dsc = qsort(numbers, ascending=False)

    print(f"Bubble asc : {bubble_asc}")
    print(f"Bubble dsc : {bubble_dsc}")
    print(f"Quick sort asc : {quick_asc}")
    print(f"Quick sort dsc : {quick_dsc}")

    _ = numbers[:]
    _.sort()
    print("Answer : ", _)
    print("Bubble Sort successful" if _ ==
          bubble_asc else "Bubble sort failed")
    print("Quick Sort successful" if _ == quick_asc else "Quick sort failed")

    print("Bubble suc" if compare_reversal(
        bubble_asc, bubble_dsc) else "Bubble failed")
    print("Quick suc" if compare_reversal(
        quick_asc, quick_dsc) else "Quick failed")
    print("Bubble == Quick" if compare_lists(
        bubble_asc, quick_asc) else "Bubble Quick Different")


if __name__ == '__main__':
    main()
