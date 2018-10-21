class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand) % W != 0: return False
        if W == 0: return True
        if W == 1 and len(hand) != 0: return True
        dicts = {}
        for card in hand:
            dicts[card] = dicts.get(card, 0) + 1

        keys = sorted(dicts.keys())
        j = 0
        while dicts:
            # print dicts
            start = keys[j]
            if start not in dicts:
                j += 1
                continue
            for i in xrange(W):
                if start + i in dicts:
                    dicts[start + i] -= 1
                else:
                    return False
                if dicts[start + i] == 0:
                    del dicts[start + i]
        return True


