import math
from array_queue import ArrayQueue


class Sieve:
    def __init__(self) -> None:
        self.n = 0
        self.nums_q = ArrayQueue()
        self.primes_q = ArrayQueue()

    def get_n(self) -> int:
        return self.n

    def set_n(self, n_param: int) -> None:
        self.n = n_param

    def compute_primes(self) -> None:
        pass # TODO: finish this

    def report_results(self) -> tuple[int, float]:
        print(f"Primes up to {self.n} are as follows:")
        num_primes = len(self.primes_q)
        prime_percent = 0.0
        if self.n != 0:
            prime_percent = (num_primes / self.n) * 100

        return num_primes, prime_percent