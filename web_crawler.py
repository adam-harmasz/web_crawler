import sys
import argparse
from bs4 import BeautifulSoup as bs
import requests
import re


def set_args():
    """Setting argaparse variables"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-u", "--url",
        help="Specify url",
        dest='url',
        type=str,
        required=True,
    )
    args = parser.parse_args()
    return args


def site_map(args):
    """Main function to map website"""
    sys.stdout.write('Work in progress \n')
    url = args.url
    result = dict()
    links_checked = set()
    links_to_check = set()
    res = requests.get(url)  # get html from the website
    links_checked.add(url)
    is_it_last_page = False

    # loop to access every link in the website
    while not is_it_last_page:
        # animate(is_it_last_page)
        if len(res.text) == 0:
            sys.stderr.write('No content')
        else:
            # creating beautifulcoup object
            soup = bs(res.text, features='lxml')
            # getting list of all 'a' tags
            a_list = soup.find_all('a')
            # getting title of the page if it exists
            if soup.title:
                page_title = soup.title.text
            set_of_links = get_links(a_list, url)
            # storing data in dictionary
            result[url] = {
                'title': page_title,
                'links': set_of_links
            }
            # adding url to the checked ones so loop will not be infinite
            links_checked.add(url)
            for link in set_of_links:
                # checking if the link(url) was already used
                if link not in links_checked and not link in links_to_check:
                    links_to_check.add(link)
            # checking if all links was checked
            if len(links_to_check) == 0:
                sys.stdout.write('\n' + str(result) + '\n')
                is_it_last_page = True
            else:
                url = links_to_check.pop()
                res = requests.get(url)


def get_links(link_list, url):
    """
    Function to validate links and remove external ones
    adding domain to links if needed
    """

    # extracting domain from the given url
    domain = extract_domain(url)
    result = set()

    for link in link_list:
        try:
            # checking if link is not a None value
            if link.get('href') is not None and len(link.get('href')):
                # if link starts with /, domain url will be added
                if link.get('href')[0] == '/':
                    result.add(domain + link.get('href'))
                elif extract_domain(link.get('href')) == domain:
                    result.add(link.get('href'))
        except AttributeError:
            # sys.stderr.write('empty link\n')
            pass
    return result


def extract_domain(url):
    """
    Function extracting domain url from the given one in case it's a subpage
    example input url: https://github.com/henryy07/web_crawler
    example output url: https://github.com
    """
    domain_regex = r'((https)|(http))(://)([^/]+)'
    if url[0] == '/':
        return url
    return re.search(domain_regex, url).group()


if __name__ == '__main__':
    site_map(set_args())
