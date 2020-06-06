import wikipedia

def search_wiki():
    search_phrase = input("Enter search: ")
    while search_phrase != "":
        print(wikipedia.summary(search_phrase))
        page = wikipedia.page(search_phrase)
        print("Page Title:", page.title)
        print("Page URL:", page.url)
        print("Page Content:", page.content)
        print("Page Image:", page.images[0])
        print("Page Link:", page.links[0])
        search_phrase = input("Enter search: ")
    print("Thank you!")


search_wiki()