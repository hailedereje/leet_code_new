class Solution:
      def largestNumber(self,nums: list[int]):
            for i ,n in enumerate(nums):
                nums[i] = str(n)
            def comparator(n1,n2):
                if n1 +n2 >n2+n1:
                    return -1
                else:
                    return 1
            nums = sorted(nums, key=cmp_to_key(comparator))
            if nums[0] == '0' :
                return '0'
            else:

                return ''.join(nums)
            return ''.join(nums)
        