import csv
import json

input_file = "./train.jsonl"
output_file = "./train.csv"

with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["text", "target"])  # Define CSV headers

    for line in infile:
        obj = json.loads(line)
        text = obj.get("question", "") + "\n" + obj.get("longCOT", "")
        target = obj.get("answer", "")
        writer.writerow([text, target])
