import heapq
import time 
# using heap data structure
class shortestDistance:
    def findShortestDistance(points:list[list[int]], topk:int):
        result=[]
        minQue=[]
        for point in points:
            dist=0
            for cordinate in point:
                dist+=cordinate**2
            minQue.append([dist, point])
            heapq.heapify(minQue)
        while topk > 0 :
            dist, point=heapq.heappop(minQue)
            result.append(point)
            topk-=1
        return result
# eventhough this looks short but it take longer time to execute.
    def findShortestDistance1(points:list[list[int]], topk:int):
        points.sort(key = lambda k:k[0]**2+k[1]**2+k[2]**2)
        return points[:topk]
    

if __name__ == "__main__":
    p=[[1,2,3], [1,3,4], [-1,-5,-8], [4,3,5],[0,1,0],[0,0,1]]
    k=2
    sol=shortestDistance
    print(time.time())
    print(sol.findShortestDistance(p,k))   
    print(time.time())
    print(time.time())         
    print(sol.findShortestDistance1(p,k)) 
    print(time.time())  
    