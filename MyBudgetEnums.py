from enum import Enum

class FinancialType(Enum):
    ASSET = "asset"
    LIABILITY = "liability"

class UpdateType(Enum):
    CREDIT = "credit"
    DEBIT = "debit"

class AccountType(Enum):
    CHECKING = 1
    SAVINGS = 2
    BUDGET_ADJUSTMENT = 3
