total_sum = 0
grade_sum = 0
grade_point = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}
for _ in range(20):
    nums = list(input().split())
    if nums[2] in grade_point:
        total_sum += float(nums[1]) * grade_point[nums[2]]
        grade_sum += float(nums[1])



print(total_sum/grade_sum)
