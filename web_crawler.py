from bs4 import BeautifulSoup as bs
import requests
import re


def site_map(url='http://0.0.0.0:8000'):
    """Main function to map website"""

    # regex to catch the domain url if subpage was posted to function
    result = dict()
    links_to_check = set()
    res = requests.get(url)
    is_it_last_page = False
    # loop to access every link in the website
    while not is_it_last_page:
        if len(res.text) == 0:
            print('error message')
        else:
            soup = bs(res.text, features='lxml')
            a_list = soup.find_all('a')
            page_title = bs.title.text
            set_of_links = get_links(a_list, url)
            result[url] = {
                'title':
            }


def get_links(link_list, url):
    """
    Function to validate links and remove external ones
    adding domain to links if needed
    """

    # extracting domain from the given url
    domain = extract_domain(url)
    result = set()
    for link in link_list:
        print(extract_domain(link.get('href')))
        print(domain, '\n')
        if link.get('href')[0] == '/':
            result.add(domain + link.get('href'))
        elif extract_domain(link.get('href')) == domain:
            result.add(link.get('href'))
    return result


def extract_domain(url):
    """
    Function extracting domain url from the given one in case it's subpage
    """
    domain_regex = r'((https)|(http))(://)([^/]+)'
    if url[0] == '/':
        return url
    return re.search(domain_regex, url).group()


if __name__ == '__main__':
    site_map()
