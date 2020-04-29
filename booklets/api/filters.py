
from rest_framework import filters

class Dynamic_BookLets_search_Filter(filters.SearchFilter):

    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])