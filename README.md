# polyrize-ex

start with 
`pip install -r requirements.txt`

### testing Magic List ex.:  
edit `main.py` with some test cases (basic ones are already there) and run `python main.py`  
OR  
` from magic_list import MagicList` & do whatever
***
### testing API ex.:  
- `python server.py`
- send a POST request to `0.0.0.0:8000/auth`, with `{username: <username>, password: <password>}` as body (will be checked against `users.csv` file)
- if auth was successful, you will get a JWT access token in the response
- send a POST request (with a valid Auth. header containing the token you got) to `0.0.0.0:8000/normalize` for testing the JSON normalization logic

the expected request body is: `{"data": [...your array of JSON objects...]}`, *for example:*
```json
{
    "data": [
        {
            "name": "device",
            "strVal": "iPhone",
            "metadata": "not interesting"
        },
        {
            "name": "isAuth",
            "strVal": "true",
            "lastSeen": "not interesting"
        }
        
    ]
}
```

***
### testing SERVERLESS ex.:  
send a POST request as above (no need for token) to the endpoint:  
`https://qomqbv7a79.execute-api.us-east-1.amazonaws.com/dev/normalize`  
(the handler function is in `polyrize_ex/handler.py`)
