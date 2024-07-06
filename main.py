import os

from dotenv import load_dotenv

import xendit
from xendit.apis import BalanceApi
from pprint import pprint

load_dotenv()
API_KEY = os.getenv('API_KEY')
xendit.set_api_key(API_KEY)

client = xendit.ApiClient()

try:
    response = BalanceApi(client).get_balance("CASH")
    pprint(response)
except xendit.XenditSdkException as e:
    print("Exception when calling BalanceApi->get_balance: %s\n" % e)
