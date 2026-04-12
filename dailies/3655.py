MOD = 10**9 + 7

class Solution(object):
    def xorAfterQueries(self, nums, queries):
        from collections import defaultdict

        n = len(nums)
        groups = defaultdict(list)
        for l, r, k, v in queries:
            groups[(k, l % k)].append((l, r, v))

        for (k, rem), qs in groups.items():
            idxs = list(range(rem, n, k))
            m = len(idxs)
            pos = {idx: i for i, idx in enumerate(idxs)}
            diff = [1] * (m + 1)
            for l, r, v in qs:
                start = pos[l]
                end_idx = r - ((r - l) % k)
                end = pos[end_idx]

                diff[start] = diff[start] * v % MOD
                diff[end + 1] = diff[end + 1] * pow(v, MOD - 2, MOD) % MOD

            cur = 1
            for i in range(m):
                cur = cur * diff[i] % MOD
                nums[idxs[i]] = nums[idxs[i]] * cur % MOD

        out = 0
        for x in nums:
            out ^= x
        return out
