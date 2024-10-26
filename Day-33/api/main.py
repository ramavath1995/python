import requests
# An application programming interface(API) is a set of commands, functions, protocols, and objects that programmers
# can use to create software or interact with external system
# api is barrier between your system and external system it makes a request to external system to pull live data


a = requests.get("http://api.open-notify.org/iss-now.json")
print(a.json())
