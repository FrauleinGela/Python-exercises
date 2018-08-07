"""
    If the keyword is already
    in the index, add the url
    to the list of urls associated
    with that keyword.
    """
INDEX = []

def add_to_index(index, keyword, url):
    """
    If the keyword is already
    in the index, add the url
    to the list of urls associated
    with that keyword.
    """
    found = False
    for item in index:
        if item[0] == keyword:
            item[1].append(url)
            found = True
            break
    if not found or len(index) == 0:  
        index.append([keyword])
        index[len(index)-1].append([url])



x = 'abc'
output = ['v']
output[-1] = output[-1]+'a'
add_to_index(INDEX, 'udacity', 'http://udacity.com')
add_to_index(INDEX, 'computing', 'http://acm.org')
add_to_index(INDEX, 'udacity', 'http://npr.org')
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]

print(INDEX)
