def knapsack(i, W, n, values, weights):
    # base case
    if i == n or W == 0:
        return 0

    # if weight of current item is more than remaining capacity, skip it
    if weights[i] > W:
        return knapsack(i + 1, W, n, values, weights)

    # choice: take or not take
    take = values[i] + knapsack(i + 1, W - weights[i], n, values, weights)
    not_take = knapsack(i + 1, W, n, values, weights)

    return max(take, not_take)


# inputs
n = 5
values = [10, 5, 8, 5, 3]
weights = [3, 2, 4, 6, 4]
W = 6

ans = knapsack(0, W, n, values, weights)
print(ans)
