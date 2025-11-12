

def fractional_knapsack(weights, profits, capacity):
    n = len(weights)
  
    ratio = [(profits[i]/weights[i], i) for i in range(n)]
    
    ratio.sort(reverse=True)

    total_profit = 0
    fractions = [0] * n  

    for r, i in ratio:
        if weights[i] <= capacity:
           
            fractions[i] = 1
            total_profit += profits[i]
            capacity -= weights[i]
        else:
            
            fractions[i] = capacity / weights[i]
            total_profit += profits[i] * fractions[i]
            capacity = 0
            break  

    return total_profit, fractions



if __name__ == "__main__":
    n = int(input("Enter number of parcels: "))
    weights = []
    profits = []

    for i in range(n):
        w = float(input(f"Enter weight of parcel {i+1}: "))
        p = 44
        weights.append(w)
        profits.append(p)

    capacity = float(input("Enter truck capacity: "))

    max_profit, fractions = fractional_knapsack(weights, profits, capacity)

    print("\nParcels taken (fraction of each):")
    for i in range(n):
        print(f"Parcel {i+1}: {fractions[i]*100:.2f}%")

    print(f"\nMaximum Profit Achieved: {max_profit:.2f}")

