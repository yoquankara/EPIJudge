from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import namedtuple


class Stack:
    MaxStartIdx = namedtuple('MaxStartIdx', ('max', 'start_idx'))

    def __init__(self):
        self.stack = []
        self.max_idx = []

    def empty(self) -> bool:
        # TODO - you fill in here.
        return len(self.stack) == 0

    def max(self) -> int:
        # TODO - you fill in here.
        if self.empty():
            raise RuntimeError("Stack is empty")
        else:
            return self.max_idx[-1].max

    def pop(self) -> int:
        # TODO - you fill in here.
        if self.empty():
            raise RuntimeError("Stack is empty")
        e = self.stack.pop()
        if self.max_idx[-1].start_idx == len(self.stack):
            self.max_idx.pop()
        return e

    def push(self, x: int) -> None:
        # TODO - you fill in here.
        if self.empty() or self.max() < x:
            self.max_idx.append(Stack.MaxStartIdx(x, len(self.stack)))
        self.stack.append(x)


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
