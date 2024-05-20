from abc import ABC, abstractmethod
from typing import Type

class AbsItemId(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_id(self):
        pass

class AbsPayee(ABC):
    @abstractmethod
    def __init__(self, name: str) -> None:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass


class AbsTag(ABC):
    @abstractmethod
    def __init__(self, name: str) -> None:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass        


class AbsAccount(ABC):
    @abstractmethod
    def __init__(self, acct_num: str, balance: float,
                 active_acct: bool) -> None:
        pass

    @abstractmethod
    def get_acct_num(self) -> str:
        pass

    @abstractmethod
    def get_balance(self) -> float:
        pass

    @abstractmethod
    def is_active_accnt(self) -> bool:
        pass


class AbsBudget(ABC):
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


class AbsTransaction(ABC):
    @abstractmethod
    def __init__(self, amount: float, affected_acct: AbsAccount, 
                 category: str, description: str, payee: str,
                 tag: str, date: str, cleared_status: bool) -> None:
        pass

    @abstractmethod
    def get_amount(self) -> float:
        pass

    @abstractmethod
    def get_affected_acct(self) -> AbsAccount:
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
