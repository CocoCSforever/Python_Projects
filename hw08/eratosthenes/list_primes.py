from prime_generator import PrimeGenerator


def main():
    pg = PrimeGenerator()
    n = int(input("Please enter the max value:"))
    print(pg.primes_to_max(n))


main()
