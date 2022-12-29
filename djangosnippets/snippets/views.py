from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from snippets.models import Snippet

# Create your views here.

def top(request):
    snippets = Snippet.objects.all()
    context = {'snippets': snippets}
    return render(request, 'snippets/top.html', context)

def snippet_new(request):
    return HttpResponse('スニペットの登録')

def snippet_edit(request, snippet_id):
    return HttpResponse('スニペットの編集')

def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    context = {'snippet': snippet}
    return render(request, 'snippets/snippet_detail.html', context)
