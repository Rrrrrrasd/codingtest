import sys
import math

#sort 만들어서 한번 넣어보기 //-> 더 늘어남 ? 
def merge(arr1, arr2):
    result = list()
    i = 0
    j = 0

    while i<len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    
    return result


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = math.floor(len(arr)/2)
    left = mergeSort(arr[0:mid])
    right = mergeSort(arr[mid:])
    return merge(left,right)


n = int(sys.stdin.readline().strip())
in_company = dict()
result = list()

for _ in range(n):
    name, status = sys.stdin.readline().split()
    if status == 'leave':
        in_company[name] = 0
    if status == 'enter':
        in_company[name] = 1

for name, status in in_company.items():
    if status:
        result.append(name)

result = mergeSort(result)

for name in result:
    print(name)



