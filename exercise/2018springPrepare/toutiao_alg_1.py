import sys
def getboarder(points):
    points.sort(key=lambda p: (-p[1], p[0]))  # sort by y
    print(points)
    lastX = -1
    result = []
    for p in points:
        if lastX < p[1]:
            print("L", lastX)
            result.append(p)
            lastX = p[0]
    return result

if __name__ == "__main__":
    list = [(2, 2), (2, 3), (1, 2), (1, 3), (1, 4)]
    with open("D:\\work_space\\Algorithm_practice_py\\AlgorithmTraining\\exercise\\2018springPrepare\\p1") as f:
        line = f.readline()
        nums = line.split()
        N = nums[0]
        pointList = [(int(nums[i]), int(nums[i + 1])) for i in range(1, len(nums), 2)]
        for p in getboarder(pointList):
            print(p[0], p[1])
