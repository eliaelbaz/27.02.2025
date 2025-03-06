import sys
import gc
import weakref
from memory_profiler import profile
# 1
a = []
print(sys.getrefcount(a))
# 2
lst = [1, 2, 3, 4, 5]
print(sys.getsizeof(lst))
# 3
print(gc.get_count())
# 4
gc.collect()
# 5
gc.disable()
gc.enable()
# 6
class MyClass:
    pass

obj = MyClass()
weak_obj = weakref.ref(obj)
print(weak_obj())
del obj
print(weak_obj())
# 7
@profile
def main_processing_function():
    large_list = [i for i in range(10**6)]
    return sum(large_list)

if __name__ == "__main__":
    main_processing_function()