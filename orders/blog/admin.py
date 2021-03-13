from django.contrib import admin
from .models import Post

#admin.site.register(Post)


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('title', 'status')
    search_fields = ('author',)