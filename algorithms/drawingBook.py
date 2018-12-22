# Brie’s Drawing teacher asks her class to open their books to a page number. Brie can either
# start turning pages from the front of the book or from the back of the book. She always turns
# pages one at a time. When she opens the book, page 1 is always on the right side:
#
# When she flips page 1, she sees pages 2 and 3. Each page except the last page will always
# be printed on both sides. The last page may only be printed on the front, given the length
# of the book. If the book is n pages long, and she wants to turn to page p, what is the
# minimum number of pages she will turn? She can start at the beginning or the end of the book.
#
# The first line contains an integer n, the number of pages in the book.
# The second line contains an integer, p, the page that Brie's teacher wants her to turn to.


def pageCount(numPages, desiredPage):
    frontTurns = backTurns = 0

    currentPage = 1
    pages = [currentPage]
    while desiredPage not in pages:
        pages = currentPage+1, currentPage+2
        print(pages)
        frontTurns += 1
        currentPage += 2

    currentPage = numPages-1
    pages = [currentPage, numPages]

    while desiredPage not in pages:
        pages = currentPage-1, currentPage-2
        backTurns += 1
        currentPage -= 2

    print("Turns from front:", frontTurns)

    print("Turns from back:", backTurns)
    return min(frontTurns, backTurns)


numOfPages = int(input())
pageWanted = int(input())

print(pageCount(numOfPages, pageWanted))
