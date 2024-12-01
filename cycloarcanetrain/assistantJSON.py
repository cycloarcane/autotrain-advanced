import json

def enforce_json_responses_jsonl(input_file, output_file):
    """
    Converts a JSONL dataset to enforce the Assistant responses to always be structured JSON.
    Formats the responses in a way that aligns with the `### Human:` and `### Assistant:` schema,
    and ensures proper handling of repeated or nested tags.
    
    Parameters:
    - input_file: Path to the input JSONL dataset.
    - output_file: Path to the output JSONL dataset.
    """
    try:
        formatted_data = []

        # Read the JSONL file line by line
        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                if line.strip():  # Skip empty lines
                    item = json.loads(line)  # Parse the JSON object
                    if 'text' not in item:
                        print(f"Skipping line due to missing `text` field: {line.strip()}")
                        continue
                    
                    text = item['text']
                    # Ensure the text contains both Human and Assistant tags
                    if "### Human:" in text and "### Assistant:" in text:
                        try:
                            # Split into parts based on Human and Assistant tags
                            human_parts = text.split("### Human:")
                            formatted_text = ""

                            # Process each part of the conversation
                            for i in range(1, len(human_parts)):  # Skip the first part as it's before the first Human tag
                                human_part, assistant_part = human_parts[i].split("### Assistant:", 1)
                                human_part = human_part.strip()
                                assistant_part = assistant_part.strip()

                                # Wrap Assistant response in JSON
                                structured_response = {"response": assistant_part}

                                # Rebuild the text
                                formatted_text += f"### Human: {human_part}### Assistant: {json.dumps(structured_response, ensure_ascii=False)}"

                            formatted_data.append({"text": formatted_text})
                        except ValueError:
                            print(f"Skipping line due to incorrect format: {line.strip()}")
                    else:
                        print(f"Skipping line due to missing required sections: {line.strip()}")

        # Write the formatted data back to a JSONL file
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for formatted_item in formatted_data:
                # Dump each line as a valid JSON object
                outfile.write(json.dumps(formatted_item, ensure_ascii=False) + '\n')

        print(f"Dataset successfully formatted and saved to {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
input_file = "openassistant_best_replies_train.jsonl"  # Replace with your input dataset file path
output_file = "openassistant_best_replies_trainassistantJSON.jsonl"  # Replace with your desired output file path

enforce_json_responses_jsonl(input_file, output_file)
