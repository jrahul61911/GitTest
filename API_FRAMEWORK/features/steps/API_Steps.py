import requests
from behave import *

from utilities.configurations import *
from Payload import *


@given('the Book details which needs to be added to the Library')
def step_impl(context):
    context.url_post = getConfig()['API']['endpoint'] + APIResources.addmaps
    context.headers = {"Content-Type": "application/json"}


@when('we execute the AddBook Post API method')
def step_impl(context):
    context.add_APIresponse = requests.post(context.url_post, json=addPlacePayload(),
                                            headers=context.headers)


@then('book is successfully added')
def step_impl(context):
    print(context.add_APIresponse.json())
