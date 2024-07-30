class BudgetCategory():
    def init(self, name, budget):
        self.__name = name
        self.__budget = budget

    def set_category(self, new_name):
        self.__name = new_name
    
    def get_category(self):
        return self.__name
    
    def set_category(self, new_budget):
        self.__budget = new_budget
    
    def get_category(self):
        return self.__budget

budgetlist = {}

def new_category(budget_list):
    category = input("What is your category?: ")
    budget = input("What is your budget?: ")
    budget_list[category] = BudgetCategory(category, budget)
    