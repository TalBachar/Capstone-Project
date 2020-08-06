import requests

class Query:
    #   This part is to get a token from the API, using our API key and Secret
    #   And then from the json we get back, "isolate" the token and save it
    #   as a variable. then use the token in the headers: we need to use the token
    #   every time we make a request
    def req_token():
        data = {
        'grant_type': 'client_credentials',
        'client_id': 'T6zwFVoQKCTvBaHMMnAo5X7g6mcfiRsuUXnKGG7slbIE2SeV4E',
        'client_secret': 'IiCMulXrvKGg24Du97cojCBdJ6oWIBJRYtTe53I4'
        }

        response = requests.post('https://api.petfinder.com/v2/oauth2/token', data=data)
        response = response.json()
        #print("Response is: ", response)
        token = response["access_token"]
        return token


    #   Query the database using specific args
    def query(pet_type, pet_age, pet_breed):
        token = Query.req_token()
        headers = { 'Authorization': 'Bearer {0}'.format(token), }
        param = {
            "type": pet_type,
            "age": pet_age,
            "breed": pet_breed,
            "location" : "New York City, NY",
            "distance" : 25,
        }  #close param
        
        response = requests.get('https://api.petfinder.com/v2/animals', headers=headers, params=param)
        response = response.json()
        return response

    # def get_query_values(pet_type, pet_age, pet_breed):
    #     response = query(pet_type, pet_age, pet_breed)

    
    def get_total_results(pet_type, pet_age, pet_breed):
        response = Query.query(pet_type, pet_age, pet_breed)
        total_count = response["pagination"]["total_count"]
        print("Args are: ", pet_type, pet_age, pet_breed)
        print("and the total count is ", total_count)
        return total_count

    
    #   query the database's organizations
    def org_query(token, org_code):
        headers = { 'Authorization': 'Bearer {0}'.format(token), }
        org_response = requests.get('https://api.petfinder.com/v2/organizations/{0}'.format(org_code), headers=headers)
        org_response = org_response.json()
        return org_response

"""
def print_results():
    print("There are", total_count, "results!\n\n")
    if total_count > 0:
        for i in range(int(limit)): #loop through results
            if response["animals"][i]["organization_id"][0:2] == 'NY':  #make sure shelter code begins with NY (exclude other results)
                print(response["animals"][i]["name"], "is a", response["animals"][i]["colors"]["primary"],
                    response["animals"][i]["breeds"]["primary"], "." )
                org_code = response["animals"][i]["organization_id"]
                org_response = org_query(token, org_code)

                #pprint(org_response["organization"]["name"])
                print("To adopt please call", org_response["organization"]["name"], "at", org_response["organization"]["phone"],
                "location: ", org_response["organization"]["address"]["city"],",", org_response["organization"]["address"]["state"] ,"\n")
    else:
        print("Nothing to show, sorry!")
"""

# print(Query.get_total_results("Dog", "Baby", "Hound"))