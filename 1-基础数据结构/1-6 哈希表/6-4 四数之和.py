# 18 四数之和（中等）
# 类似《三数之和》
# https://leetcode.cn/problems/4sum
# 给你一个由 n 个整数组成的数组nums ，和一个目标值 target 。
# 请你找出并返回满足下述全部条件且不重复的四元组[nums[a], nums[b], nums[c], nums[d]]
# （若两个四元组元素一一对应，则认为两个四元组重复）

# 0 <= a, b, c, d< n
# a、b、c 和 d 互不相同
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 你可以按 任意顺序 返回答案 。

# 示例：
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]

# 方法1，排序+双指针
# https://leetcode.cn/problems/4sum/solution/si-shu-zhi-he-by-leetcode-solution/
# 对数组排序后，数值之和是递增，可以顺序排除相同项，可以比较容易地保证每个元素的确定都是不相同
# 先确定a和b，再双指针确定c和d

from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = list()
        # 数组元素小于4个，则不满足要求，直接退出
        if len(nums) < 4:
            return result
        # 对给定的整数数组进行排序
        nums.sort()
        n = len(nums)
        # 如果数组前四个数之和大于target，则后面怎么组合都大于target
        if nums[0] + nums[1] + nums[2] + nums[3] > target:
            return result
        # 如果数组后四个数之和小于target，则前面怎么组合都小于target
        if nums[n-4] + nums[n-3] + nums[n-2] + nums[n-1] < target:
            return result

        for a in range(n-3):
            # a为第二个索引，如果值与前一个相等，则跳过继续下个a
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1, n-2):
                if b > a+1 and nums[b] == nums[b-1]:
                    continue
                c = b+1
                d = n-1
                while c < d:
                    if c > b+1 and nums[c] == nums[c-1]:
                        c += 1
                        continue
                    if d < n-1 and nums[d] == nums[d+1]:
                        d -= 1
                        continue
                    sums = nums[a] + nums[b] + nums[c] + nums[d]
                    if sums == target:
                        result.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                    elif sums < target:
                        c += 1
                    else:
                        # nums[a] + nums[b] + nums[c] + nums[d] > target
                        d -= 1
        return result


nums = [-2,-1,-1,1,1,2,2]
target = 0
test = Solution()
print(test.fourSum(nums, target))


# 执行用时：500 ms, 在所有 Python3 提交中击败了73.18%的用户
# 内存消耗：14.9 MB, 在所有 Python3 提交中击败了85.93%的用户
# 通过测试用例：291 / 291

