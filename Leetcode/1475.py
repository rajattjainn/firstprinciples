class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        idxs = []
        discount = [-1] * len(prices)

        i = 0
        while i < len(prices):
            p = prices[i]
            if not idxs or p > prices[idxs[-1]]:
                idxs.append(i)
                i += 1
            else:
                index = idxs.pop()
                discount[index] = prices[index] - p
        
        while idxs:
            index = idxs.pop()
            discount[index] = prices[index]

        return discount
