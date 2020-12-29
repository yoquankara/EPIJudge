from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # TODO - you fill in here.
    ret = 0.0
    buy, sell = 0, 1
    while buy < len(prices)-1:
        while sell < len(prices) and prices[sell] >= prices[buy]:
            ret = max(ret, prices[sell] - prices[buy])
            sell += 1
        if sell == len(prices) -1:
            break
        else:
            buy = sell
    return ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
