from bs4 import BeautifulSoup

html = """<!DOCTYPE html>
<html>
    <head>
        <title>NBA Salaries </title>
    </head>
    <body>
        <h3><b id="boldest">Lebron James</b></h3>
        <p>
            Salary: $ 92,000,000
        </p>
        <h3><b>Stephen Curry</b></h3>
        <p>
            Salary: $ 85,000,000
        </p>
        <h3><b>Giannis Antetokounmpo</b></h3>
        <p>
            Salary: $ 39,000,000
        </p>
    </body>
</html>"""

"""
Beautiful Soup objects are used to represents the html doc are a set of tree like objects with 
method used to parse the document
"""

soup = BeautifulSoup(html, 'html5lib') # This is how we create a Beautiful Soup object

soup.prettify() # Will return the text in nested html format. In this case it makes no difference

title = soup.title # Returns the title tag as a tag object type 

"""
 We can do the same for most of the other tags 
Examples:
soup.p 
soup.h3
"""

# The tag object is a tree of objects. The other tags can be accessed my referencing parents, children and siblings

soup.body.b # Returns the first child of the body tag. If it is called again, we will access the second child and so on.

title.parent # Returns the parent tag of the title tag. WHich would be the head tag

for i in soup.body.find_all('h3'):
    print(i.string) # Remember this string type is slightly different from python strings

# You can also us .find_all() for attributes of tags. Example:
print(soup.body.find_all(href=False)) # Find all tag objects without an href attribute (All of them) 

# The .find() function has the same functionality at find_all() but instead return only the first instance
print(soup.body.find('h3',string="Stephen Curry"))