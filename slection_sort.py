def selection_sort(l):
    n = len(l)
    for i in range(0, n-1):
        current_min = i
        for j in range(i + 1, n):
            if l[j] < l[current_min]:
                current_min = j

        if current_min != i:
            l[i], l[current_min] = l[current_min], l[i]


if __name__ == "__main__":
    l = [2,5,1,9,56,4,7,6,5]
    print("Before Sort:", l)
    selection_sort(l)
    print('After Sort: ', l)



"""-------------------------------------------------"""
"""-------------------------------------------------"""
"""-------------------------------------------------"""


def selection_sort(l):
    n = len(l)

    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            if l[j] < l[min_index]:
                min_index = j
        if min_index != i:
            l[i], l[min_index] = l[min_index], l[i]

def selection_sort(l):
    n = len(l)

    for i in range(0, n -1):
        min = i
        for j in range(i +1, n):
            if l[j] < l[min]:
                min = j

        if min != i:
            l[i], l[min] = l[min], l[i]

def selection_sort(p):
    m = len(p)
    for q in range(0, m -1):
        min_valu = q
        for f in range(q + 1, m):
            if p[f] < p[min_valu]:
                min_valu = f
        if min_valu != q:
            p[q], p[min_valu] = p[min_valu], p[q]


if __name__ == "__main__":
    p = [12,15,11,19,156,14,17,16,15]
    print("Before Sort:", p)
    selection_sort(p)
    print('After Sort: ', p)

"""-------------------------------------------------"""
"""-------------------------------------------------"""
"""-------------------------------------------------"""



def sel_sort(a):
    b = len(a)
    for c in range(0, b-1):
        mini_value = c
        for d in range(c + 1, b):
            if a[d] < a[mini_value]:
                mini_value = d

        if mini_value != c:
          a[c], a[mini_value] = a[mini_value], a[c]

def sort(a):
     n = len(a)
     for i in range(0,n-1):
         index_min = i
         for j in range(i + 1, n):
             if a[j] < a[index_min]:
                index_min = j
         if index_min != i:
            a[i], a[index_min] = a[index_min], a[i]

def sort(a):
    x = len(a)
    for i in range(0, x-1):
        min_index = i
        for j in range(i + 1, x):
            if a[j] < a[min_index]:
                min_index = j

        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]

if __name__ == "__main__":
    a = [97,654,614,654,654,64,635,465,487,65,435,468,768,463,1,2,3,4,65,6,
         4,3,2,1,6,1,8,0,3,4,5,56,65,]
    print("Before sort: ", a)
    sort(a)
    print("After Sort: ", a)

if __name__ == "__main__":
    a = [97,654,614,654,654,64,635,465,487,65,435,468,768,463,1,2,3,4,65,6,
         4,3,2,1,6,1,8,0,3,4,5,56,65,]
    print("Before sort: ", a)
    sel_sort(a)
    print("After Sort: ", a)


