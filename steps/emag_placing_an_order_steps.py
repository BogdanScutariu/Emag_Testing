from behave import *

@given('The user navigates to the main page')
def step_impl(context):
    try:
        context.items_page.navigate_to_item()
    except Exception as e:
        print(f"Error navigating to the main page: {e}")

@when('We login with credentials')
def step_impl(context):
    try:
        context.items_page.login_into_account()
    except Exception as e:
        print(f"Error logging in with credentials: {e}")

@when('We search for iPhone 15')
def step_impl(context):
    try:
        context.items_page.search_items()
    except Exception as e:
        print(f"Error searching for iPhone 15: {e}")

@when('We add a product to the shopping cart')
def step_impl(context):
    try:
        context.items_page.add_item()
    except Exception as e:
        print(f"Error adding a product to the shopping cart: {e}")

@when('We proceed to checkout')
def step_impl(context):
    try:
        context.items_page.checkout()
    except Exception as e:
        print(f"Error proceeding to checkout: {e}")

@when('We place the order')
def step_impl(context):
    try:
        context.items_page.order_place_with_success()
    except Exception as e:
        print(f"Error placing the order: {e}")
