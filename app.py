class Solution:

    def longestCommonPrefix(self, strs: list[str]) -> str:
        self.strs = strs

        if not self.strs:
            return ""

        prefix = self.strs[0]

        for string in self.strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]

                if not prefix:
                    return ""

        return prefix


solution = Solution()
longest_common_prefix = solution.longestCommonPrefix(["flow", "flower", "flight"])
# print(longest_common_prefix)


print("flower".startswith("flow"))
