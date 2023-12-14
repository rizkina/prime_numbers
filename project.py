from prettytable import PrettyTable
import sys


def prime_selector(min, max):
    """
    Selected list of prime number limited by by lower limit until upper limit.

    :param limit: Maximum number
    :type limit: int
    :raise TypeError: If limit is not an positif int
    :return: list of prime number in rannge 1 to limit
    :rtype: list
    """
    primes = []
    for num in range(min, max + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def is_prime(num):
    """
    Define a number is a prime number or not.

    :param num: number to check as prime or not
    :type num: int
    :raise TypeError: If num is not an positif int
    :return: boolean (True or False)
    :rtype: boolean (True or False)
    """
    if num <= 1:
        return False
    if num > 1:
        # using for loop to check modulo number divide by i start from 2 up to square root num + 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True


def sum_primes(min, max):
    """
    Summerize all prime number in specific range by lower limit until upper limit.

    :param limit: maximum number
    :type limit: int
    :raise TypeError: If primes is not a positif int
    :return: Sum of prime numbers in range
    :rtype: int
    """
    primes = prime_selector(min, max)
    return sum(prime for prime in primes)


def menu(choice):
    if choice == 1:
        min = int(input("Enter minimum limit of number : "))
        max = int(input("Enter maximum limit of number : "))
        if min < 1 or min > max:
            raise ValueError("Must greather than 1 and min number less than max number")
        prime_nums = prime_selector(min, max)

        # max row
        max_row = 100
        # for loop to print table in max_row
        for x in range(0, len(prime_nums), max_row):
            table = PrettyTable()
            table.field_names = ["No", "Prime Numbers"]

            for i, prime in enumerate(prime_nums[x : x + max_row], start=x + 1):
                table.add_row([i, prime])
            print(f"Prime number {min} to {max}, Table {x//max_row + 1} : \n{table}")
            print("\n" + "-" * 40 + "\n")

        main()
    elif choice == 2:
        num_to_check = int(input("Enter a number to check if it's prime: "))
        if is_prime(num_to_check):
            print(f"{num_to_check} is a prime number.")
        else:
            print(f"{num_to_check} is not a prime number.")
        main()
    elif choice == 3:
        min = int(input("Enter minimum limit of number : "))
        max = int(input("Enter maximum limit of number : "))
        prime_sum = sum_primes(min, max)
        print(f"Sum of prime numbers from {min} to {max}: {prime_sum}")
        main()
    elif choice == 4:
        sys.exit("Bye \U0001F44B")
    else:
        main()


def main():
    """
    Main function for the Prime Numbers Generator program.

    Prompts the user to choose from a menu of options:
    1. Show prime numbers specified from  a minimum number to a  maximum number.
    2. Check if a given number is prime.
    3. Calculate the sum of all prime numbers in a specified range.
    4. Exit the program.

    :return: None
    """
    print("\n" + "-" * 60 + "\n")
    print("Prime numbers generator")
    print("Select one of the menu bellow:")
    print("1. Show prime numbers from minimum number to maximum number")
    print("2. Check a number is a prime or not")
    print("3. Count all prime number in range minumum number to maximum number")
    print("4. Exit from program")
    print("\n" + "-" * 60 + "\n")
    choice = int(input("Enter your choice (1, 2, 3 or 4): "))
    menu(choice)


if __name__ == "__main__":
    main()
