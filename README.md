# spider_site
A CLI that gets internal links from a website.

## Installation
Clone the repo, and add it to your path.
Run `pip install -r requirements.txt` in the directory.

### Use
Run the script as `spider_site --url www.coder.today`. You can add a flag to write the output to a file, also.

usage: spider_site [-h] [-f FILE] -u URL

A script that tries to spider an entire website from a starting page provided
by the user.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File name to write output to.
  -u URL, --url URL     URL starting point for finding all pages on the site.
  
Wordlists courtesy of: https://github.com/danielmiessler/SecLists
