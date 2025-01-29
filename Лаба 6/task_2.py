from pydantic import BaseModel
from typing import List

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book(BaseModel):
   id_: int
   name: str
   pages: int

   def __str__(self)->str:
       return f'Книга "{self.name}"'

   def __repr__(self)-> str:
       return f'Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'

# TODO написать класс Library
class Library(BaseModel):
    id: int =0
    books: List[Book] = []

    def get_next_book_id(self):
        if self.books:
            max_id = max(book.id_ for book in self.books)
        else:
            max_id = 0
        return max_id + 1

    def get_index_by_book_id(self, book_id_: int)-> int:
        for index, book in enumerate(self.books):
            if book.id_ == book_id_:
                return index
        raise ValueError((f"Книги с запрашиваемым id {book_id_} не существует"))




if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
