def twoSum(self, nums, target):
        seen = {}

        for i, number in enumerate(nums):
            complement = target - number

            if complement in seen:
                return [seen[complement], i]

            seen[number] = i
