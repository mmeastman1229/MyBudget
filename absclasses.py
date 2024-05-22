from abc import ABC, abstractmethod
from typing import Type
import uuid

class ItemId():
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_id(self):
        pass

class Payee(ABC):
    @abstractmethod
    def __init__(self, name: str) -> None:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass


class Tag(ABC):
    @abstractmethod
    def __init__(self, name: str) -> None:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass        


class Account(ABC):
    @abstractmethod
    def __init__(self, account_id: str, balance: float, owner: str, 
        account_status: bool) -> None:
        pass

    @abstractmethod
    def get_account_id(self) -> str:
        pass

    @abstractmethod
    def get_balance(self) -> float:
        pass

    @abstractmethod
    def is_active(self) -> bool:
        pass


class Budget(ABC):
    @abstractmethod
    def __init__(self, name: str, balance: float, category: str) -> None:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_balance(self) -> float:
        pass

    @abstractmethod
    def get_category(self) -> str:
        pass


class Transaction(ABC):
    @abstractmethod
    def __init__(self, amount: float, affected_account: AbsAccount, 
                 category: str, description: str, payee: str,
                 tag: str, date: str, cleared_status: bool) -> None:
        pass

    @abstractmethod
    def get_amount(self) -> float:
        pass

    @abstractmethod
    def get_affected_account(self) -> AbsAccount:
        pass

    @abstractmethod
    def get_category(self) -> str:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_payee(self) -> str:
        pass
 
    @abstractmethod
    def get_date(self) -> str:
        pass

    @abstractmethod
    def get_cleared_status(self) -> bool:
        pass
