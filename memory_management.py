import sys
import gc
import weakref
from memory_profiler import profile


def check_references():
    obj = [1, 2, 3]
    print(f"Number of strong references to the object: {sys.getrefcount(obj)}")

def measure_memory():
    lst = [i for i in range(1000)]
    print(f"Memory size of the list: {sys.getsizeof(lst)} bytes")

def gc_status():
    print(f"GC status: {gc.get_count()}")

def manual_gc_collection():
    gc.collect()
    print("Garbage collection performed!")

def disable_and_enable_gc():
    print("Disabling GC...")
    gc.disable()
    print("Is GC enabled?", gc.isenabled())

    print("Enabling GC...")
    gc.enable()
    print("Is GC enabled?", gc.isenabled())

def weak_reference_demo():
    class MyClass:
        pass

    obj = MyClass()
    weak_obj = weakref.ref(obj)

    print(f"Object before deletion: {weak_obj()}")
    del obj
    print(f"Object after deletion: {weak_obj()}")

@profile
def memory_intensive_function():
    large_list = [i for i in range(10**6)]
    print("Finished creating a large list")
    del large_list
    gc.collect()

def main():
    print("\n Checking strong references count")
    check_references()

    print("\n Measuring list memory size")
    measure_memory()

    print("\n Checking GC status before cleanup")
    gc_status()

    print("\n Manually triggering garbage collection")
    manual_gc_collection()

    print("\n Disabling and enabling GC")
    disable_and_enable_gc()

    print("\n Demonstrating weak reference usage")
    weak_reference_demo()

    print("\n Running a memory-intensive function")
    memory_intensive_function()

if __name__ == "__main__":
    main()
