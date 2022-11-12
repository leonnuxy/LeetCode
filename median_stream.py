class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
       self.arr.append(num) 

    def findMedian(self) -> float:
        self.arr = sorted(self.arr)
        l = len(self.arr)
        if l%2 == 0:
            return (self.arr[l//2] + self.arr[(l//2)-1])/2
        
        else:
            return self.arr[l//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


if __name__ == "__main__":
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())
    obj.addNum(4)
    print(obj.findMedian())
    obj.addNum(5)
    print(obj.findMedian())
    obj.addNum(6)
    print(obj.findMedian())