def analyze_drive(lanes: list[int]) -> tuple[int, int]:
     count1 = count2 = 0
     for i in range(len(lanes)-1):
         diff = abs(lanes[i] - lanes[i + 1])
         if diff==1:
             count1 += 1
         elif diff==2:
             count2 += 1
             count1 += 1
     return count1, count2
