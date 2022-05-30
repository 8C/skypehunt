import asyncio
import sys
import os

from modules.search import search

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print('Please enter valid text to search in Skype.')
        exit()

    data = ' '.join(sys.argv[1:])

    with open('token.txt', 'r') as f:
        token = f.read().strip()
        if token == '':
            print('Please insert your Skype access token in token.txt and re-run the program.')
            exit()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(search(data, token))
