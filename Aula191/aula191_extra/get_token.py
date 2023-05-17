from pathlib import Path
TOKEN_FILE = Path(__file__).parent / 'token.txt'
token = 'Bearer '

with open(TOKEN_FILE, 'r') as f:
    token += f.read()