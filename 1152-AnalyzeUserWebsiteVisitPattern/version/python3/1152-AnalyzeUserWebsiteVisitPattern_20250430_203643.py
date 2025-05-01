# Last updated: 30/04/2025, 20:36:43
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        users=defaultdict(list)
        for user,timestamp,website in sorted(zip(username,timestamp,website), key=lambda x: [x[0],x[1]]):
            users[user].append(website)
        pattern=Counter()
        for user,sites in users.items():
            pattern.update(Counter(set(combinations(sites,3))))

        return max(sorted(pattern),key=pattern.get)
