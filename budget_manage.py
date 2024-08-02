class BudgetCategory:
    def __init__(self, name, budget):
        self.__name = name
        self.__budget = budget

    def add_category(food_category, budget_list):
        cat_name = food_category.get_category()
        if cat_name not in budget_list:
            budget_list[cat_name] = food_category
            print(f"{cat_name} category added to Budget")

    def set_category(self, new_name):
        self.__name = new_name
    
    def get_category(self):
        return self.__name
    
    def set_budget(self, new_budget):
        self.__budget = new_budget
    
    def get_budget(self):
        return self.__budget
    
    def add_expense(self, amount):
        category = input("What's the category?: ")
        if category in budget_list:
            new_budget = budget_list[category].get_budget() + amount
            budget_list[category].set_budget(new_budget)
            print(f"{amount} added to {category} budget")
        
    def display_category_summary(self):
        for category in budget_list:
            print(f"{category}: {budget_list[category].get_budget()}")
    
budget_list = {}

food_category = BudgetCategory("Food", 500)
BudgetCategory.add_category(food_category, budget_list)
food_category.add_expense(100)
food_category.display_category_summary()

