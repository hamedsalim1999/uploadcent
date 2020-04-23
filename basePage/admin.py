from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_at'
    actions_on_bottom = True
    actions_selection_counter = True
    fieldsets = (
        (None, {
            'fields':(
                
            ('tittle',),
            ('image', 'width_field','height_field',),
            ('main_text',),
            ('main_file',),
           
           
            )

        }),

    )

