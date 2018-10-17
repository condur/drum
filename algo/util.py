import itertools, time


def partition_iterable(iterable, step, pad=0):
    """
    Returns a lazy sequence of lists of n items each, at offsets
    step apart. If step is not supplied, defaults to n, i.e.
    the partitions do not overlap. If a pad collection is supplied,
    use its elements as necessary to complete last partition upto
    n items. In case there are not enough padding elements, return
    a partition with less than n items.
    """
    pad = step if pad == 0 else pad
    start, stop = 0, step
    item = tuple(itertools.islice(iterable, start, stop))
    while item:
        yield item
        start, stop = start + pad, stop + pad
        item = tuple(itertools.islice(iterable, start, stop))


def partition(list, step, pad=0):
    """
    Returns a lazy sequence of lists of n items each, at offsets
    step apart. If step is not supplied, defaults to n, i.e.
    the partitions do not overlap. If a pad collection is supplied,
    use its elements as necessary to complete last partition upto
    n items. Stop in case there are not enough padding elements.
    """
    pad = step if pad == 0 else pad
    for i in range(0, len(list), pad):
        res = list[i : i + step]  # noqa E203
        if len(res) < step:
            return
        yield tuple(res)


def preudo_random_generator(n, total=5):
    """
    Linear congruential generator implementation 
    """

    def lcg(n, seed):
        """
        Linear congruential generator
        https://en.wikipedia.org/wiki/Linear_congruential_generator
        
        Parameters:
            The same as for Java's java.util.Random, POSIX, glibc
            modulus m: 2 ** 48
            multiplier a: 25214903917
            increment c: 11

        Args:
            n (int): the top limit
            seed (int): a number used to initialize a
                        pseudorandom number generator. 

        Yields:
            int: random numbers in the n limit
        """
        modulus = 2 ** 48
        a = 25214903917
        c = 11
        while True:
            seed = (a * seed + c) % modulus
            yield (seed % n) + 1

    seed = int(time.time())
    return itertools.islice(lcg(n, seed), total)
