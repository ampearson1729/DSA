def insertionSort(A):
    """ """
    i = 1; n = len(A)
    while i < n:
        j = i - 1
        while j >= 0 and A[j+1] < A[j]:
            A[j], A[j+1] = A[j+1], A[j]
            j -= 1
        i += 1
    return A

def recursiveMergeSort(A):
    """ """
    n = len(A)
    if n < 2: return A
    else: 
        i = n//2
        return mergeSortedLists(recursiveMergeSort(A[:i]),recursiveMergeSort(A[i:]))

def mergeSortedLists(A,B):
    """ Given two sorted lists A and B, merge them """
    i,j,k = 0,0,0
    C = [0]*(len(A)+len(B))
    # Fill out C with comparisons until one of the lists is completed
    while i < len(A) and j < len(B):
        if A[i] < B[j]: 
            C[k] = A[i]
            i += 1
        else: 
            C[k] = B[j]
            j += 1
        k += 1
    # Finish filling C with list that still has values
    if i == len(A): C[k:] = B[j:] # copy over B vals
    else: C[k:] = A[i:]

    return  C


if __name__ == "__main__":
    # Test cases
    test_cases = [
        [],
        [1],
        [5, 3, 8, 1, 2],
        [10, 9, 8, 7, 6],
        [2, 2, 2, 2],
    ]


if __name__ == "__main__":
    for i, case in enumerate(test_cases, 1):
        print(f"Test case {i}: {case} -> {recursiveMergeSort(case.copy())}")

