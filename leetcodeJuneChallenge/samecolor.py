def sortColors(nums):
	for i in range(len(nums)):
		for j in range(i, len(nums)):
			if nums[i] > nums[j]:
				temp = nums[i]
				nums[i] = nums[j]
				nums[j] = temp

	print(nums)		




nums = [2,0,2,1,1,0]
sortColors(nums)

# US project

# canada
# SQL, PYTHON, Front end visualization (Sunand, )
# colleges, exp in python, in sql and frontend tech power BI, tablue 
# 