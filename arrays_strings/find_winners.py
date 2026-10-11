def findWinners(matches: list[list[int]]) -> list[list[int]]:
        from collections import defaultdict, Counter
        
        counts = defaultdict(list)
        
        # matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
        
        for winner, loser in matches:
            counts[winner].append(0)
            counts[loser].append(1)
            
        ans = [[],[]]
        
        # print("counts: ", counts)
            
        for player, played in counts.items():
            played_counts = Counter(played)
            if played_counts.get(1, 0) == 0:
                ans[0].append(player)
            if played_counts.get(1, 0) == 1:
                ans[1].append(player)
            
           
        return [sorted(player) for player in ans]


if __name__ == "__main__":
     matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]

     print(findWinners(matches=matches))
     