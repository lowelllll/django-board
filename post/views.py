from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .forms import PostForm, CommentForm
from .models import BoardTbl, CommentTbl

def index(request):
    posts = BoardTbl.objects.raw( # ORM 미사용
        'SELECT b.idx, u.last_name, u.first_name, b.subject, b.content, b.date '
        'FROM board_tbl b '
        'JOIN auth_user u '
        'ON b.writer = u.id'
    )
    count = len(list(posts));
    return render(request, 'post/index.html', {'posts':posts, 'count':count})


def post_detail(request,id):
    post = BoardTbl.objects.raw(
        'SELECT b.idx, u.last_name, u.first_name, b.subject, b.content, b.date '
        'FROM board_tbl b '
        'JOIN auth_user u '
        'ON b.writer = u.id '
        'WHERE idx = %s'
        ,[id])[0]

    comments = CommentTbl.objects.raw(
        'SELECT c.idx, u.last_name, u.first_name, c.content, c.date '
        'FROM comment_tbl c '
        'JOIN auth_user u '
        'ON c.writer = u.id '
        'WHERE bidx = %s'
        ,[id])

    form  = CommentForm()
    return render(request, 'post/detail.html', {'post':post, 'comments':comments, 'form':form})


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid(): # ORM 사용
            post = form.save(commit=False)
            post.writer = request.user.id
            post.date = timezone.localtime()
            post.save()
            messages.success(request, '게시글이 작성되었습니다.')
            return redirect('post:index')
    else:
        form = PostForm()
    return render(request, 'post/form.html', {'form':form})


@login_required
def post_edit(request, id):
    post = get_object_or_404(BoardTbl, idx=id)
    if post.writer != request.user.id:
        messages.error(request, '게시물 수정은 해당 작성자만 가능합니다.')
    else:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save() # 작성자와 게시글과 작성일은 그대로 나둠
                messages.success(request, '게시글이 수정되었습니다.')
        else:
            form = PostForm(instance=post)
            return render(request, 'post/form.html', {'form':form})
    return redirect('post:index')


@login_required
def post_delete(request):
    if request.method == 'POST':
        idx = request.POST['idx']
        post = get_object_or_404(BoardTbl, idx=idx)
        if post.writer != request.user.id:
            messages.error(request, '게시물 삭제은 해당 작성자만 가능합니다.')
        else:
            comments = CommentTbl.objects.filter(bidx=idx)
            post.delete()
            comments.delete() # CASCADE
            messages.success(request, '게시물이 삭제되었습니다.')
    return redirect('post:index')


@login_required
def comment_new(request, bidx):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.writer = request.user.id
            comment.date = timezone.localtime()
            comment.bidx = bidx
            comment.save()
            messages.success(request, '댓글이 작성되었습니다.')
        else:
            messages.error(request, '댓글 작성에 실패했습니다.')
    return redirect('post:post_detail',id=bidx)


@login_required
def comment_delete(request):
    if request.method == 'POST':
        idx = request.POST['idx']
        bidx = request.POST['bidx']
        comment = get_object_or_404(CommentTbl, idx=idx)
        if comment.writer != request.user.id:
            messages.error(request, '댓글 삭제은 해당 작성자만 가능합니다.')
        else:
            comment.delete()
            messages.success(request, '댓글이 삭제되었습니다.')
    return redirect('post:post_detail', id=bidx)

