class BudgetCategory:
    def __init__(self, name, budget):
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
    
    def add_category(food_category, budget_list):
        cat_name = food_category.get_category()
        if cat_name not in budget_list:
            budget_list[cat_name] = food_category
            print(budget_list)
    
    def add_expense(self, amount):
        category = input("What's the category?: ")
        if category in budget_list:
            new_budget = category.getbudget() + amount
            print(new_budget)
            return new_budget
        
    def display_category_summary(self):
        print(budget_list)
    
budget_list = {}

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()