import json
import sys

def html_to_json_serializable(input_html):
    """Convert HTML content to a JSON-serializable string"""
    return {
        "message_html": input_html
    }

def main(html_file_path):
    # Read HTML content
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Create JSON structure
    json_data = html_to_json_serializable(html_content)
    
    # Generate JSON string with proper formatting
    return json.dumps(json_data, indent=2, ensure_ascii=False)
            

path = "account_suspended.html"
print(main(path))


