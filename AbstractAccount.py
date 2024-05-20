from abc import ABC, abstractmethod
from typing import Type

class AbstractAccount(ABC):
    
    @abstractmethod
    def __init__(self, account_id: str, param2: float, param3: bool):
        pass

    @abstractmethod
    def get_id(self) -> str:
        pass

    @abstractmethod
    def get_balance(self) -> float:
        pass

    @abstractmethod
    def is_active(self) -> bool:
        pass


class FinancialType(ABC):

    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def get_financial_type(self):
        pass


class BalanceUpdate(ABC):

    @abstractmethod
    def debit_account(self):
        pass 

    @abstractmethod
    def credit_account(self):
        pass


class ItemId(ABC):
    
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_id(self):
        pass


class ItemAge(ABC):

    @abstractmethod
    def has_creation_date(self):
        pass

    @abstractmethod
    def has_creation_time(self):
        pass

    @abstractmethod
    def get_creation_date(self):
        pass

    @abstractmethod
    def get_creation_time(self):
        pass
    
    @abstractmethod
    def calculate_age(self):
        pass


class ItemName(ABC):

    @abstractmethod
    def name_item(self):
        pass

    @abstractmethod
    def has_name(self):
        pass
    
    @abstractmethod
    def get_name(self):
        pass


class AccountManager(ABC):

    @abstractmethod
    def __init__(self) -> None: 
        super().__init__()

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def remove_account(self):
        pass

