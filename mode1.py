from island import Island
from data_structures.bst import BinarySearchTree

class Mode1Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        The solution uses BST as it has depth bound by log(n) based on assignment as well as easier iteration with in order.
        The order is reversed because when iterated i want to get the highest value first so i made the highest value on the left.
        The complexity of this approach is NlogN because evrytime you add an item the complexity is log(n) because the complexity is the depth which
        in this case is always log(n) because of the assignment. this adding is done n times because u add n items to the BST
        Here N is the size of the input list.   
        The best case and worst case for the problem is O(Nlog(N))
        """
        self.crew_numbers = crew
        self.islands = BinarySearchTree()
        for island in islands:
            self.islands.__setitem__((island.marines/island.money), island)

    def select_islands(self) -> list[tuple[Island, int]]:
        """
        The solution uses BST's in order iteration to iterate from most possible money made to least.
        This method also has an if else function for if crew is larger or smaller than marines which sets the crew if smaller to 0.
        then it appends the current island plus the crew sent into the list.
        The complexity of this approach is N because you iterate over every node
        Here N is the size of the input list.  
        The best case and worst case for the problem is O(N)
        """
        # def island_efficiency(sort_key: Island):
        #     return sort_key.money/sort_key.marines
        
        # sorted_islands_by_efficiency = mergesort(self.islands, key=island_efficiency)
        current_crew = self.crew_numbers
        # count = (len(sorted_islands_by_efficiency)-1)
        island_and_crew_list = []
        money = 0
        for island_node in self.islands:
            island = island_node.item
            if current_crew >= island.marines:
                current_crew -= island.marines
                island_and_crew_list.append((island,island.marines))
            else:
                island_and_crew_list.append((island,current_crew))
                money += (current_crew * island.money)/island.marines
                current_crew = 0

        # list version
        # money = 0
        # while current_crew > 0 and count >= 0:
        #     if current_crew >= sorted_islands_by_efficiency[count].marines:
        #         current_crew -= sorted_islands_by_efficiency[count].marines
        #         island_and_crew_list.append((sorted_islands_by_efficiency[count],sorted_islands_by_efficiency[count].marines))
        #         money += sorted_islands_by_efficiency[count].money
        #     else:
        #         island_and_crew_list.append((sorted_islands_by_efficiency[count],current_crew))
        #         money += (current_crew * sorted_islands_by_efficiency[count].money)/sorted_islands_by_efficiency[count].marines
        #         current_crew = 0

        #     count -= 1


        return(island_and_crew_list)



    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        The solution uses BST's in order iteration to iterate from most possible money made to least.
        This method also has an if else function for if crew is larger or smaller than marines which sets the crew if smaller to 0.
        This time, it repeats multiple times for different amounts of crew.
        then it appends the current island plus the crew sent into the list.
        The complexity of this approach is N*C because you iterate over every node for every crew amount
        Here N is the size of the input list.  
        Here C is the length of crew_members
        The best case and worst case for the problem is O(N*C)
        """
        
        money_list = []
        for current_crew in crew_numbers:
            money = 0
            for island_node in self.islands:
                island = island_node.item
                if current_crew >= island.marines:
                    current_crew -= island.marines
                    money += island.money
                else:
                    money += (current_crew * island.money)/island.marines
                    current_crew = 0
            money_list.append(money)
        return money_list

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        The solution is simply deleting the island from the BST from the input, updating the values, then readding it into the correct position.
        The complexity of this approach is log(n) because you have to del and add which is 2log(n)
        Here N is the size of the input list.  
        The best case and worst case for the problem is O(log(n))
        """
        self.islands.__delitem__(island.marines/island.money)
        island.money = new_money
        island.marines = new_marines
        self.islands.__setitem__((island.marines/island.money), island)

