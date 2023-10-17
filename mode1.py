from island import Island
from algorithms.mergesort import mergesort

class Mode1Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.crew_numbers = crew
        self.islands = islands

    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        def island_efficiency(sort_key: Island):
            return sort_key.money/sort_key.marines
        
        sorted_islands_by_efficiency = mergesort(self.islands, key=island_efficiency)
        current_crew = self.crew_numbers
        count = (len(sorted_islands_by_efficiency)-1)
        island_and_crew_list = []
        #test
        money = 0
        while current_crew > 0 and count >= 0:
            if current_crew >= sorted_islands_by_efficiency[count].marines:
                current_crew -= sorted_islands_by_efficiency[count].marines
                island_and_crew_list.append((sorted_islands_by_efficiency[count],sorted_islands_by_efficiency[count].marines))
                money += sorted_islands_by_efficiency[count].money
            else:
                island_and_crew_list.append((sorted_islands_by_efficiency[count],current_crew))
                money += (current_crew * sorted_islands_by_efficiency[count].money)/sorted_islands_by_efficiency[count].marines
                current_crew = 0

            count -= 1


        return(island_and_crew_list)



    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        """
        def island_efficiency(sort_key: Island):
            return sort_key.money/sort_key.marines
        
        sorted_islands_by_efficiency = mergesort(self.islands, key=island_efficiency)
        money_list = []
        for crew_number in crew_numbers:
            current_crew = crew_number
            count = (len(sorted_islands_by_efficiency)-1)
            money = 0
            while current_crew > 0 and count >= 0:
                if current_crew >= sorted_islands_by_efficiency[count].marines:
                    current_crew -= sorted_islands_by_efficiency[count].marines
                    money += sorted_islands_by_efficiency[count].money
                else:
                    money += (current_crew * sorted_islands_by_efficiency[count].money)/sorted_islands_by_efficiency[count].marines
                    current_crew = 0

                count -= 1
            money_list.append(money)
        return money_list

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        island.money = new_money
        island.marines = new_marines

if __name__ == '__main__':
    a = Island("A", 400, 100)
    b = Island("B", 300, 150)
    c = Island("C", 100, 5)
    d = Island("D", 350, 90)
    e = Island("E", 300, 100)
    # Create deepcopies of the islands
    islands = [
        Island(a.name, a.money, a.marines),
        Island(b.name, b.money, b.marines),
        Island(c.name, c.money, c.marines),
        Island(d.name, d.money, d.marines),
        Island(e.name, e.money, e.marines),
    ]
    test = Mode1Navigator(islands, 50)
    test.select_islands()