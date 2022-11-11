class PrimeGenerator:
    def __init__(self):
        self.list = []
        self.set = set()

    def primes_to_max(self, n):
        """Construct a list of prime number and add composite to set"""
        for i in range(2, n+1):
            if i in self.set:
                continue
            self.list.append(i)
            self.add_composite(i, n)
        return self.list

    def add_composite(self, p, n):
        """Add multiples of p (from 2p to n) to set"""
        for i in range(2, n//p + 1):
            self.set.add(i*p)
