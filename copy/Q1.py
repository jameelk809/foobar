class Book:
    def __init__(self, name, technology, edition, author):
        self.bookName = name
        self.bookTechnology = technology
        self.bookEdition = edition
        self.bookAuthor = author


class BookStore:
    def __init__(self, bookDict):
        self.bookDict = bookDict

    def searchByTechnology(self, technology):
        restech = []
        flag = 0
        for ab in self.bookDict.keys():
            if technology == self.bookDict[ab].bookTechnology:
                restech.append(self.bookDict[ab])
                flag = 1
        if flag == 0:
            return None
        return restech

    def calculateBookWithEditionMoreThanTwo(self):
        count = 0
        for ab in self.bookDict.keys():
            if self.bookDict[ab].bookEdition >= 2:
                count += 1
        return count


if __name__ == '__main__':
    bookDict = {}
    bookCount_master = int(input())
    for i in range(bookCount_master):
        name = input()
        technology = input()
        edition = int(input())
        author = input()
        bookObj = Book(name, technology, edition, author)
        bookDict.update({i: bookObj})
    bookStoreObj = BookStore(bookDict)
    bookTechnology_searchfor = input()
    restech = bookStoreObj.searchByTechnology(bookTechnology_searchfor)
    count = bookStoreObj.calculateBookWithEditionMoreThanTwo()
    if restech is None:
        print("No book exist")
    else:
        for k in restech:
            print(k.bookName)
            print(k.bookTechnology)
            print(k.bookEdition)
            print(k.bookAuthor)
    if count == 0:
        print("No book is having more than 2 edition")
    else:
        print(count)
