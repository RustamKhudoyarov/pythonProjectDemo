import memory_profiler


@memory_profiler.profile
def custom_load_func():
    i = [i for i in range(0, 100000)]
    some_calc = [num % 3 * 100 for num in range(0, 150000)]
    del i
    return some_calc


custom_load_func()

if __name__ == '__main__':
    custom_load_func()
