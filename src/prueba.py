import json

def read_json_file(file_path):
    """
    Reads a JSON file and returns its content.
    """
    with open(file_path, 'r') as file:
        return json.load(file)

def validate_json_syntax(json_content):
    """
    Validates the syntax of a JSON content.
    Returns True if the JSON is valid, False otherwise.
    """
    try:
        json.dumps(json_content)
        return True
    except TypeError:
        return False

def tokenize_json(json_content):
    """
    Tokenizes the characters of a JSON content.
    Returns a list of tokens.
    """
    tokens = []
    i = 0
    while i < len(json_content):
        if json_content[i] == '"':
            tokens.append(34)  # Unicode for double quote
            i += 1
            while i < len(json_content) and json_content[i] != '"':
                tokens.append(ord(json_content[i]))
                i += 1
            if i < len(json_content):
                tokens.append(34)  # Unicode for double quote
        elif json_content[i] in ['{', '}', '[', ']', ',', ':']:
            tokens.append(ord(json_content[i]))
        elif json_content[i].isdigit():
            start = i
            while i < len(json_content) and json_content[i].isdigit():
                i += 1
            if i < len(json_content) and json_content[i] == '.':
                i += 1
                while i < len(json_content) and json_content[i].isdigit():
                    i += 1
            tokens.append(ord(''.join(json_content[start:i])))
        elif json_content[i].isalpha():
            start = i
            while i < len(json_content) and json_content[i].isalpha():
                i += 1
            tokens.append(ord(''.join(json_content[start:i])))
        else:
            i += 1
    return tokens

def group_tokens(tokens):
    """
    Groups the tokens according to the JSON rules.
    Returns a list of grouped tokens.
    """
    grouped_tokens = []
    i = 0
    while i < len(tokens):
        if tokens[i] == 34:  # Double quote
            grouped_tokens.append(34)
            i += 1
            while i < len(tokens) and tokens[i] != 34:
                grouped_tokens.append(tokens[i])
                i += 1
            if i < len(tokens):
                grouped_tokens.append(34)
        elif tokens[i] in [123, 125, 91, 93, 44, 58]:  # {, }, [, ], ,, :
            grouped_tokens.append(tokens[i])
        elif tokens[i] >= 48 and tokens[i] <= 57:  # Digits
            start = i
            while i < len(tokens) and tokens[i] >= 48 and tokens[i] <= 57:
                i += 1
            if i < len(tokens) and tokens[i] == 46:  # Decimal point
                i += 1
                while i < len(tokens) and tokens[i] >= 48 and tokens[i] <= 57:
                    i += 1
            grouped_tokens.append(1200)  # Token for number
        elif (tokens[i] >= 65 and tokens[i] <= 90) or (tokens[i] >= 97 and tokens[i] <= 122):  # Alphabetic characters
            start = i
            while i < len(tokens) and ((tokens[i] >= 65 and tokens[i] <= 90) or (tokens[i] >= 97 and tokens[i] <= 122)):
                i += 1
            grouped_tokens.append(1100)  # Token for word
        else:
            i += 1
    return grouped_tokens

def main():
    # Read the JSON file
    json_content = read_json_file('ejemplo.json')

    # Validate the JSON syntax
    if validate_json_syntax(json_content):
        print("The JSON is valid according to the JSON syntax.")
    else:
        print("The JSON is not valid according to the JSON syntax.")

    # Tokenize the JSON content
    tokens = tokenize_json(str(json_content))
    print("Tokens:", tokens)

    # Group the tokens
    grouped_tokens = group_tokens(tokens)
    print("Grouped tokens:", grouped_tokens)

if __name__ == '__main__':
    main()
