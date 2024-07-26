from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = [1]
        product = 1
        for i in range(1, len(nums)):
            product *= nums[i-1]
            prefix_products.append(product)
        postfix_products = [1]
        product = 1
        for i in range(len(nums) - 2, -1, -1):
            product *= nums[i+1]
            postfix_products.append(product)

        postfix_products.reverse()

        return [
            prefix_products[i] * postfix_products[i]
            for i in range(len(nums))
            ]


s = Solution()
print(s.productExceptSelf([-1, 1, 0, -3, 3]))
