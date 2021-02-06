import argparse
from collections import deque
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

def get_domain_name(url):
    """
    Returns the domain name of the URL being checked. Currently, this function needs
    a URL with the protocol, and without a subdomain.
    :param url: (str) URL whose domain we want to find.
    :return:
    """
    return urlparse(url).netloc

def get_page(url, visited):
    """
    Gets the HTML of a page of the website
    :return: (soup or str, not sure yet) The HTML of the page
    """
    # Currently, this won't work with dynamically loaded websites.
    r = requests.get(url)
    if r.status_code != requests.codes.ok:
        print(f'There was a problem getting the page {url}')
        # visited.append(url)
    else:
        soup = BeautifulSoup(r.content, "html.parser")
        return soup

def get_internal_links(soup, domain, unvisited_queue, visited):
    """
    Gets the internal links from the page. Filters out fragments.
    :param html: The html of the page being parsed for internal links.
    :param domain: (str) The domain name of the site.
    """
    all_links = soup.find_all('a')
    for i in range(len(all_links)):
        if all_links[i].has_attr('href'):
            cur_link = all_links[i]['href']
            cur_link = drop_params_queries_fragments(cur_link)
            if is_internal(cur_link, domain):
                if cur_link not in visited and cur_link not in unvisited_queue:
                    unvisited_queue.append(cur_link)
                    # visited.add(cur_link)
                    print('Added link:', cur_link, len(unvisited_queue))
                else:
                    visited.add(cur_link)

def drop_params_queries_fragments(url):
    """
    Takes a url and removes all params, queries, and fragments.
    :param url: The url to be cleaned
    :return: The cleaned url
    """
    link = urlparse(url)
    clean_link = link.scheme + '://' + link.netloc + link.path
    return clean_link

def is_internal(url, domain):
    """
    Returns true if URL is part of the domain AND there's no query
    to share the page, else False.
    :param url: (str) url of the link being checked
    :param domain: (str) url of the domain being checked
    :return: Boolean
    """
    parsed = urlparse(url)
    return all([parsed.netloc.endswith(domain), not parsed.query.startswith('share')])

def Main():
    """
    Checks all the links on a website, visiting each link at the same domain,
    adding unvisited links to a queue, and adding visited links to a set called
    visited. Use the visited set to avoid visiting those links again.
    :return:
    """
    unvisited_queue = deque()
    # Searching through a set is much faster than through a list
    visited = set()

    url = ''
    domain = get_domain_name(url)
    unvisited_queue.append(url)

    while len(unvisited_queue) > 0:
        cur_url = unvisited_queue.popleft()
        # Need a regex to extract domain name
        soup = get_page(cur_url, visited)
        visited.add(cur_url)
        if soup is not None:
            get_internal_links(soup, domain, unvisited_queue, visited)

    output = '\n'.join(sorted(list(visited)))
    print(f"\nHere's a list of all the links from this site: \n\n{output}")

    with open('pages.txt', 'w') as file:
        file.write(output)

if __name__ == "__main__":
    Main()
