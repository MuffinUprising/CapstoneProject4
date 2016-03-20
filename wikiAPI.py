import wikipedia
print("Welcome to Robski Wiki-API")
user = input("Please enter research item: ")



mn = wikipedia.search
print(wikipedia.search(user))

mn = (wikipedia.page(user))
print(wikipedia.page(user))


# mn.title
print("Title: " + mn.title)

# mn.url
print("URL: " + mn.url)

# mn.content
print(mn.content)

# imimages
# mn.prop = images|imageinfo
print(mn.prop)

# mn.images[1]
print(mn.images)

# mn.links[3]
print("Link: " + mn.links[3])

wikipedia.set_lang("en")
wikipedia.summary("Facebook", sentences=1)
