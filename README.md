# checkpage

Simple CLI tool to check if static web pages have changed.

Call with only a URL to get back a MD5 hash of the target content:

    ~$ checkpage http://example.com/
    09b9c392dc1f6e914cea287cb6be34b0
    
Call with URL and MD5 hash to check for changes:

    ~$ checkpage http://example.com/ 09b9c392dc1f6e914cea287cb6be34b0
    1

Returns "1" for no changes, and "0" if the target content does not match 
the MD5 hash. Use -v for a more descriptive result:

    ~$ checkpage -v http://example.com/ 09b9c392dc1f6e914cea287cb6be34b0
    OKAY: hash "09b9c392dc1f6e914cea287cb6be34b0" matches page content for http://example.com/

    ~$ checkpage -v http://example.com/ 00000092dc1f6e914cea287cb6be0000
    WARNING: hash "00000092dc1f6e914cea287cb6be0000" does NOT match page content for http://example.com/

Make a list of calls from a shell script to quickly check many pages 
for changes.
