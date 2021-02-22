class Solution(object):
    def minMutation(self, start, end, bank):
        wordset = set(bank)
        if end not in wordset:
            return -1
        beginset = set([start])
        endset = set([end])
        visited = set([start, end])
        step = 0
        while beginset:
            if len(beginset) > len(endset):
                beginset, endset = endset, beginset
            next_level = set()
            for word in beginset:
                letters = list(word)
                for i in range(8):
                    ch = letters[i]
                    for x in ['A', 'C', 'G', 'T']:
                        letters[i] = x
                        cand_gene = "".join(letters)
                        if cand_gene in wordset:
                            if cand_gene in endset:
                                return step + 1
                            if cand_gene not in visited:
                                visited.add(cand_gene)
                                next_level.add(cand_gene)
                    letters[i] = ch
            step += 1
            beginset = next_level
        return -1