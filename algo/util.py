import itertools


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
        res = list[i : i + step]
        if len(res) < step:
            return
        yield tuple(res)
