from threading import Thread, Lock

class BankAccount:

    def __init__(self):
        self.balance = 1000

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount



def deposit_task(account, amount):
    for _ in range(5):
        with lock:
            account.deposit(amount)
        print(f'Deposited {amount}, new balance is {account.balance}')


def withdraw_task(account, amount):
    for _ in range(5):
        with lock:
            account.withdraw(amount)
        print(f'Withdrew {amount}, new balance is {account.balance}')


account = BankAccount()
lock = Lock()
deposit_thread = Thread(target=deposit_task, args=(account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()

