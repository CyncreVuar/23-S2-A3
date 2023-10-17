from island import Island

class Mode2Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, n_pirates: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.n_pirates = n_pirates
        self.islands = []

    def add_islands(self, islands: list[Island]):
        """
        Student-TODO: Best/Worst Case
        """
        for island in islands:
            self.islands.append(island)

    def simulate_day(self, crew: int) -> list[tuple[Island|None, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        raise NotImplementedError()
