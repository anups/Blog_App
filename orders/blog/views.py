from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


from .models import Post, Comment

from .forms import EmailPostForm, CommentForm


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


# def post_list(request):
#     # To fetch all the records form posts tables
#     all_posts = Post.objects.all()
#     paginator = Paginator(all_posts, 3)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#
#     # Need to render all_posts to template "blog/post/list.html" with request of all_posts
#     return render(request,
#                   'blog/post/list.html',
#                   {'page': page,
#                    'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='publish',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # THIS WILL CREATE THE NEW_COMMENT AS AN OBJECT BUT NEW_COMMENT WILL NOT SVAED IN TABLE
            new_comment = comment_form.save(commit=False)
            # THIS WILL CREATE THE NEW_COMMENT AS AN OBJECT BUT NEW_COMMENT WILL BE SVAED IN TABLE
            # new_comment = comment_form.save()
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'blog/post/detail.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='publish')

    if request.method == 'POST':
        # Creation of form object
        form = EmailPostForm(request.POST)
        # Form validation check
        if form.is_valid():
            cd = form.cleaned_data  # for form save with validation
            print("FORM is saving.................")

    else:
        form = EmailPostForm()
    return render(request,
                  'blog/post/share.html',
                  {'post': post,
                   'form': form})

    # Cross Site Resource Forgery for HTTP POST