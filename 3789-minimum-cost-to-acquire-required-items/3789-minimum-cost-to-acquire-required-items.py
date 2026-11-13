class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Step 1: Use Type 3 items for the overlapping requirement min(need1, need2)
        common_need = min(need1, need2)
        total_cost = common_need * min(costBoth, cost1 + cost2)
        
        # Remaining requirements after fulfilling the common part
        rem1 = need1 - common_need
        rem2 = need2 - common_need
        
        # Step 2: Fulfill remaining type 1 requirement using the cheaper option between cost1 and costBoth
        total_cost += rem1 * min(costBoth, cost1)
        
        # Step 3: Fulfill remaining type 2 requirement using the cheaper option between cost2 and costBoth
        total_cost += rem2 * min(costBoth, cost2)
        
        return total_cost