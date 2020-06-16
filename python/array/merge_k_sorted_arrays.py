import typing

import base.solution

class Solution(base.solution.Solution):
    def merge_k_sorted_arrays(self, arr: typing.List[int]) -> typing.List[int]:
        # Use merge sort
        # T: O(NlogN)
        if not arr:
            return []
        
        ascending = True
        for l in arr:
            if len(l) > 1 and l[-1] < l[0]:
                ascending = False
                break
        
        def merge(l1, l2, smaller=True):
            nonlocal ascending
            merged = []
            i = j = 0
            while i < len(l1) and j < len(l2):
                if ascending and l1[i] < l2[j] or not ascending and l1[i] > l2[j]:
                    merged.append(l1[i])
                    i += 1
                else:
                    merged.append(l2[j])
                    j += 1
            merged.extend(l1[i:])
            merged.extend(l2[j:])
            return merged

        def devide_n_conquer(left, right):
            if left == right:
                return arr[left]
            elif right == left + 1:
                return merge(arr[left], arr[right])
            
            mid = (right - left) // 2 + left
            return merge(
                devide_n_conquer(left, mid),
                devide_n_conquer(mid + 1, right)
            )
        
        return devide_n_conquer(0, len(arr) - 1)