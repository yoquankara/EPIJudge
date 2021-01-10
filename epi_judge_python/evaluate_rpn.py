from test_framework import generic_test


def evaluate(expression: str) -> int:
    # TODO - you fill in here.
    if not expression:
        return 0
    stack = []
    ops = {'+': lambda y, x: x + y,
           '-': lambda y, x: x - y,
           '*': lambda y, x: x * y,
           '/': lambda y, x: x // y}
    for c in expression.split(','):
        if c in ops:
            stack.append(ops[c](stack.pop(), stack.pop()))
        else:
            stack.append(int(c))

    return stack.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
