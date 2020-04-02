import collections

import base.solution
import lib.ds_collections.treenode as treenode

class Solution(base.solution.Solution):
    def single_number(self, arr: list) -> None:
        num = 0
        for n in arr:
            num ^= n
        
        return num ^ (0 ^ 0)