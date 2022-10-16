# 1475. 商品折扣后的最终价格（简单）
# 给你一个数组prices，其中prices[i]是商店里第i件商品的价格。
# 商店里正在进行促销活动，如果你要买第i件商品，那么你可以得到与 prices[j] 相等的折扣，
# 其中j是满足j > i且prices[j] <= prices[i]的最小下标，如果没有满足条件的j，你将没有任何折扣。
# 请你返回一个数组，数组中第i个元素是折扣后你购买商品 i最终需要支付的价格。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/final-prices-with-a-special-discount-in-a-shop
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = list()
        nums = len(prices)
        result = [0 for _ in range(nums)]
        prices.append(0)
        for i in range(nums + 1):
            while stack and stack[-1][0] >= prices[i]:
                p, j = stack.pop()
                result[j] = p - prices[i]
            stack.append([prices[i], i])
        return result

prices = [8,4,6,2,3]
#输出：[4,2,4,2,3]
test = Solution()
print(test.finalPrices(prices))

