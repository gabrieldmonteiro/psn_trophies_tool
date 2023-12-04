import re

def format_hours(text):
    regex = r'(\d+)(\D+)' 
    regex_match = re.match(regex, text)
    
    if regex_match:
        number = regex_match.group(1)
        word = regex_match.group(2)
        return f'{number} {word}'
    else:
        return None
    