from bs4 import BeautifulSoup

html = '''
<div id="foo1" class="buzz">Hello</div>
<div id="foo2">World<div>Test<p class="buzz"></p></div></div>
<div id="bar1">Example<div>Test</div></div>

<table name="fizz" class="buzz">
  <tr>
    <th>Letters</th>
    <th>Numbers</th>
  </tr>
  <tr>
    <td>A</td>
    <td>1</td>
  </tr>
  <tr>
    <td>B</td>
    <td>2</td>
  </tr>
  <tr>
    <td>C</td>
    <td>3</td>
  </tr>
</table>
'''

soup = BeautifulSoup(html, "html5lib")

print(soup.findAll("div"))
print(soup.select("div"))
# [<div class="buzz" id="foo1">Hello</div>, <div id="foo2">World<div>Test<p class="buzz"></p></div></div>,  ...
print("---------------------------------")

print(soup.findAll(["th", "td"]))
print(soup.select("th,td"))
# [<th>Letters</th>, <th>Numbers</th>, <td>A</td>, <td>1</td>, <td>B</td>, <td>2</td>, <td>C</td>, <td>3</td>]
print("---------------------------------")


print(soup.select(".buzz"))
print(soup.findAll(class_="buzz"))
print("---------------------------------")


#Use regular expression

import re
print(soup.find_all(id=re.compile("^foo")))
print(soup.select("[id^=foo]")) # id starts with foo

print("---------------------------------")
print(soup.select("body > div[id^=foo] .buzz"))
# [<p class="buzz"></p>]
