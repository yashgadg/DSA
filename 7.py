

def merge(arr, left, mid, right):

    L = arr[left:mid+1]
    R = arr[mid+1:right+1]

    i = j = 0
    k = left

    
    while i < len(L) and j < len(R):
        if L[i][1] <= R[j][1]:  
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1


    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)



if __name__ == "__main__":
    print("Enter the number of orders: ", end="")
    n = int(input())
    orders = []

    for i in range(n):
        order_id = input(f"Enter Order ID for order {i+1}: ")
        time = int(input(f"Enter Estimated Delivery Time (in minutes) for Order {order_id}: "))
        orders.append((order_id, time))

    print("\nOriginal Orders (Unsorted):")
    for order in orders:
        print(f"Order ID: {order[0]}, Delivery Time: {order[1]} mins")

    merge_sort(orders, 0, len(orders) - 1)

    print("\nSorted Orders (by Delivery Time):")
    for order in orders:
        print(f"Order ID: {order[0]}, Delivery Time: {order[1]} mins")

