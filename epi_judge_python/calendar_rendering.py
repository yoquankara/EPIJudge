import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    # Note: If end time of event A is the same as start time of event B then A and B are concurrent
    Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))
    E = [
        p for event in A
        for p in (Endpoint(event.start, True), Endpoint(event.finish, False))
    ]
    E.sort(key=lambda e: (e.time, not e.is_start))  # start time before end time
    max_events, events_cnt = 0, 0
    for e in E:
        if e.is_start:
            events_cnt += 1
        else:
            max_events = max(max_events, events_cnt)
            events_cnt -= 1

    return max_events


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
