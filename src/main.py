# -*- coding: utf-8 -*-

import os

from google.genai import Client

# NOTE: This is WRONG, but for demonstration purposes only.
# NOTE: You should never hardcode your API key in your code!

api_key = os.environ["GEMINI_API_KEY"]
client = Client(api_key = api_key)


print(client.models.generate_content.__doc__)

response = client.models.generate_content(
    model = "gemini-3.8-flash",
    contents = "Write a short story about a robot learning to love."
)

print(response.result)