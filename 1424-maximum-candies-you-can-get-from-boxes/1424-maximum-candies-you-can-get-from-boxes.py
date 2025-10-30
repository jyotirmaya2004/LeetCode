from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:

        boxes = deque(initialBoxes)
        total_candies = 0
        while boxes:
            box = boxes.popleft()

            if status[box] != 1:
                status[box] = -1
                continue

            total_candies += candies[box]

            for new_box in containedBoxes[box]:
                boxes.append(new_box)

            for key in keys[box]:
                if status[key] == -1:
                    boxes.append(key)
                status[key] = 1
            
        return total_candies