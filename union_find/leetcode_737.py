class Solution(object):
    def areSentencesSimilarTwo(self, sentence1, sentence2, similarPairs):
        n = len(sentence1)
        if n != len(sentence2):
            return False

        pair_map = {}
        for pair in similarPairs:
            first, second = pair
            if first not in pair_map:
                pair_map[first] = []
            pair_map[first].append(second)
            if second not in pair_map:
                pair_map[second] = []
            pair_map[second].append(first)

        for i in range(n):
            word1 = sentence1[i]
            word2 = sentence2[i]
            if word1 == word2:
                continue
            if word1 not in pair_map or word2 not in pair_map:
                return False
            if not self.find_target(pair_map, word1, word2, set()):
                return False

        return True

    def find_target(self, pair_map, word, target, visited):
        if word == target:
            return True
        if word not in pair_map:
            return False

        visited.add(word)

        for sim_word in pair_map[word]:
            if sim_word in visited:
                continue
            if self.find_target(pair_map, sim_word, target, visited):
                return True

        return False
