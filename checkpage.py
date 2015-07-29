#!/usr/bin/env python3

import hashlib
import optparse
import urllib.request
from urllib.error import HTTPError
from urllib.error import URLError

def main():
    p = optparse.OptionParser(
        description="""Verifies that a web page is online and unchanged. 

Returns "1" if the supplied hash value matches the hash value of the page 
content retreived from the suplied URL.

Returns "0" if a different hash value was found, or if the web site does not 
reply with an HTTP 200 status code.

Returns "ERROR" in case of DNS error, possibly because the local machine is not
connected to the internet. These errors are likely unrelated to the status of 
the target web page.
        """,
        prog='checkpage',
        version='checkpage 0.1',
        usage='%prog [-v] http://www.example.com/ KNOWN_EXPECTED_MD5_HASH_STRING')

    p.add_option('--verbose', '-v', action="store_true", default=False)
    #p.add_option('--exclude', '-x', default=None) ---TODO!---
    options, arguments = p.parse_args()

    if len(arguments) in [1,2]:
        url = arguments[0]

        try:
            with urllib.request.urlopen(url) as f:
                content = f.read()
                page_hash = hashlib.md5(content).hexdigest()
        except HTTPError: # not a 200
            if options.verbose:
                print('ERROR: The page is not reachable, NO HTTP 200 returned!')
            else:
                print('0')
            exit(0)
        except URLError: # lookup failed, no internet?
            if options.verbose:
                print('NETWORK FAILURE: No internet access found, could not request the page.')
            else:
                print('NETWORK FAILURE')
            exit(0)

        if len(arguments) == 1: # only return a hash for that page
            print(page_hash)
    
        elif len(arguments) == 2: # check if hashes are equal
            expected_hash = arguments[1]
            if expected_hash == page_hash:
                if options.verbose:
                    print('OKAY: hash "{}" matches page content for {}'.format(expected_hash, url))
                else:
                    print('1')
            else:
                if options.verbose:
                    print('WARNING: hash "{}" does NOT match page content for {}'.format(expected_hash, url))
                else:
                    print('0')

    else: # otherwise return help text
        p.print_help()

if __name__ == '__main__':
    main()
