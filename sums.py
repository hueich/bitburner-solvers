import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--numbers", type=str, required=True, help="Comma-separated list of numbers"
    )
    parser.add_argument(
        "--target", type=int, required=True, help="Target number to sum to"
    )
    args = parser.parse_args()

    numbers_str = args.numbers
    if not numbers_str:
        print("Must specify --numbers as comma-separated list")
        exit(1)
    numbers = [int(n) for n in numbers_str.split(",")]

    print(f"target={args.target} numbers={numbers}")

    ways = ways_to_sum(numbers, args.target)
    print(f"Ways to sum: {ways}")


def ways_to_sum(numbers, target):
    # Assume source numbers are positive and not empty.
    if target == 0 or len(numbers) == 0:
        return 0

    num = numbers[0]
    ways = 0

    ways += 1 if target % num == 0 else 0

    if len(numbers) > 1:
        for n in range(0, target, num):
            ways += ways_to_sum(numbers[1:], target - n)

    return ways


if __name__ == "__main__":
    main()
