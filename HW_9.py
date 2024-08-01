# Реалізація задачі про видачу решти за допомогою жадібного алгоритму та динамічного програмування

# Функція жадібного алгоритму для видачі решти
def find_coins_greedy(amount):
    """
    Функція приймає суму, яку потрібно видати покупцеві, і повертає словник
    із кількістю монет кожного номіналу, що використовуються для формування цієї суми.
    Алгоритм працює за принципом жадібного алгоритму.
    """
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count
    
    return result

# Функція динамічного програмування для видачі решти
def find_min_coins(amount):
    """
    Функція приймає суму, яку потрібно видати покупцеві, і повертає словник
    із кількістю монет кожного номіналу, що використовуються для формування цієї суми.
    Алгоритм працює за принципом динамічного програмування, забезпечуючи мінімальну кількість монет.
    """
    coins = [1, 2, 5, 10, 25, 50]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result

# Приклади використання
if __name__ == "__main__":
    # Приклад для жадібного алгоритму
    amount = 113
    greedy_result = find_coins_greedy(amount)
    print(f"Жадібний алгоритм для суми {amount}: {greedy_result}")  # {50: 2, 10: 1, 2: 1, 1: 1}
    
    # Приклад для динамічного програмування
    dp_result = find_min_coins(amount)
    print(f"Динамічне програмування для суми {amount}: {dp_result}")  # {50: 2, 10: 1, 2: 1, 1: 1}
