from django.contrib import admin
from .models import Post

# Register your models here.

# admin.site.register(Post)
# we tell to django that model is register by using castom class inherit from ModelAdmin
#it allows to manipulate how to dispal the model and interact with it
#it show syou this filter on the side of admin panel
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields= {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy= 'publish'
    ordering = ['status', 'publish']