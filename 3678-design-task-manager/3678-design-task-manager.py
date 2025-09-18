from sortedcontainers import SortedList

class TaskManager:
    def __init__(self, tasks: list[list[int]]):
        # map taskId → (userId, priority)
        self.task_info = {}
        # sorted list of keys to pick execTop
        # store tuples like (-priority, -taskId) so that when you do .pop(0),
        # you get the highest priority, highest taskId
        self.sorted_tasks = SortedList()
        
        # initialize
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)
    
    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_info[taskId] = (userId, priority)
        self.sorted_tasks.add((-priority, -taskId))
    
    def edit(self, taskId: int, newPriority: int) -> None:
        userId, oldPriority = self.task_info[taskId]
        # remove old entry
        self.sorted_tasks.discard((-oldPriority, -taskId))
        # update
        self.task_info[taskId] = (userId, newPriority)
        # add new entry
        self.sorted_tasks.add((-newPriority, -taskId))
    
    def rmv(self, taskId: int) -> None:
        userId, priority = self.task_info.pop(taskId)
        self.sorted_tasks.remove((-priority, -taskId))
    
    def execTop(self) -> int:
        if not self.sorted_tasks:
            return -1
        # get the top task (first in sorted list, since we stored negatives)
        neg_priority, neg_taskId = self.sorted_tasks.pop(0)
        taskId = -neg_taskId
        userId, _ = self.task_info.pop(taskId)
        return userId
