from django.urls import path
from .views import BorrowBook
from .views import BorrowedHistoryView, ReturnBook
urlpatterns = [
    path('book/<int:id>', BorrowBook, name= 'Borrow'),
    path('history/', BorrowedHistoryView.as_view(), name= 'borrowed_history'),
    path('book/return/<int:id>', ReturnBook, name= 'return_book')
]
