items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    ranked = sorted(
        items.items(),
        key=lambda kv: kv[1]["calories"] / kv[1]["cost"],
        reverse=True,
    )

    chosen = []
    total_cost = 0
    total_cal = 0

    for name, data in ranked:
        if total_cost + data["cost"] <= budget:
            chosen.append(name)
            total_cost += data["cost"]
            total_cal += data["calories"]

    return chosen, total_cost, total_cal


def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = names[i - 1]
        cost = items[name]["cost"]
        cal = items[name]["calories"]

        for b in range(budget + 1):
            dp[i][b] = dp[i - 1][b]
            if cost <= b:
                take = dp[i - 1][b - cost] + cal
                if take > dp[i][b]:
                    dp[i][b] = take

    chosen = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name = names[i - 1]
            chosen.append(name)
            b -= items[name]["cost"]

    chosen.reverse()
    total_cost = sum(items[name]["cost"] for name in chosen)
    total_cal = sum(items[name]["calories"] for name in chosen)

    return chosen, total_cost, total_cal


if __name__ == "__main__":
    budget = 100

    g_items, g_cost, g_cal = greedy_algorithm(items, budget)
    dp_items, dp_cost, dp_cal = dynamic_programming(items, budget)

    print("BUDGET:", budget)

    print("\nGreedy:")
    print("  items:", g_items)
    print("  cost:", g_cost)
    print("  calories:", g_cal)

    print("\nDP (optimal):")
    print("  items:", dp_items)
    print("  cost:", dp_cost)
    print("  calories:", dp_cal)
