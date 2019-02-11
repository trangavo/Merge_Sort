# for simulation and generating plots
import math, time, random
import matplotlib.pyplot as plt
# 2-way merge-sort
def Two_Merge(L,R,A):
    l = len(L)
    r = len(R)
    n = len(A)
    L.append(math.inf)
    R.append(math.inf)
    i = 0
    j = 0
    for k in range(n):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j = j+1
def Two_MergeSort(A):
    n = len(A)
    if n == 1:
        return A
    else:
        L = []
        R = []
        for x in range(n//2):
            L.append(A[x])
        for y in range(n//2,n):
            R.append(A[y])
        Two_MergeSort(L)
        Two_MergeSort(R)
        Two_Merge(L,R,A)
        return A

# 3-way merge sort
def Three_Merge(L,M,R,A):
    l = len(L)
    m = len(M)
    r = len(R)
    n = len(A)
    L.append(math.inf)
    M.append(math.inf)
    R.append(math.inf)
    i = 0
    h = 0
    j = 0
    for k in range(n):
        if L[i] <= M[h] and L[i] <= R[j]:
            A[k] = L[i]
            i = i+1
        elif M[h] <= L[i] and M[h] <= R[j]:
            A[k] = M[h]
            h = h+1
        elif R[j] <= L[i] and R[j] <= M[h]:
            A[k] = R[j]
            j = j+1
def Three_MergeSort(A):
    n = len(A)
    if n == 1:
        return A
    elif n == 2:
        A.append(math.inf)
        n += 1
        L = A[0:n//3]
        M = A[n//3:2*(n//3)]
        R = A[2*(n//3):n]
        Three_MergeSort(L)
        Three_MergeSort(M)
        Three_MergeSort(R)
        Three_Merge(L,M,R,A)
        return A[0:2]
    else:
        L = []
        M = []
        R = []
        for x in range(n//3):
            L.append(A[x])
        for y in range(n//3, 2*(n//3)):
            M.append(A[y])
        for z in range(2*(n//3),n):
            R.append(A[z])
        Three_MergeSort(L)
        Three_MergeSort(M)
        Three_MergeSort(R)
        Three_Merge(L,M,R,A)
        return A

# 3-way merge sort 2
def Insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return(A)
def Mod_Merge(L,M,R,A):
    l = len(L)
    m = len(M)
    r = len(R)
    n = len(A)
    L.append(math.inf)
    M.append(math.inf)
    R.append(math.inf)
    i = 0
    h = 0
    j = 0
    for k in range(n):
        if L[i] <= M[h] and L[i] <= R[j]:
            A[k] = L[i]
            i = i+1
        elif M[h] <= L[i] and M[h] <= R[j]:
            A[k] = M[h]
            h = h+1
        elif R[j] <= L[i] and R[j] <= M[h]:
            A[k] = R[j]
            j = j+1
def Mod_MergeSort(A, thres):
    n = len(A)
    if n < thres:
        Insertion_sort(A)
    else:
        L = []
        M = []
        R = []
        for x in range(n//3):
            L.append(A[x])
        for y in range(n//3, 2*(n//3)):
            M.append(A[y])
        for z in range(2*(n//3),n):
            R.append(A[z])
        Mod_MergeSort(L, thres)
        Mod_MergeSort(M, thres)
        Mod_MergeSort(R, thres)
        Mod_Merge(L,M,R,A)
        return A

# simulation
def simulation(low, high, step, times, thres):
    size_array = [a for a in range(low, high, step)]
    run_time_1 = []
    run_time_2 = []
    run_time_3 = []
    # users can input array size, number of simulations for each array size, and the threshold for the augmented 3-way merge-sort of their own choice
    # for each array size
    for size in range(low, high, step):
        B = random.sample(range(0,size),size)
        A = random.choices(B, k=size)
        sum_1 = 0
        sum_2 = 0
        sum_3 = 0
        # for each simulation of a certain array size
        for j in range(times):
            start_1 = time.time()
            Two_MergeSort(A)
            end_1 = time.time()
            sum_1 += end_1-start_1
            
            start_2 = time.time()
            Three_MergeSort(A)
            end_2 = time.time()
            sum_2 += end_2-start_2
            
            start_3 = time.time()
            Mod_MergeSort(A, thres)
            end_3 = time.time()
            sum_3 += end_3-start_3
        # averaged running time of each algorithm at a certain array size
        average_1 = sum_1/times
        average_2 = sum_2/times
        average_3 = sum_3/times
        run_time_1.append(average_1)
        run_time_2.append(average_2)
        run_time_3.append(average_3)
    # plot the running time against array size for each algorithm
    plt.plot(size_array, run_time_1, color="red")
    plt.plot(size_array, run_time_2, color="blue")
    plt.plot(size_array, run_time_3, color="green")
    plt.show()
simulation(1,100,5,20,5)
simulation(1,100,5,20,20)
simulation(1,100,5,20,60)
simulation(10,1000,50,10,20)
simulation(10,1000,50,10,60)
simulation(10,1000,50,10,100)
