
def hello_world():
  print("hello world")
  
# %%
import re

import pandas as pd
import requests

# %%
url = "https://huggingface.co/datasets/bigcode/ta-prompt/blob/main/TA_prompt_v1.txt"
# Make an HTTP request to the URL and get the response
response = requests.get(url, verify=True)

# %%
# The request was successful, so download the file
if response.status_code == 200:
    with open("myfile.txt", "wb") as f:
        f.write(response.content)
else:
    # The request was not successful, so raise a specific error with the status code
    raise Exception("Failed to download file. Status code: {}".format(response.status_code))




# %%
text = response.content
# %%
# https://pynative.com/python-regex-capturing-groups/
# bard agrees
#ptrn = rb"Human: (.*)Assistant"
ptrn = rb"Human:(.+?)Assistant"
matches = re.finditer(ptrn, text)

# %%
patterns = []
for match in matches:
  patterns.append(match.group())

# %%
cleaned = []
for p in patterns:
    p = p.replace(b'Human: ', b'')
    p = p.replace(b'Assistant', b'')
    p = p.replace(b'&quot', b'')
    p = p.replace(b';', b'')
    p = p.replace(b',', b'')
    cleaned.append(p)
# %%
# remove words from string
# %%
cleaned[:2]
# %%
with open('ta_prompt2.txt', "w") as f:
  for string in cleaned:
    f.write(str(string) + "\n")
# %%
