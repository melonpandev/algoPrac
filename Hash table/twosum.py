class Solution:
    def twosum(self,list: [],target: int) -> [int,int]:
        hmap={}
        for i in range(len(list)):
            complement=target-list[i]
            if hmap.get(complement)==None:
                hmap[list[i]]=i
            else:
                return [hmap.get(complement),i]
