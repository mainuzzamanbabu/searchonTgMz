from telethon import TelegramClient, events, sync
import asyncio
import re
import json
# Your API ID and Hash
api_id = ''
api_hash = ''

# The channel or group you want to search
channel_id = 
# channel_id = 
# The search query

def extract_data(text):
    data = {}

    # Renounced
    data["Renounced"] = bool(re.search(r"\*\*Renounced: ✅\*\*", text))

    # Burned
    # Burned
    burned_match = re.search(r"Burned:\s*([✅❌]+)", text)
    data["Burned"] = burned_match.group(1) == "✅" if burned_match else False

    # Creator
    # creator_match = re.search(r"\*\*Creator:\*\*`\s*([0-9.]+)%`", text)
    # data["Creator"] = float(creator_match.group(1)) if creator_match else 0.0
    creator_match = re.search(r"\*\*Creator:\*\*`\s*([0-9.]+)%`", text)
    data["Creator"] = float(creator_match.group(1)) if creator_match else 0.0
    # Top 5
    top_5_match = re.search(r"\*\*Top 5:\*\*`\s*(?:⚠️\s*)?([0-9.]+)%`", text)
    data["Top 5"] = float(top_5_match.group(1)) if top_5_match else 0.0

    # Tokens in LP
    tokens_in_lp_match = re.search(r"\*\*Tokens in LP:\*\*`\s*([0-9.]+)%`", text)
    data["Tokens in LP"] = float(tokens_in_lp_match.group(1)) if tokens_in_lp_match else 0.0

    return data


search_query = 'DhS4zHEPmqHjgJ1zJtdekDwbKUEJh9RTWDAR6d6y6fXk'

client = TelegramClient('session_name', api_id, api_hash)
client.start()
    
    # Searching for messages in the channel or group
messages = client.get_messages(channel_id, search=search_query)
    
    # Printing the messages that match the search query
for message in messages:
        print(message.id, message.text)
        data = extract_data(message.text)
        json_data = json.dumps(data, indent=4)
        print(json_data)
    

