from island import Island
from data_structures.heap import MaxHeap


class Mode2Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, n_pirates: int) -> None:
        """
        The solution creates a list for islands and stores n_pirates in self.
        The complexity of this approach is 1 because you create an empty list
        The best case and worst case for the problem is O(1)
        """
        self.n_pirates = n_pirates
        self.islands = []

    def add_islands(self, islands: list[Island]):
        """
        The solution is just appending all islands into the current list
        The best case and worst case for the problem is O(I)
        Here I is the length of islands
        """
        for island in islands:
            self.islands.append(island)
        # self.islands = MaxHeap(len(islands))
        # for island in islands:
        #     self.islands.add(island)
            

    def simulate_day(self, crew: int) -> list[tuple[Island|None, int]]:
        """
        The solution uses BST's in order iteration to iterate from most possible money made to least.
        This method also has an if else function for if crew is larger or smaller than marines which sets the crew if smaller to 0.
        then it appends the current island plus the crew sent into the list.
        The complexity of this approach is N+ C*log(n) as N is for the loop making all the island.crews based on crew number as well as
        heapify which is O(n)
        The C*log(n) part is the for loop that runs C times with it having a log(n) funciton inside being add
        Here N is the size of the input list.  
        Here C is the number of captains participating.
        The best case and worst case for the problem is O(C*log(n))
        """
        for island in self.islands:
            island.crew = crew
        sorted_islands = MaxHeap.heapify(self.islands)

        # for island in self.islands:
        #     print (sorted_islands.get_max())
        # for island in self.islands:
        #     island.crew = crew
        # sorted_islands = MaxHeap.heapify(self.islands)
        captain_choices = []
        for _ in range(self.n_pirates):
            current_crew = crew
            current_money = 0
            max_island = sorted_islands.get_max()
            if current_crew >= max_island.marines:
                current_crew -= max_island.marines
                captain_choices.append((max_island,max_island.marines))
                max_island.marines = 0
                current_money += max_island.money
                max_island.money = 0
                
            else:
                stolen_money = (current_crew * max_island.money)/max_island.marines
                max_island.money -= stolen_money
                captain_choices.append((max_island,current_crew))
                max_island.marines -= current_crew
                current_crew = 0
            sorted_islands.add(max_island)
        return captain_choices
                
            

