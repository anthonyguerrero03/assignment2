# sandwich_maker.py
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True
