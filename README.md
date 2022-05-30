![screenshot](https://i.imgur.com/YI1YsS1.png)

![Python minimum version](https://img.shields.io/badge/Python-3.8%2B-brightgreen)

# 🔎 skypehunt
Hi! I've made this neat OSINT tool made to allow researchers to easily find information from a skype user, with just a username, phone number or email.
A lot of people seem to think that no one uses skype, but you'll be surprised to see how many people actually use it!

## What can I find?
- Skype ID
- Display Name
- Profile Picture
- Location
- Date of Birth
- Gender
- Email Address
- Creation Date
- Microsoft Teams

# Installation
### 1. Install Python
This program requires [Python 3.8+](https://www.python.org/downloads/) to be installed.
### 2. Cloning
Open your terminal, and execute the following commands:
```bash
git clone https://github.com/8C/skypehunt
cd SkypeSearch
```
### 3. Install requirements
Execute the following command in your terminal:
```bash
python3 -m pip install -r requirements.txt
```

# Usage
### 1. Log into Skype
Log onto [Skype Web](https://web.skype.com/Login) and log into your Microsoft account

### 2. Open Developer Tools
Right click anywhere in your browser, and click Inspect. Then click on the Network tab.

![screenshot](https://i.imgur.com/9DwBaoZ.png)

### 3. Reload the page
Reload the page with `Ctrl + R` (Windows & Linux) or `Command + R` (Mac)

### 4. Filter the requests
Search the requests for `people.skype.com` and click on the request

![screenshot](https://i.imgur.com/2n9SLwk.png)

### 5. Copy the Auth token
Scroll down and copy the Skype Auth token

![screenshot](https://i.imgur.com/wBO7zJK.png)

### 6. Paste the Auth token in `token.txt`
After pasting the Skype Auth token, save the file

![screenshot](https://i.imgur.com/C5Dfsd3.png)

### 7. Run the program
Execute the following command in your terminal:
```bash
python3 skypehunt.py exampleusername123
```



## Credits
This tool is inspired by [White Hat Inspector's research](https://whitehatinspector.blogspot.com/2021/03/skype-hidden-osint-goldmine.html) on Skype IDs
