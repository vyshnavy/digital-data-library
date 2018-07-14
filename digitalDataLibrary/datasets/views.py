from .models import data
from .forms import DataSearchForm
from search_views.search import SearchListView
from search_views.filters import BaseFilter
import digitalDataLibrary.settings as settings
import urllib.parse
import os
import mimetypes
from django.http import HttpResponse

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
    ordering = ["click_count", "-rating"]


def respond_as_attachment(request):
    did = request.GET.get('did')
    data1 = data.objects.get(username=did)
    data1.click_count = data1.click_count + 1
    data1.save()
    fp = open(data1.path, 'rb')
    response = HttpResponse(fp.read())
    fp.close()
    type_of_file, encoding = mimetypes.guess_type(data1.file_name)
    if type_of_file is None:
        type_of_file = 'application/octet-stream'
    response['Content-Type'] = type_of_file
    response['Content-Length'] = str(os.stat(data1.path).st_size)
    if encoding is not None:
        response['Content-Encoding'] = encoding
    if u'WebKit' in request.META['HTTP_USER_AGENT']:
        # Safari 3.0 and Chrome 2.0 accepts UTF-8 encoded string directly.
        filename_header = 'filename=%s' % data1.file_name.encode('utf-8')
    elif u'MSIE' in request.META['HTTP_USER_AGENT']:
        # IE does not support internationalized filename at all.
        # It can only recognize internationalized URL, so we do the trick via routing rules.
        filename_header = ''
    else:
        # For others like Firefox, we follow RFC2231 (encoding extension in HTTP headers).
        filename_header = 'filename*=UTF-8\'\'%s' % urllib.parse.quote(data1.file_name.encode('utf-8'))
    response['Content-Disposition'] = 'attachment; ' + filename_header
    return response
