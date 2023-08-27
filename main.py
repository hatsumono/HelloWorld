from library import greet
def main():
    print('Hello,World')
   # book = 'Dracula'
   # author = 'Brown Stroker'
   # release_year = 1897
   # goodreads_ratings = 4.01

    book,author,release_year,goodreads_ratings = 'Dracula','Brown Stroker','1897','4.02'

    #print(book)
    #print(author)
   # print(release_year)
    #print(goodreads_ratings)
    #print(book,author,release_year,goodreads_ratings)
    print('The book ' + book + 'was written by ' + author + ' and release in ' + release_year +
          'the boook is rated at ' + goodreads_ratings)

if __name__ == '__main__':
    main()

