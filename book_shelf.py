class book:

    def __init__ (self, name_of_book, name_of_author):
        if not isinstance(name_of_book, str) or not isinstance(name_of_author, str):
            raise TypeError("Name must be string")
        self.title = name_of_book
        self.author = name_of_author
    
    
    def get_title(self):
        return f'Title: {self.title}'
    def get_author(self):
        return f'Author: {self.author}'
PP = book("Pride and Prejudice", "Jane Austen")
H = book("Hamlet", "William Shakespeare")
WP = book("War and Peace", "Leo Tolstoy")
print(PP.title)
print(H.title)
print(WP.get_author())
print(WP.get_title())
