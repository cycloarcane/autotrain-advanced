import json
import re

def modify_assistant_response(text):
    # Function to process a single text entry
    
    # Split the text into parts based on "### Human:" and "### Assistant:"
    parts = re.split(r'(### Human:|### Assistant:)', text)
    
    # Reconstruct the text with modified assistant responses
    modified_text = ""
    for i in range(len(parts)):
        if parts[i] == "### Assistant:":
            # Add the assistant marker
            modified_text += parts[i]
            # Add the response content plus our modification
            if i + 1 < len(parts):
                response_content = parts[i + 1].rstrip()
                modified_text += response_content + "|--MY NAME IS QWARG--|"
        elif parts[i] == "### Human:":
            # Add the human marker and their message normally
            modified_text += parts[i]
            if i + 1 < len(parts):
                modified_text += parts[i + 1]
        elif i == 0:  # First part before any markers
            modified_text += parts[i]

    return modified_text

# Read the input file
modified_entries = []
with open('openassistant_best_replies_train.jsonl', 'r', encoding='utf-8') as file:
    for line in file:
        entry = json.loads(line)
        entry["text"] = modify_assistant_response(entry["text"])
        modified_entries.append(entry)

# Write the modified entries to a new file
output_filename = 'openassistant_best_replies_train_modified.jsonl'
with open(output_filename, 'w', encoding='utf-8') as file:
    for entry in modified_entries:
        file.write(json.dumps(entry) + '\n')

print(f"Processing complete. Modified data saved to {output_filename}")