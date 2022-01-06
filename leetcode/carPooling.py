class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        time_lst = []
        curr = 0
        for n,i,j in trips:
            time_lst.append([i, n])
            time_lst.append([j, -n])
        
        time_lst.sort()
        for j,n in time_lst:
            curr += n
            if curr>capacity:
                return False
        
        return True