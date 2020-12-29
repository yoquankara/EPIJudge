from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # TODO - you fill in here.
    ret = 0.0
    buy = 0
    for i in range(len(prices)):
        if prices[i] > prices[buy]:
            ret = max(ret, prices[i] - prices[buy])
        elif prices[i] < prices[buy]:
            buy = i
    return ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
