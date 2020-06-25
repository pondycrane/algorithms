import collections
import typing

import base.solution

class Solution(base.solution.Solution):

    """
    Bruteforce with bad iteration, overtime!!
    Because at every level we need to iterate all numbers.
    """
    def can_partition_k_subsets(self, nums: typing.List[int], k: int) -> bool:
        if not nums:
            return k == 0
        nums.sort()
        total = sum(nums)
        p_target = total / k
        if p_target % 1 != 0:
            return False
        
        count = collections.defaultdict(int)
        for num in nums:
            count[num] += 1

        def partitionable(count, cur, p_target, p_size):
            if cur > p_target:
                return False
            elif cur == p_target:
                p_size -= 1
                if p_size == 0:
                    return True
                cur = 0
            
            for num, c in count.items():
                if count[num] > 0:
                    count[num] -= 1
                    if partitionable(count, cur + num, p_target, p_size):
                        return True
                    count[num] += 1
            
            return False
            
        return partitionable(count, 0, p_target, k)
