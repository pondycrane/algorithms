import typing

import base.solution

class Solution(base.solution.Solution):
    def three_sum(self, arr) -> typing.List[int]:
        res = []
        arr.sort()
        for i in range(0, len(arr) - 2):
            if i > 0 and arr[i - 1] == arr[i]:
                continue

            j, g = i + 1, len(arr) - 1
            while j < g:
                total = arr[i] + arr[j] + arr[g]
                if total == 0:
                    res.append([arr[i], arr[j], arr[g]])
                    j += 1
                    while j < g and arr[j] == arr[j - 1]:
                        j += 1

                    g -= 1
                    while j < g and arr[g] == arr[g + 1]:
                        g -= 1
                elif total > 0:
                    g -= 1
                else:
                    j += 1
        return res