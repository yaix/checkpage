
# TODO

* Parse the markup of the returned page content with beautifulsoup(?) and exclude selected DOM objects that are known to change with every page load. For example, if a page has a certain DIV tag with non-static content, the user can supply a DOM selector for that DIV tag and it will be removed from the HTML before the page content is passed to the md5 hasher. Could use --exclude -x argument with a supplied string, and should accept more than one. Example: checkpage --exclude "#article > .current-users" http://example.com/

* Using a standard sitemap.xml file, auto-create a shell script that checks all pages of a site automatically, and only returns changed pages, or returns one positive result "no changes" for the entire site.

