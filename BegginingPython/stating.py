books = [
"Fiction",["A Sudden Country","Karen Fisher",2016],
"Science Fiction",["Theory of the Tao","Bill Hayden",2004]
]

for book in books:
    if isinstance(book,list):
        for item in book:
            print(item)
    else:
        print("--------------------------")
        print(book)
        print("--------------------------")
        