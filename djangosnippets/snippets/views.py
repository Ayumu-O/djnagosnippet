from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe
from django.http import HttpResponse, HttpResponseForbidden
from django.core.paginator import Paginator

from snippets.models import Snippet, Comment, Tag
from snippets.forms import SnippetForm, CommentForm

# Create your views here.

@require_safe
def top(request):
    snippets = Snippet.objects.\
        select_related('created_by').\
        prefetch_related('comments').\
        order_by('-created_at').all()
    paginator = Paginator(snippets, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'snippets/top.html', context)

@login_required
def snippet_new(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.created_by = request.user
            snippet.save()
            return redirect(snippet_detail, snippet_id=snippet.pk)
    else:
        form = SnippetForm()
    return render(request, 'snippets/snippet_new.html', {'form': form})

@login_required
def snippet_edit(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    checked_tags = snippet.tags.all()
    all_tags = Tag.objects.all()
    if snippet.created_by_id != request.user.id:
        return HttpResponseForbidden('このスニペットの編集は許可されていません')
    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            tag_ids = request.POST.getlist('tag[]')
            tags = Tag.objects.filter(id__in=tag_ids)
            snippet.tags.set(tags)
            snippet.save()
            return redirect('snippet_detail', snippet_id=snippet_id)
    else:
        form = SnippetForm(instance=snippet)
    context = {'form': form, 'already_checked': checked_tags, 'all_tags': all_tags}
    return render(request, 'snippets/snippet_edit.html', context)

@require_safe
@login_required
def snippet_delete(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    if snippet.created_by_id != request.user.id:
        return HttpResponseForbidden('このスニペットの削除は許可されていません')
    snippet.delete()
    return redirect('top')

@require_safe
def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet.objects.select_related('created_by'), pk=snippet_id)
    comments = snippet.comments.all().select_related('created_by')
    tags = snippet.tags.all()
    context = {
        'snippet': snippet,
        'tags': tags,
        'comments': comments,
        'comment_form': CommentForm()
    }
    return render(request, 'snippets/snippet_detail.html', context)

@login_required
def my_snippets(request):
    my_snippets = Snippet.objects.filter(created_by_id=request.user.id)
    return render(request, 'snippets/mypage.html', {'snippets': my_snippets})

@login_required
def comment_new(request, snippet_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.created_by = request.user
            comment.to = get_object_or_404(Snippet, pk=snippet_id)
            comment.save()
            return redirect('snippet_detail', snippet_id=snippet_id)
    else:
        form = CommentForm()
    return render(request, 'snippets/snippet_detail.html', {'comment_form': form})
