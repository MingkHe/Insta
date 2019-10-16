from django.contrib import admin
from Insta.models import Post, InstaUser, Like,Comment, UserConnection

# Register your models here.
admin.site.register(Post)
admin.site.register(InstaUser)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(UserConnection)
