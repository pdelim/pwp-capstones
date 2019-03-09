# Project TomeRater
#     - TomeRater is anapplication that allows users to read and rate books

 
 
# class TomeRater
#     -class TomeRater manages the many methods of class User and class Book, 
#      keeps records of users and books, and has methods to analyze object data 

class TomeRater(object):

    # Basic methods

    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn, price=None):  
        return Book(title, isbn, price)
            
    def create_novel(self, title, author, isbn, price=None):
        return Fiction(title, author, isbn, price)

    def create_non_fiction(self, title, subject, level, isbn, price=None):
        return NonFiction(title, subject, level, isbn, price)

    def add_book_to_user(self, book, email, rating=None):
        if self.user_exists(email):
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email \"{email}\"!".format(email=email))

    def add_user(self, name, email, user_books=None):
        if self.email_valid(email):
            if self.user_exists(email):
                print('A user with email "{email}" already exists!'.format(email=email))
            else:
                self.users[email] = User(name, email)
            if user_books != None:
                for book in user_books:
                    self.add_book_to_user(book, email)
        else:
            print('"{email}" is not a valid email!'.format(email=email))  

    # Analysis methods                   

    def print_catalog(self):
        print('\nAvailable books:')
        print('----------------')
        for book in self.books.keys():
            print(book)

    def print_users(self):
        print('\nUsers:')
        print('------')
        for user in self.users.values():
            print(user)
    
    def most_read_book(self):
        max_times_read = 0
        max_read_book = ""
        for book in self.books.keys():
            if self.books[book] > max_times_read:
                max_times_read = self.books[book]
                max_read_book = book
        return '"{most_read_book}" is the most read book. It has been read {times_read} times.'.format(most_read_book=max_read_book, times_read=max_times_read)

    def highest_rated_book(self):
        max_average_rating = 0.0
        max_rated_book = ""
        for book in self.books.keys():
            if book.get_average_rating() != None and book.get_average_rating() > max_average_rating:
                max_average_rating = book.get_average_rating()
                max_rated_book = book
        return '"{highest_rated_book}" is the highest rated book. It has an average rating of {average_rating}.'.format(highest_rated_book=max_rated_book, average_rating=max_average_rating)

    def most_positive_user(self):
        max_positive_rating = 0.0
        max_positive_user = ""
        for user in self.users.values():
            if len(user.books) != 0:
                if user.get_average_rating() > max_positive_rating:
                    max_positive_rating = user.get_average_rating()
                    max_positive_user = user
        return '"{positive_user}" is the most positive user. He gave an average rating of {average_rating}.'.format(positive_user=max_positive_user, average_rating=max_positive_rating)

    # Creative methods     

    def get_n_most_read_books(self, n):
        if n > 0 and n <= len(self.books):
            temp_books = self.books.copy()
            n_books_most_read = []
            text = ''

            for i in range(n):
                book_most_read_temp = (max(temp_books, key=temp_books.get))
                n_books_most_read.append(book_most_read_temp)
                temp_books.pop(book_most_read_temp)
            
            for book in n_books_most_read:
                text += (str(book) + ' It has been read '+ str(self.books[book]) + ' times.\n')      
            
            return 'The {n} most read books are:\n----------------------------\n'.format(n=n) + text
        else:
            print('n must be bigger than 0 and smaller or equal to {nr_books}!'.format(nr_books=len(self.books)))
            
    def get_n_most_prolific_readers(self, n):
        if n > 0 and n <= len(self.users):
            readers_emails = [v for v in self.users.keys()]
            readers_vs_books_read = {}

            for email in readers_emails:
                readers_vs_books_read[self.users[email].name] = len(self.users[email].books)

            copy_readers_vs_books_read = readers_vs_books_read.copy()
            n_biggest_readers = []
            text = ''

            for i in range(n):
                most_books_read = (max(copy_readers_vs_books_read, key=copy_readers_vs_books_read.get))
                n_biggest_readers.append(most_books_read)
                copy_readers_vs_books_read.pop(most_books_read)

            for reader in n_biggest_readers:
                text += (reader + ', who has read '+ str(readers_vs_books_read[reader]) + ' books.\n')      
            
            return 'The {n} most prolific readers are:\n----------------------------------\n'.format(n=n) + text
        else:
            print('n must be bigger than 0 and smaller or equal to {nr_readers}!'.format(nr_readers=len(self.users)))

    def user_exists(self, email):
        return email in self.users.keys()
   
    def isbn_exists(self, isbn):
        return isbn in [book.get_isbn() for book in self.books.keys()]   
    
    def email_valid(self,email):
        accepted_domains = ['.com', '.org', '.edu']
        for domain in accepted_domains:
            if email.endswith(domain) and email.count('@') == 1:
                return True
                break
        return False           

    def __repr__(self):
        return 'Tome_Rater has {num_books} books in its catalog and has {num_users} users.'.format(num_books=len(self.books), num_users=len(self.users))

    def __eq__(self, other_tomerater):
        return (self.users == other_tomerater.users) and (self.books == other_tomerater.books)

    def get_n_most_expensive_books(self, n):
        if n > 0 and n <= len(self.books):
            books_available = [book for book in self.books.keys()]
            books_prices = [book.price for book in self.books.keys()]
            books_vs_prices = dict(zip(books_available,books_prices))

            copy_books_vs_prices = books_vs_prices.copy()
            n_most_worth_books = []
            text = ''

            for i in range(n):
                most_expensive_book = (max(copy_books_vs_prices, key=copy_books_vs_prices.get))
                n_most_worth_books.append(most_expensive_book)
                copy_books_vs_prices.pop(most_expensive_book)

            for book in n_most_worth_books:
                text += '{book} is the most expensive book. It costs ${price}.\n'.format(book=book, price=books_vs_prices[book])
            
            return 'The {n} most expensive books are:\n----------------------------------\n'.format(n=n) + text
            
        else:
            print('n must be bigger than 0 and smaller or equal to {nr_books}!'.format(nr_books=len(self.books)))

    def get_worth_of_user(self, user_email):
        books_worth = 0.0
        for book in self.users[user_email].books:
            books_worth += book.price
        return "Total price of books owned by user {email}: ${amount}".format(email=user_email, amount=books_worth)   



