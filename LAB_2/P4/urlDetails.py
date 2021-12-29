import requests  # requests Library

url = input("Enter the URL : ")
req = requests.get(url)   # Simple GET Request , It returns Response Object.


print(f"Status Code : {req.status_code} \n")   # HTTP 200 -  success status
print(f"Headers : {req.headers} \n")           # returns a case-insensitive dictionary of the response headers.
print(f"History : {req.history} \n")           # to track redirection. Gives a list which contains the Response objects
                                               # that were created in order to complete the request.
print(f"Encoding : {req.encoding}\n")          # Encoding of the Webpage you have requested for, utf - 8
print(f"Reason : {req.reason}\n")              # A short textual description of the Status-Code
print(f"Cookies : {req.cookies}\n")            # accessing the cookies that the server sent back.
print(f"Elapsed : {req.elapsed}\n")            # time elapsed between sending the request and getting back a response.
print(f"URL : {req.url}\n")                    # Requested URL
print(f"{req}\n")                              # Response object sent from the server.