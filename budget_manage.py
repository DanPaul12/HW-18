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
    
    def get_budget(self):
        return self.__budget
    
    def add_expense(self, amount):
        category = input("What's the category?: ")
        if category == isinstance(BudgetCategory):
            new_budget = category.getbudget() + amount
            return new_budget
        
    def display_category_summary(self):
        for category in budget_list:
            print(category)

budget_list = {}
