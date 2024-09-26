import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Initialize instances of the classes
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    print("Welcome to the Sandwich Maker!")

    while True:
        # Prompt user for sandwich size
        sandwich_size = input(
            "What size sandwich would you like? (small/medium/large, or type 'exit' to quit): ").lower()

        if sandwich_size == 'exit':
            print("Thank you for using the Sandwich Maker. Goodbye!")
            break

        if sandwich_size in recipes:
            order_ingredients = recipes[sandwich_size]["ingredients"]
            cost = recipes[sandwich_size]["cost"]

            # Check if there are enough resources
            if sandwich_maker_instance.check_resources(order_ingredients):

                # Process payment
                total_coins = cashier_instance.process_coins()

                if cashier_instance.transaction_result(total_coins, cost):
                    # Make the sandwich if payment is successful
                    sandwich_maker_instance.make_sandwich(sandwich_size, order_ingredients)
            else:
                print("Unable to make sandwich due to insufficient resources.")
        else:
            print("Invalid size. Please choose from small, medium, or large.")


if __name__ == "__main__":
    main()