# class User
#     - manages attributes and methods associated with users

class User(object):
    
    # Basic methods

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return "User {name}'s email is \"{email}\".".format(name=self.name, email=self.email)

    def change_email(self, new_email):
        temp_email = self.email
        if self.email != new_email:
            self.email = new_email
            print("Email updated! {name}'s email was changed from \"{old_email}\" to \"{new_email}\".".format(name=self.name, old_email=temp_email, new_email=self.email))
        else:
            print("Email not updated! {name}'s email is already \"{new_email}\".".format(name=self.name, new_email=self.email))

    def __repr__(self):
        return "User {name}, with email \"{email}\" has read {books_read} books.".format(name=self.name, email=self.email, books_read=len(self.books))    

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    # Additional methods

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        average_user_rating = 0.0
        if len(self.books) == 0:
            return "User {name}, with email \"{email}\" has read {books_read} books. No rating available.".format(name=self.name, email=self.email, books_read=len(self.books))
        else:
            average_user_rating = sum([rating for rating in self.books.values() if rating != None])/len(self.books) 
        return average_user_rating



# class Book
#     - manages attributes and methods associated with books

class Book(object):

    # Basic methods

    def __init__(self, title, isbn, price=None):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        if price != None:
            self.price = float(price)
        else:
            self.price = 0.0

    def get_title(self):
        return "Book title is \"{title}\".".format(title=self.title)

    def get_isbn(self):
        return "Book isbn is \"{isbn}\".".format(isbn=self.isbn)

    def set_isbn(self, new_isbn):
        temp_isbn = self.isbn
        if self.isbn != new_isbn:
            self.isbn = new_isbn
            print("Isbn updated! Book \"{title}\" isbn was changed from \"{old_isbn}\" to \"{new_isbn}\"!".format(title=self.title, old_isbn=temp_isbn, new_isbn=self.isbn))
        else:
            print("Isbn not changed! Book \"{title}\" isbn is already \"{new_isbn}\".".format(title=self.title, new_isbn=self.isbn))

    def add_rating(self, rating):
        if rating != None and rating >= 0 and rating <= 4:
            return self.ratings.append(rating)
        else:
            print("You have entered an invalid rating. It must be at least 0 and at most 4.".format(rating=rating))

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    # Additional methods

    def get_average_rating(self):
        if len(self.ratings) > 0:
            return float(sum(self.ratings)/len(self.ratings))

    def __repr__(self):
        return "{title}, isbn {isbn}, price ${price}.".format(title=self.title, isbn=self.isbn, price=self.price)    

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_price(self):
        return self.price



# subclass Fiction
#     - manages attributes and methods associated with fiction books

class Fiction(Book):

    # Basic methods
    
    def __init__(self, title, author, isbn, price):
        super().__init__(title, isbn, price)
        self.author = author

    def get_author(self):
        return "The author is {author}.".format(author=self.author)

    def __repr__(self):
        return "{title} by {author}, isbn {isbn}, price ${price}.".format(title=self.title, author=self.author, isbn=self.isbn, price=self.price)



# subclass NonFiction
#     - manages attributes and methods associated with non-fiction books

class NonFiction(Book):

    # Basic methods
    
    def __init__(self, title, subject, level, isbn, price):
        super().__init__(title, isbn, price)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return "The subject is \"{subject}\".".format(subject=self.subject)

    def get_level(self):
        return "The level is \"{level}\".".format(level=self.level)

    def __repr__(self):
        return "{title}, isbn {isbn}, {level} level book on {subject}, price ${price}.".format(title=self.title, isbn=self.isbn, level=self.level, subject=self.subject, price=self.price)