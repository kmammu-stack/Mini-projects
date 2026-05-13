import logging

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


# Base class
class Transaction:
    def __init__(self, amount, category, description=""):
        if amount < 0:
            raise ValueError("Amount cannot be negative!")
        if not category.strip():
            raise ValueError("Category cannot be empty!")
        self.amount = amount
        self.category = category
        self.description = description

    def display_info(self):
        try:
            info = f"Type: {self.__class__.__name__} | Amount: ${self.amount:.2f} | Category: {self.category} | Description: {self.description}"
            print(info)
            logger.info(info)
        except Exception as e:
            logger.error(f"Error displaying info: {e}")


# Income subclass
class Income(Transaction):
    def display_income(self):
        msg = f"[INCOME] Amount: ${self.amount:.2f} | Category: {self.category}"
        print(msg)
        logger.info(msg)


# Expense subclass
class Expense(Transaction):
    def display_expense(self):
        msg = f"[EXPENSE] Amount: ${self.amount:.2f} | Category: {self.category}"
        print(msg)
        logger.info(msg)


# Get input from user
def get_transaction():
    try:
        t_type = input("Enter type (income/expense): ").strip().lower()
        amount = float(input("Enter amount: "))
        category = input("Enter category: ").strip()
        description = input("Enter description: ").strip()

        if t_type == "income":
            t = Income(amount, category, description)
            t.display_income()
        elif t_type == "expense":
            t = Expense(amount, category, description)
            t.display_expense()
        else:
            print("Invalid type! Please enter income or expense.")

    except ValueError as e:
        print(f"Invalid input: {e}")


# Run
print("=== Transaction System ===\n")

inc = Income(3000, "Salary", "April salary")
inc.display_info()
inc.display_income()

exp = Expense(500, "Rent", "Monthly rent")
exp.display_info()
exp.display_expense()

print("\n--- Enter your own transaction ---")
get_transaction()