class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.peeked = iterator.next()

    def peek(self):
        return self.peeked

    def next(self):
        current = self.peeked
        self.peeked = self.iterator.next() if self.iterator.hasNext() else None
        return current

    def hasNext(self):
        return self.peeked is not None