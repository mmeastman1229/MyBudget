from abc import ABC, abstractmethod

class AbsTransaction(ABC):

    @abstractmethod
    def create_transaction(self):
        pass

    @abstractmethod
    def delete_transaction(self):
        pass

    @abstractmethod
    def set_amount(self):
        pass
    
    @abstractmethod
    def set_type(self):
        pass

    @abstractmethod
    def add_category(self):
        pass

    @abstractmethod
    def add_description(self):
        pass

    @abstractmethod
    def add_payee(self):
        pass

    @abstractmethod
    def add_tag(self):
        pass

    @abstractmethod
    def add_date(self):
        pass

    @abstractmethod
    def add_time(self):
        pass

    @abstractmethod
    def is_cleared(self):
        pass

    @abstractmethod
    def has_category(self):
        pass

    @abstractmethod
    def has_description(self):
        pass

    @abstractmethod
    def has_payee(self):
        pass

    @abstractmethod
    def has_tag(self):
        pass