from django.urls import path, include
from django.conf import settings

from snippets.views import *

urlpatterns = [
    path('new/', snippet_new, name='snippet_new'),
    path('<int:snippet_id>/', snippet_detail, name='snippet_detail'),
    path('<int:snippet_id>/edit/', snippet_edit, name='snippet_edit'),
    path('<int:snippet_id>/delete/', snippet_delete, name='snippet_delete'),
    path('<int:snippet_id>/comments/new/', comment_new, name='comment_new'),
    path('tag/<str:tag_name>', snippet_filter_by_tag, name='filter_by_tag'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path('__debuf__/', include(debug_toolbar.urls)))
