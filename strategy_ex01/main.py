import time
from sums import sum_list1, sum_list2, sum_list3
from strategy import sum_list


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [x for x in range(1, 1000)]
list3 = [x for x in range(1, 1_000_000)]

used_list = list3

# Checking performance of methods
print(f"Testing performance for {len(used_list)} elements.")
to = time.perf_counter()
sum_list1(used_list)
ti = time.perf_counter()
print(f"Elapsed time: {ti - to:.4f} sec.")

to = time.perf_counter()
sum_list2(used_list)
ti = time.perf_counter()
print(f"Elapsed time: {ti - to:.4f} sec.")

to = time.perf_counter()
sum_list3(used_list)
ti = time.perf_counter()
print(f"Elapsed time: {ti - to:.4f} sec.")


# Applying strategy
print("\nApplied strategy")
to = time.perf_counter()
sum_list(used_list)
ti = time.perf_counter()
print(f"Elapsed time: {ti - to:.4f} sec.")