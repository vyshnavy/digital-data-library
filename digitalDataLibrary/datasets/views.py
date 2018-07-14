from .models import data
from .forms import DataSearchForm
from search_views.search import SearchListView
from search_views.filters import BaseFilter

# search by tags
class DataFilter(BaseFilter):
    search_fields = {
        'search_text': ['tags', 'title'],
    }

# search list view model
class DataSearchList(SearchListView):
    model = data
    paginate_by = 30
    template_name = "datasets/data_list.html"
    form_class = DataSearchForm
    filter_class = DataFilter
    ordering = "-rating"
