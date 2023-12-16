import requests    

api_endpoint = "https://api.openai.com/v1/completions"   
api_key = "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"



request_headers = {                                             # set HTTP headers                 
    'Content-Type': 'application/json',                         # set request type to JSON 
    'Authorization': 'Bearer ' + api_key,                       # set authorization to Bearer + API key
}


request_data = {                                               # set request data
    "model" : "gpt-3.5-turbo-instruct"                         # set model to instruct version of GPT-3 
    "prompt": "This is a test",                                # set prompt example
    "max_tokens": 500,                                         # set max tokens to 500 (default is 16)
    "temperature": 0.9,                                        # set temperature to 0.9 (default is 0.7)
}

requests.post(api_endpoint, headers= request_headers, json = {})               # make request to API endpoint with headers and data 


