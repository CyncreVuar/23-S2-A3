from island import Island
from data_structures.heap import MaxHeap

class Mode2Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, n_pirates: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.n_pirates = n_pirates

    def add_islands(self, islands: list[Island]):
        """
        Student-TODO: Best/Worst Case
        """
        self.islands = MaxHeap(len(islands))
        for island in islands:
            self.islands.add(island)
            

    def simulate_day(self, crew: int) -> list[tuple[Island|None, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        money_list = []
        current_crew = crew
        current_money = 0
        max_island = self.islands.get_max()
        if current_crew >= max_island.marines:
            current_crew -= max_island.marines
            max_island.marines = 0
            current_money += max_island.money
            max_island.money = 0
        else:
            stolen_money = (current_crew * max_island.money)/max_island.marines
            max_island.money -= stolen_money
            max_island.marines -= current_crew
            current_crew = 0
        self.islands.add(max_island)




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
    test = Mode2Navigator(5)
    test.add_islands(islands)