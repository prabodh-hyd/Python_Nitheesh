"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    new_cart = current_cart.copy()
    for item in items_to_add:
        new_cart[item] = new_cart.get(item, 0) + 1
    return new_cart
pass


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    cart = {}
    for item in notes:
        cart[item] = 1
    return cart
pass


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    new_ideas = ideas.copy()
    for recipe_name, ingredients in recipe_updates:
        new_ideas[recipe_name] = ingredients
    return new_ideas
pass


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return dict(sorted(cart.items()))

pass


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment_cart = {}
    for item, quantity in sorted(cart.items(), reverse=True):
        aisle, refrigerated = aisle_mapping[item]
        fulfillment_cart[item] = [quantity, aisle, refrigerated]
    return fulfillment_cart
pass


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    new_inventory = store_inventory.copy()
    for item, [quantity, aisle, refrigerated] in fulfillment_cart.items():
        current_quantity = new_inventory[item][0]
        if isinstance(current_quantity, int):
            new_quantity = current_quantity - quantity
            new_inventory[item] = ['Out of Stock' if new_quantity <= 0 else new_quantity, aisle, refrigerated]
    return new_inventory
pass
