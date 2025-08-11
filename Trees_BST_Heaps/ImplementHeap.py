# sabse phele library import karni hoti hee
import heapq

h = []
heapq.heapify(h)
# yeeh naa reorder karta
# Heapify: Only guarantees that the smallest element is at index 0,
# and the heap structure is valid for fast insertion/removal  the rest of the list isn’t fully sorted.

# heapq.heapify() doesn’t sort the list it just rearranges it so that it follows the heap property.

# sorting jesa nhi hota okk yeeh
# isse kya hoga pata hee empty list banega
# aur by default min heap banega small value root prr rehti vooh vala

# min heap raha toh minimum number top pee hota he

# heapq.heappush(argument,value)
# appending and element
heapq.heappush(h, 5)
heapq.heappush(h, 3)
heapq.heappush(h, 2)
heapq.heappush(h, 6)

print(heapq.heappop(h))  # sab chota element pop hoga okk

# yeeh vala bhi method hota joo hume n largest
# dega number secify krr sakhte
print(heapq.nlargest(2, h))
# toh yeeh naa apko 2 largest number dega in heap

# ================== EXTRA IMPORTANT HEAP METHODS FOR DSA ==================

# 1. heapq.nsmallest(k, iterable) → k smallest elements from the heap/iterable
print(heapq.nsmallest(2, h))  # 2 smallest values

# 2. heapq.heappushpop(heap, value) → Push new value and pop smallest in one step (more efficient than push + pop)
print(heapq.heappushpop(h, 1))  # pushes 1, pops smallest, returns popped value

# 3. heapq.heapreplace(heap, value) → Pop smallest & push new value (heap must not be empty)
print(heapq.heapreplace(h, 4))  # pops smallest, inserts 4

# 4. Max Heap in Python → By default heapq is Min Heap, so for Max Heap we insert negative values
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -2)
heapq.heappush(max_heap, -8)
print(-heapq.heappop(max_heap))  # max value pop

# 5. Converting a normal list to a heap in O(n)
nums = [9, 4, 7, 1, 3]
heapq.heapify(nums)
print(nums)  # Now nums follows heap property (min at index 0)
