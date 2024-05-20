from abc import ABC, abstractmethod

class AbstractBudget(ABC):

    @abstractmethod
    def __init__(self, name: str, balance: float, category: str) -> None:
        pass

    @abstractmethod
    def delete_budget(self):
        pass

    @abstractmethod
    def add_categories(self):
        pass

    @abstractmethod
    def add_start_date(self):
        pass

    @abstractmethod
    def add_start_time(self):
        pass

    @abstractmethod
    def carry_over_balance(self):
        pass

    @abstractmethod
    def carry_over_negative_balance(self):
        pass

    @abstractmethod
    def include_pending_transactions(self):
        pass

    @abstractmethod
    def add_tags(self):
        pass

    @abstractmethod
    def remove_tags(self):
        pass

    