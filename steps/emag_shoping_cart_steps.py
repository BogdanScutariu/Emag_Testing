from behave import *


@given('Navigate to items page')
def step_impl(context):
    try:
        context.items_page.navigate_to_item()
    except Exception as e:
        print(f"Error navigating to items page: {e}")
        assert False, f"Error navigating to items page: {e}"

@when('We add one product in our cart')
def step_impl(context):
    try:
        context.items_page.add_one_item()
    except Exception as e:
        print(f"Error adding one product to cart: {e}")
        assert False, f"Error adding one product to cart: {e}"

@then('Count if the product from cart is one')
def step_impl(context):
    try:
        context.items_page.check_one_item_in_cart()
        context.emag_shopping_cart.navigate_to_shopping_cart()
        context.emag_shopping_cart.clear_all_items()
    except Exception as e:
        print(f"Error counting products in cart or clearing cart: {e}")
        assert False, f"Error counting products in cart or clearing cart: {e}"

@when('We add more products in cart')
def step_impl(context):
    try:
        context.items_page.add_more_items()
    except Exception as e:
        print(f"Error adding more products to cart: {e}")
        assert False, f"Error adding more products to cart: {e}"

@then('We have more products in our cart')
def step_impl(context):
    try:
        context.items_page.check_more_item_in_cart()
        context.emag_shopping_cart.navigate_to_shopping_cart()
        context.emag_shopping_cart.clear_all_items()
    except Exception as e:
        print(f"Error checking products in cart or clearing cart: {e}")
        assert False, f"Error checking products in cart or clearing cart: {e}"

@when('We look at more products and insert more items in shopping cart')
def step_impl(context):
    try:
        context.items_page.add_new_item()
    except Exception as e:
        print(f"Error adding new item to cart: {e}")
        assert False, f"Error adding new item to cart: {e}"

@then('We remove one product from our shopping cart')
def step_impl(context):
    try:
        context.items_page.check_more_item_in_cart()
        context.emag_shopping_cart.navigate_to_shopping_cart()
        context.emag_shopping_cart.clear_one_item()
    except Exception as e:
        print(f"Error removing one product from cart: {e}")
        assert False, f"Error removing one product from cart: {e}"
