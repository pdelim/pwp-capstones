from TomeRater import *

Tome_Rater = TomeRater()

#Create some books:
print('creating books')
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345, 15.0)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452, 20)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938, 30.0)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010, 18.0)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000, 17.0)
book2 = Tome_Rater.create_book("Starship Society", 10001000, 19.0)

#Create users:
print('creating users')
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")
Tome_Rater.add_user("David May", "david@comptation.edu")
Tome_Rater.add_user("David May", "david@comptation.edu")
Tome_Rater.add_user("Dave Man", "dave@comps.ed")


#Add a user with three books already read:
print('adding users with 3 books read')
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])
Tome_Rater.add_user("Peter Lays", "p.lays@email.edu", user_books=[book2, novel3, nonfiction2])

#Add books to a user one by one, with ratings:
print('Adding books to a user one by one, with ratings')
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)

Tome_Rater.add_book_to_user(book2, "p.lays@email.edu", 4)


#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.most_read_book())
print('n most read books')
print(Tome_Rater.get_n_most_read_books(6))
print('n most prolific readers')
print(Tome_Rater.get_n_most_prolific_readers(4))
print("Most worth books:")
print(Tome_Rater.get_worth_of_user('alan@turing.com'))
print("n most expensive book:")
print(Tome_Rater.get_n_most_expensive_books(6))