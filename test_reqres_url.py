#import part
import pprint
from get_users_list import *

# variables part
base_url="https://reqres.in"
sub_url="/api/users?page=2"
url=base_url+sub_url

# testing
def test_get_users_list():
    excepted_status_code=200
    print("\nThe test_get_users_list start")
    print("\nThe url request is " + url)
    response=get_users_list(url)
    print("\nThe response have been return")
    json_text=json.loads(response.text)
    print("\nThe response have been converted to json text")
    pprint.pprint(json_text)
    print("\nThe expected status code is "+str(excepted_status_code))
    print("\nThe real status code is " + str(response.status_code))
    assert response.status_code==200
    print("\nThe test_get_users_list over")
