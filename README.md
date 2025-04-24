# 🔄 Day-12: Maximum Circular Subarray Sum

Today's challenge dives into an enhanced variant of Kadane’s Algorithm. While Kadane finds the maximum subarray sum for a linear array, this problem explores a **circular array**, where the subarray can wrap around.

---

## 💡 Problem Statement

Given a circular array `arr`, calculate the **maximum sum of a contiguous subarray**, allowing the subarray to wrap around the end to the beginning.

---

## 🧠 Approach

To solve this, we consider two cases:

1. **Non-Circular Case (Standard Kadane)** – Just apply Kadane’s algorithm to find the max subarray sum.
2. **Circular Case** – The max circular subarray is equal to: Total Sum of Array - Minimum Subarray Sum

---
1. To compute the **min subarray sum**, we invert the array and run Kadane’s algorithm again.

2. Inverted max = -1 × original min.
#### Finally, return the **maximum** of the two cases.
---

## 🔁 Edge Case

If all elements are negative, the circular sum would incorrectly compute to 0. So we return the normal Kadane's result.

---

## 🧾 Python Code

```python
def circularSubarraySum(arr):
 n = len(arr)

 # Kadane's Algorithm
 def maxSubarraySum(nums):
     curr_sum = max_sum = nums[0]
     for num in nums[1:]:
         curr_sum = max(num, curr_sum + num)
         max_sum = max(max_sum, curr_sum)
     return max_sum

 # Step 1: Max subarray sum without circularity
 normal_max = maxSubarraySum(arr)

 # Step 2: Total sum
 total_sum = sum(arr)

 # Step 3: Min subarray sum using inverted array
 inverted_array = [-x for x in arr]
 inverted_max_sum = maxSubarraySum(inverted_array)
 min_sub_sum = -inverted_max_sum

 # Step 4: Max circular subarray sum
 circular_max = total_sum - min_sub_sum

 # Edge case: If all numbers are negative
 if circular_max == 0:
     return normal_max

 return max(normal_max, circular_max)

# Test Example
if __name__ == '__main__':
 arr = [8, -8, 9, -9, 10, -11, 12]
 print("Maximum circular subarray sum is:", circularSubarraySum(arr))
```
---
### ⏱️ Time & Space Complexity
Time: O(n)

Space: O(1)

---
# 📅 Challenge Tag
#gfg160 #geekstreak2025 #Day12
---

## ✍️ Author
Crafted with clarity by Vikash Joshi 🚀

