def minAreaRect(self, points: List[List[int]]) -> int:
    seen = set()
    area = sys.maxsize
    flag = True
    for x1,y1 in points:
        for x2,y2 in seen:
            if (x1,y2) in seen and (x2,y1) in seen:
                temp = abs(x2-x1) * abs(y2-y1)
                area = min(temp,area)
        seen.add((x1,y1))
    return area if area < sys.maxsize else 0


points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
print(minAreaRect(points))

