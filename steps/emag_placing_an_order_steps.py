from behave import *

@given('The user navigates to the main page')
def step_impl(context):
     context.items_page.navigate_to_item()

@when('We login with credentials')
def step_impl(context):
        context.items_page.login_into_account()


@when('We search for iPhone 15')
def step_impl(context):
        context.items_page.search_items()


@when('We add a product to the shopping cart')
def step_impl(context):
        context.items_page.add_item()

@when('We proceed to checkout')
def step_impl(context):
        context.items_page.checkout()


@when('We place the order')
def step_impl(context):
        context.items_page.order_place_with_success()
