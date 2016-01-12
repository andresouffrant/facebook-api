import facebook
import facepy
 
application_id = #application id
application_secret_key = # secret key
user_id = # id of user or page to look for. not sure how this is initialized

def get_access_token(app_id, key):
    return facepy.utils.get_application_access_token(app_id, key)

def access_graph(token):
    return facebook.GraphAPI(access_token=token)

if __name__ == "__main__":
    # this token won't be correct, i don't understand the token system well enough
    token = get_access_token(application_id, application_secret_key)
    graph = access_graph(token)
    me = graph.get_object("me")
    print(me["birthday"])
