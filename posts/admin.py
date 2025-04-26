from django.contrib import admin
from.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'created_on')  # Fields to display in the admin list view
    search_fields = ('title', 'subtitle')  # Fields to search in the admin panel
    
admin.site.register(Post, PostAdmin) # Post

