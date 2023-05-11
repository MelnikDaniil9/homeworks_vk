import cProfile
import functools
import time
import weakref


def profile_deco(func):
    profiler = cProfile.Profile()

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        return result

    def print_stat():
        profiler.print_stats()

    wrapper.print_stat = print_stat
    return wrapper


class MyClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class MySlotClass:
    __slots__ = ["a", "b", "c"]

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class MyWeakRefClass:
    def __init__(self, a, b, c):
        self.a = weakref.ref(a)
        self.b = weakref.ref(b)
        self.c = weakref.ref(c)


class PassClass:
    pass


@profile_deco
def run_my_class(n):
    start_time = time.time()
    objs = [MyClass(1, 2, 3) for _ in range(n)]
    print("time create MyClass:", time.time() - start_time)

    start_time = time.time()
    for o in objs:
        o.a += 1
        o.b += 10
        o.c = 0
    print("time update MyClass:", time.time() - start_time)


@profile_deco
def run_my_slots_class(n):
    start_time = time.time()
    objs_slots = [MySlotClass(1, 2, 3) for _ in range(n)]
    print("time create MySlotClass:", time.time() - start_time)

    start_time = time.time()
    for o in objs_slots:
        o.a += 1
        o.b += 10
        o.c = 0
    print("time update MySlotClass:", time.time() - start_time)


@profile_deco
def run_my_weakref_class(n):
    start_time = time.time()
    objs_weakref = [
        MyWeakRefClass(MyClass(1, 2, 3), MyClass(4, 5, 6), MyClass(7, 8, 9))
        for _ in range(n)
    ]
    print("time create MyWeakRefClass:", time.time() - start_time)

    start_time = time.time()
    for o in objs_weakref:
        o.a = MyClass(9, 8, 7)
        o.b = MyClass(6, 5, 4)
        o.c = MyClass(3, 2, 1)
    print("time update MyWeakRefClass:", time.time() - start_time)

    start_time = time.time()
    for o in objs_weakref:
        o.a = PassClass()
        o.b = PassClass()
        o.c = PassClass()
    print("time update pass MyWeakRefClass:", time.time() - start_time)


if __name__ == "__main__":
    n = 10**7
    run_my_class(n)
    run_my_class(n)
    run_my_slots_class(n)
    run_my_weakref_class(n)
    run_my_class.print_stat()
    run_my_slots_class.print_stat()
    run_my_weakref_class.print_stat()
