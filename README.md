# ProfanityApi Documentation

## Overview
`ProfanityApi` is a Python class that interfaces with the ProfanityApi service to detect and filter profanity in user-generated content.

## Initialization
- `ProfanityApi(extra_headers={})`: Initializes the API object. Optional `extra_headers` can be passed as a dictionary to include additional headers in the requests.

## Methods
- `check_profanity(message)`: Sets the message to be checked and perform the profanity check. Returns the API object itself.

## Properties
- `score`: Returns the profanity score from the API response.
- `profanity`: Returns a boolean indicating whether the message contains profanity.

## Usage Example
```python
api = ProfanityApi()
result = api.check_profanity("Your message here")
print(f"Profanity Score: {result.score}")
print(f"Contains Profanity: {result.profanity}")
