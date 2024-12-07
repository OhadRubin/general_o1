import json

# Path to the JSON file uploaded by the user
# input_file_path = '/mnt/data/ORPG - Sat Dec 07 2024.json'
# output_file_path = '/mnt/data/pretty_printed_messages.txt'

# Read and parse the JSON file
with open("/Users/ohadr/Downloads/ORPG - Sat Dec 07 2024.json", "r") as file:
    data = json.load(file)

# Extract and format messages
messages = data.get("messages", {})
formatted_messages = []
import datetime


# 2024-12-07T15:40:15.735Z
messages = sorted(messages.items(), key=lambda x: datetime.datetime.fromisoformat(x[1]["updatedAt"].replace('Z', '+00:00')), reverse=False)
for msg_id, msg_details in messages:
    character_id = msg_details.get("characterId", "Unknown Character")
    character_id = "User" if character_id == "USER" else "Assistant"
    content = msg_details.get("content", "No Content")
    updated_at = msg_details.get("updatedAt", "No Update Timestamp")
    formatted_message = (
        f"{character_id}:\n"
        # f"Updated At: {updated_at}\n"
        f"{content}\n{'-' * 80}\n"
    )
    # formatted_messages.append(formatted_message)
    print(formatted_message)

# Write the pretty-printed messages to the output file
# with open("/Users/ohadr/Downloads/ORPG - Sat Dec 07 2024.json", "w") as output_file:
#     output_file.writelines(formatted_messages)

# output_file_path
