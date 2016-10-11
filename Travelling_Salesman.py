# Travelling  Salesman Problem DP Solution
# Author: Haiyuan Cao

class Solution(object):
    def tsp_rec_solve(d):
        def rec_tsp_solve(c, ts):
            assert c not in ts
            if ts:
                return min((d[lc][c] + rec_tsp_solve(lc, ts - set([lc]))[0], lc)
                           for lc in ts)
            else:
                return (d[0][c], 0)

        best_tour = []
        c = 0
        cs = set(range(1, len(d)))
        while True:
            l, lc = rec_tsp_solve(c, cs)
            if lc == 0:
                break
            best_tour.append(lc)
            c = lc
            cs = cs - set([lc])

        best_tour = tuple(reversed(best_tour))

        return best_tour
