import absclasses as abscls
from enum import Enum


class FinancialType(Enum):
    ASSET = "asset"
    LIABILITY = "liability"


class AccountType(Enum):
    CHECKING = 1
    SAVINGS = 2


class UpdateMethod(Enum):
    CREDIT = "credit"
    DEBIT = "debit"


class ItemId(aa.ItemId):

    def __init__(self):
        super().__init__()
        self._id_num = 0

    def get_id(self):
        self._id_num += 1
        return f"{self._id_num:02d}"


class Account(aa.AbstractAccount):

    def __init__(self, account_id, balance=0, is_active=True):
        super().__init__(account_id, balance, is_active)
        self.account_id = account_id
        self.balance = balance
        self.is_active = is_active
        self.creation_date = None
        self.financial_type = None
        self.account_typeccount_type = None
        self.name = None

    def get_id(self) -> str:
        return self.account_id

    def get_balance(self) -> float:
       return self.balance

    def is_active(self) -> bool:
        return self.is_active

    def __str__(self) -> str:
        return f"Account-{self.account_id} has a balance of {self.balance}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.account_id}, balance={self.balance}, is_active={self.is_active})"


class AssetAccount(Account):
    pass


class AccountManager(aa.AccountManager):
    pass
    # id_creator = ItemId()
    # accounts = []
