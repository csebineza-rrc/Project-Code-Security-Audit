"""This module defines the BankAccount class."""

__author__ = "Cedrick Sebineza"
__version__ = "1.1.2025"

from abc import ABC, abstractmethod
from datetime import date

class BankAccount(ABC):
    """Represents the bank account of a client."""

    def __init__(self, account_number: int, client_number: int, 
                date_created: date, balance: float):
        """Initializes a new instance of the BankAccount class.

        Args:
          account_number(int): An integer value representing the bank
                account number.
          client_number(int): An integer value representing the client
                number of the account holder.
          balance(float): A float value representing the current balance
                of the bank account.
          date_created(date): Represents the current date of the day.

        Raises:
          ValueError: Raised when account_number and client_number is 
              not of an integer type.
        """

        # Constants
        self.BASE_SERVICE_CHARGE: float = 0.50

        # Validation
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
       
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        
        # Date validation
        if isinstance(date_created, date):
          self._date_created = date_created
        else:
          self._date_created = date.today()
        
        self.__account_number = account_number
        self.__client_number = client_number
        self.__balance = balance
       
    @property
    def account_number(self) -> int:
        """Gets the account number of the bank account.

        Returns:
            int: The account number associated with the bank account.
        """

        return self.__account_number
    
    @property
    def client_number(self) -> int:
         """Gets the client number of the account holder.

         Returns:
            int: The client number of the account holder.
         """

         return self.__client_number
    
    @property
    def balance(self) -> float:
        """Gets the current balance of the bank account.

        Returns:
          float: The current balance of the bank account.
        """

        return self.__balance
    
    def update_balance(self, amount: float):
        """Validates the amount.

        Args:
          amount(float): Represents the deposit amount added to the 
              account balance.
        """ 

        # Check if the amount is negative or positive
        # Update the balance
        if amount < 0:
          self.__balance -= -amount
        else:
          self.__balance += amount

        return self.__balance
        
    def deposit(self, amount: float):
        """ Validates the deposit amount.

        Args:
          amount(float): A float value representing the amount.

        Raises:
          ValueError: Raised when the amount is negative.
        """

        # Validation
        try:
          amount = float(amount)
        except ValueError:
          raise ValueError(f"Deposit amount: {amount:,.2f} must be numeric.")
        if amount <= 0:
          raise ValueError(f"Deposit amount: {amount:,.2f} must be positive.")
        
        # Updating balance
        self.__balance += amount

        return self.balance    

    def withdraw(self, amount: float):
        """Validates the withdrawn amount.

        Args:
          amount(float): A float value representing the amount withdrawn.

        Raises:
          ValueError: Raised when the amount is not numeric, or positive
            and when the amount to be withdrawn exceeds the current
            balance.
        """

        # Validation
        try:
          amount = float(amount)
        except ValueError:
          raise ValueError(
              f"Withdraw amount: {amount:,.2f} must be numeric."
              )

        if amount <= 0:
          raise ValueError(
            f"Withdrawal amount: {amount:,.2f} must be positive."
            )

        if amount > self.__balance:
           raise ValueError(
              f"\nWithdrawal amount: {amount:,.2f} must not exceed the"
              f" account balance: {self.__balance:,.2f}"
            )

        # If amount is valid, update the balance
        self.update_balance(amount)
        return self.__balance
        
    def __str__(self) -> str:
        """Returns a formatted string of the account number and balance.

        Returns:
            str: A string representation of the bank account.
        """
        
        return (
            f"Account Number: {self.__account_number} "
            f"Balance: {self.__balance:,.2f}"
        )    

    @abstractmethod
    def get_service_charges(self) -> float:
       """Gets the calculated service charge that a BankAccount will incur.

      Returns: 
        float: The total calculated service charge on an account.
       """

       return self.BASE_SERVICE_CHARGE     
