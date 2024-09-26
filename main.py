# main.py
import data
from sandwhich_maker import SandwichMaker
from cashier import Cashier

resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    while True:
        sandwich_size = input("What size sandwich would you like? (small/medium/large): ").lower()
        if sandwich_size in recipes:
            order_ingredients = recipes[sandwich_size]["ingredients"]
            cost = recipes[sandwich_size]["cost"]

            # Check resources
            if sandwich_maker_instance.check_resources(order_ingredients):
                # Process payment
                total_coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(total_coins, cost):
                    sandwich_maker_instance.make_sandwich(sandwich_size, order_ingredients)
            else:
                print("Unable to make sandwich due to insufficient resources.")
        else:
            print("Invalid size. Please choose from small, medium, or large.")
