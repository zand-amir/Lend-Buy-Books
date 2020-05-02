from django.contrib import admin
from .models import Books,Proposed_Book,Borrow_book,Wishlist

admin.site.register(Books)
admin.site.register(Proposed_Book)
admin.site.register(Borrow_book)
admin.site.register(Wishlist)
