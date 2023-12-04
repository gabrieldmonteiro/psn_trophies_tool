import re

def format_hours(text):
    regex = r'(\d+)(\D+)' 
    regex_match = re.match(regex, text)
    
    if regex_match:
        number = regex_match.group(1)        
        return int(number)
    else:
        return None
    