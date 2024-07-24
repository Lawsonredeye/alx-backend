# Caching

When we talk about caching, theres a lot to conisder and put into place, especially when thinking about a system to put in place.

Caching is just storing of data that is accessed the most from the database through client queries and it actually increases read speed when compared to traditional read from disk as the data is stored into memory.

## Types of Caching

There are several types of caching and they have different use cases and each use cases is dependent on the area of implementations.

They are:
1. FIFO => FIRST IN FIRST OUT
2. LIFO => LAST IN FIRST OUT
3. LRU => LEAST RECENTLY USED
4. MRU => MOST RECENTLY USED


# Limitations
Caching systems can greatly improve the performance of a system by storing frequently accessed data in a faster storage medium. However, they do have some limitations:

1. Size: Cache memory is typically smaller than main memory. This means that not all data can be stored in the cache, and the system must decide what to keep and what to discard.

2. Coherency: In a system with multiple caches, keeping the data consistent across all caches can be challenging. If one cache changes a piece of data, all other caches must be updated.

3. Complexity: Implementing a cache requires additional logic in the system, which can increase complexity.

4. Cost: Cache memory is typically faster and therefore more expensive than main memory. This can increase the overall cost of the system.

5. Cache misses: If the needed data is not in the cache (a cache miss), the system must retrieve it from the slower main memory, which can cause delays.

6. Eviction strategy: Deciding which items to remove from the cache when it's full can be complex. Different strategies (like Least Recently Used, Most Recently Used, etc.) have their own pros and cons.