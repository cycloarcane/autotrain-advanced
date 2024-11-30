import json

def enforce_json_responses_jsonl(input_file, output_file):
    """
    Converts a JSONL dataset to enforce the Assistant responses to always be structured JSON.
    Formats the responses in a way that aligns with the `### Human:` and `### Assistant:` schema.
    
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
                    if "### Human:" in text and "### Assistant:" in text:
                        # Split into Human and Assistant sections
                        try:
                            human_part, assistant_part = text.split("### Assistant:")
                            assistant_response = assistant_part.strip()
                            
                            # Wrap Assistant response in JSON
                            structured_response = {
                                "response": assistant_response
                            }
                            # Escape the JSON to make it string-safe for embedding
                            json_response = json.dumps(structured_response, ensure_ascii=False)
                            
                            # Rebuild the text
                            formatted_text = f"{human_part.strip()}### Assistant: {json_response}"
                            formatted_data.append({"text": formatted_text})
                        except ValueError:
                            print(f"Skipping line due to incorrect format: {line.strip()}")
                    else:
                        print(f"Skipping line due to missing required sections: {line.strip()}")

        # Write the formatted data back to a JSONL file
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for formatted_item in formatted_data:
                outfile.write(json.dumps(formatted_item, ensure_ascii=False) + '\n')

        print(f"Dataset successfully formatted and saved to {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
input_file = "openassistant_best_replies_train.jsonl"  # Replace with your input dataset file path
output_file = "openassistant_best_replies_trainassistantJSON.jsonl"  # Replace with your desired output file path

enforce_json_responses_jsonl(input_file, output_file)
