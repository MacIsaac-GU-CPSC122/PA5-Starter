# NOTE: do not modify the contents of this file
import pytest

from array_queue import ArrayQueue, Empty
from sieve import Sieve


# NOTE: order is actual/received student value, expected/solution
def test_standard_queue_ops():
    q = ArrayQueue()

    # enqueue, size, is_empty
    q.enqueue(1)
    assert len(q) == 1
    assert q.is_empty() is False

    q.enqueue(2)
    assert len(q) == 2
    assert q.is_empty() is False

    # dequeue
    val = q.dequeue()
    assert val == 1
    assert len(q) == 1
    assert q.is_empty() is False

    val = q.dequeue()
    assert val == 2
    assert len(q) == 0
    assert q.is_empty() is True

    # both
    for i in range(1, 6):
        q.enqueue(i)
        assert len(q) == i

    for i in range(5, 0, -1):
        val = q.dequeue()
        assert val == 5 - i + 1
        assert len(q) == i - 1

    # clear
    for i in range(1, 6):
        q.enqueue(i)
        assert len(q) == i

    assert len(q) == 5
    q.clear()
    assert len(q) == 0
    assert q.is_empty() is True
    with pytest.raises(Empty):
        q.peek()
    with pytest.raises(Empty):
        q.dequeue()

def drain_queue(q: ArrayQueue) -> list[int]:
    """Helper function to remove and return all queue contents in FIFO order.
    """
    vals = []
    while not q.is_empty():
        vals.append(q.dequeue())
    return vals

def test_remove_divisible_by():
    q = ArrayQueue()
    for x in [1, 2, 3, 4]:
        q.enqueue(x)

    q.remove_divisible_by(2)
    assert drain_queue(q) == [1, 3]

    q = ArrayQueue()
    for x in [1, 2, 3, 4]:
        q.enqueue(x)

    q.remove_divisible_by(3)
    assert drain_queue(q) == [1, 2, 4]

def test_compute_primes():
    s = Sieve()

    s.set_n(20)
    s.compute_primes()
    num_primes, primes_percent = s.report_results()
    assert num_primes == 8
    assert primes_percent == pytest.approx(40.0)

    s.set_n(100)
    s.compute_primes()
    num_primes, primes_percent = s.report_results()
    assert num_primes == 25
    assert primes_percent == pytest.approx(25.0)

    s.set_n(1000)
    s.compute_primes()
    num_primes, primes_percent = s.report_results()
    assert num_primes == 168
    assert primes_percent == pytest.approx(16.8)