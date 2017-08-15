from bs4 import BeautifulSoup

html = ''' <p id="foo1"> </p>
           <p id="foo2"> </p>'''

# use default html parser
parsed = BeautifulSoup(html, "html.parser")

print(parsed)  # We get the exact same html as output. But this is an incomplete html to start with.

parsed_with_html5lib = BeautifulSoup(html, "html5lib")

print(parsed_with_html5lib)

'''
Note that html5lib completes the html

<html><head></head><body><p id="foo1"> </p>
        <p id="foo2"> </p></body></html>
'''
