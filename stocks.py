import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["single", "multi"], metavar="MODE")
    parser.add_argument(
        "--prices", type=str, required=True, help="Comma-separated list of daily prices"
    )
    args = parser.parse_args()

    prices_str = args.prices
    if not prices_str:
        print("Must specify --prices as comma-separated list")
        exit(1)
    prices = [int(p) for p in prices_str.split(",")]

    print(f"Solving stock trader with {args.mode} transactions...")

    if args.mode == "single":
        max_profit = solve_single_txn(prices)
    elif args.mode == "multi":
        max_profit = solve_multi_txn(prices)

    print(f"Max profit: {max_profit}")


def solve_single_txn(prices):
    return single_txn_helper(prices)


def single_txn_helper(prices):
    maxes = [prices[-1] - prices[0]]

    if len(prices) > 2:
        maxes.append(single_txn_helper(prices[0:-1]))
        maxes.append(single_txn_helper(prices[1:]))

    return max(0, *maxes)


def solve_multi_txn(prices):
    return multi_txn_helper(prices)


def multi_txn_helper(prices):
    maxes = [prices[-1] - prices[0]]

    if len(prices) > 2:
        for i in range(1, len(prices)):
            left, right = 0, 0
            if i > 1:
                left = max(multi_txn_helper(prices[0:i]), 0)
            if i < len(prices) - 1:
                right = max(multi_txn_helper(prices[i:]), 0)
            maxes.append(left + right)
    return max(0, *maxes)


if __name__ == "__main__":
    main()
