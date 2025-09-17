import heapq
from typing import List

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # Map each food -> (cuisine, rating)
        self.food_info = {}
        
        # Map each cuisine -> heap of (-rating, food)
        self.cuisine_heap = {}
        
        for f, c, r in zip(foods, cuisines, ratings):
            self.food_info[f] = [c, r]
            if c not in self.cuisine_heap:
                self.cuisine_heap[c] = []
            heapq.heappush(self.cuisine_heap[c], (-r, f))  # max-heap using negative rating

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.food_info[food]
        self.food_info[food][1] = newRating
        heapq.heappush(self.cuisine_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heap[cuisine]
        # Pop stale values until we find the current rating
        while heap:
            rating, food = heap[0]
            if -rating == self.food_info[food][1]:
                return food
            heapq.heappop(heap)
