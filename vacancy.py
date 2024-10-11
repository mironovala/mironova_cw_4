class Vacancy:
    def __init__(self, name: str, url: str, salary: int | None, description: str | None):
        self.name: str = name
        self.url: str = url
        self.salary: int = self.validate(salary)
        self.description: str | None = description

    @staticmethod
    def _validate(salary: int | None) -> int:
        return salary or 0

    def __lt__(self, other):
        pass

    def __repr__(self):
        pass
