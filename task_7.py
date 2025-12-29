import random
from collections import Counter
from typing import Dict, Optional
import matplotlib.pyplot as plt


WAYS_OUT_OF_36 = {
    2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6,
    8: 5, 9: 4, 10: 3, 11: 2, 12: 1
}


def simulate_dice_rolls(n: int, seed: Optional[int] = 42) -> Dict[int, float]:
    if seed is not None:
        random.seed(seed)

    counts = Counter()
    for _ in range(n):
        s = random.randint(1, 6) + random.randint(1, 6)
        counts[s] += 1

    return {k: counts[k] / n for k in range(2, 13)}


def analytical_probs() -> Dict[int, float]:
    return {k: v / 36 for k, v in WAYS_OUT_OF_36.items()}


def print_table(mc: Dict[int, float], an: Dict[int, float]) -> None:
    print("Sum | MonteCarlo | Analytical | AbsDiff | Analytical (x/36)")
    print("-----------------------------------------------------------")
    for s in range(2, 13):
        diff = abs(mc[s] - an[s])
        frac = f"{WAYS_OUT_OF_36[s]}/36"
        print(f"{s:>3} | {mc[s]:>9.5f} | {an[s]:>10.5f} | {diff:>7.5f} | {frac:>16}")


def plot_probs(mc: Dict[int, float], an: Dict[int, float]) -> None:
    sums = list(range(2, 13))
    mc_vals = [mc[s] for s in sums]
    an_vals = [an[s] for s in sums]

    plt.figure(figsize=(10, 5))
    plt.plot(sums, mc_vals, marker="o", label="Monte Carlo")
    plt.plot(sums, an_vals, marker="s", label="Analytical")
    plt.title("Two Dice Sum Probabilities")
    plt.xlabel("Sum")
    plt.ylabel("Probability")
    plt.xticks(sums)
    plt.grid(True)
    plt.legend()
    plt.show()


def main():
    N = 100_000
    mc = simulate_dice_rolls(N)
    an = analytical_probs()

    print("Simulations:", N)
    print_table(mc, an)
    plot_probs(mc, an)


if __name__ == "__main__":
    main()
