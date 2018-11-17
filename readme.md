## What is this?


Apility.io is the API module. Now it only hosts Email and Domain Endpoints. Maybe I can development for all endpoints in the future.

## Usage

```
pip install -r requirements.txt
```

Example:

```
import apility

apireq = apility.apility(api_key=**)

dom = apireq.DomainWhois('domain').json
print(jom)
```