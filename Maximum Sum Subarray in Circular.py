def circularSubarraySum(arr):
    n = len(arr)

    # Kadane's Algorithm to find max subarray sum (non-circular)
    def maxSubarraySum(nums):
        curr_sum = max_sum = nums[0]
        for num in nums[1:]:
            # Ya to current number lo, ya fir pichle sum me jod do (whichever is better)
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum

    # Step 1: Find non-circular max subarray sum
    normal_max = maxSubarraySum(arr)

    # Step 2: Total sum of array
    total_sum = sum(arr)

    # Step 3: Invert array for finding min subarray sum using same logic
    inverted_array = [-x for x in arr]
    inverted_max_sum = maxSubarraySum(inverted_array)
    min_sub_sum = -inverted_max_sum  # kyunki inverted array ka max == original ka min

    # Step 4: Max circular subarray sum
    circular_max = total_sum - min_sub_sum

    # Edge case: Agar saare elements negative hai to circular wala 0 ho jaayega
    if circular_max == 0:
        return normal_max

    return max(normal_max, circular_max)


# ✅ Test Example
if __name__ == '__main__':
    arr = [8, -8, 9, -9, 10, -11, 12]
    print("Maximum circular subarray sum is:", circularSubarraySum(arr))