from behave import *


@given('Navigate to items page')
def step_impl(context):
    context.items_page.navigate_to_item()


@when('We add one product in our cart')
def step_impl(context):
    context.items_page.add_one_item()


@then('Count if the product from cart is one')
def step_impl(context):
    context.items_page.check_one_item_in_cart()
    context.emag_shopping_cart.navigate_to_shopping_cart()
    context.emag_shopping_cart.clear_all_items()


@when('We add more products in cart')
def step_impl(context):
    context.items_page.add_more_items()


@then('We have more products in our cart')
def step_impl(context):
    context.items_page.check_more_item_in_cart()
    context.emag_shopping_cart.navigate_to_shopping_cart()
    context.emag_shopping_cart.clear_all_items()


@when('We look at more products and insert more items in shopping cart')
def step_impl(context):
    context.items_page.add_new_item()


@then('We remove one product from our shopping cart')
def step_impl(context):
    context.items_page.check_more_item_in_cart()
    context.emag_shopping_cart.navigate_to_shopping_cart()
    context.emag_shopping_cart.clear_one_item()
