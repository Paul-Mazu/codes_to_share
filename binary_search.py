from operator import index
from random import randint
import time
import matplotlib.pyplot as plt

def time_counter(n):
    def wrapper(fn):
        def inner(*args, **kwargs):
            times = []
            for i in range(n):
                start = time.time()
                fn(*args, **kwargs)
                finish = time.time()
                times.append(finish - start)
            return sum(times)/len(times)
        return inner
    return wrapper


@time_counter(10)
def binary_search(lst: list, number: int) -> int:
    if number < lst[0]: return None

    left = 0
    right = len(lst)-1
    
    while left <= right:
        index = (left + right) // 2
        if lst[index] == number:
            return lst[index]
        elif lst[index] < number:
            left = index + 1
        else: right = index

@time_counter(10)
def normal_search(lst, number):
    for i in lst:
        if i == number: return i

@time_counter(10)
def aljoscha_search(lst, number):
    if number in lst: return lst[index(number)]


def create_ranges(ranges):
    lst = []
    for i in ranges:
        lst.append(list(range(i)))
    return lst

# returns random number from the range
def produce_random_number(rang):
    return randint(0, rang)

# make ranges out of the list
list_of_ranges = [10, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]
table_of_ranges = create_ranges(list_of_ranges)

# lists of average times
lst_of_times_binary = [binary_search(a_range, produce_random_number(len(a_range))) for a_range in table_of_ranges]

lst_of_times_normal = [normal_search(a_range, produce_random_number(len(a_range))) for a_range in table_of_ranges]

lst_of_times_aljoscha = [aljoscha_search(a_range, produce_random_number(len(a_range))) for a_range in table_of_ranges]


plt.plot(list_of_ranges, lst_of_times_binary, label='binary')
plt.plot(list_of_ranges, lst_of_times_normal, label='iteration')
plt.plot(list_of_ranges, lst_of_times_aljoscha, label='aljoscha_search')
plt.legend()
plt.title('O notation')
plt.xlabel('size')
plt.ylabel('time')
plt.show()