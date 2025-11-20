class MyHeap:
    def __init__(self, data, reverse=False):
        if reverse:
            data = [(-x, -y) for x, y in data]
        self.data = data
        self.reverse = reverse
        self.len = len(data)
        self.valid = Counter(self.data)
        heapq.heapify(self.data)

    def push(self, x):
        if self.reverse:
            x = -x[0], -x[1]
        self.valid[x] += 1
        self.len += 1
        heapq.heappush(self.data, x)
    
    def rm(self, x):
        if self.reverse:
            x = -x[0], -x[1]
        self.valid[x] -= 1
        self.len -= 1

    def pop(self):
        out = None
        while not self.valid[out]:
            out = heapq.heappop(self.data)
        self.valid[out] -= 1
        self.len -= 1
        if self.reverse:
            out = -out[0], -out[1]
        return out

    def peek(self):
        out = self.data[0]
        while not self.valid[out]:
            heapq.heappop(self.data)
            out = self.data[0]
        if self.reverse:
            out = -out[0], -out[1]
        return out

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        cnt = Counter(nums[:k])
        scnt = sorted([i[::-1] for i in cnt.items()])
        big = MyHeap(scnt[-x:])
        small = MyHeap(scnt[:-x], reverse=True)
        # print(big.data, small.data)
        cus = sum([c * v for c, v in big.data])
        ans = [cus]
        for i, ni in enumerate(nums[k:], k):
            oni = nums[i - k]
            if oni == ni:
                ans.append(cus)
                continue
            if cnt[ni]:
                ele = cnt[ni], ni
                if big.valid[ele]:
                    big.rm(ele)
                    cus -= ele[0] * ele[1]
                else:
                    small.rm(ele)
            cnt[ni] += 1
            ele = cnt[ni], ni
            if big.len and ele >= big.peek():
                big.push(ele)
                cus += ele[0] * ele[1]
            else:
                small.push(ele)

            ele = cnt[oni], oni
            if big.valid[ele]:
                big.rm(ele)
                cus -= ele[0] * ele[1]
            else:
                small.rm(ele)
            cnt[oni] -= 1
            if cnt[oni]:
                ele = cnt[oni], oni
                if big.len and ele >= big.peek():
                    big.push(ele)
                    cus += ele[0] * ele[1]
                else:
                    small.push(ele)
            while big.len > x:
                ele = big.pop()
                cus -= ele[0] * ele[1]
                small.push(ele)
            while big.len < x and small.len:
                ele = small.pop()
                cus += ele[0] * ele[1]
                big.push(ele)
            ans.append(cus)
        return ans