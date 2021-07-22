##Se comentan las lineas para ingresar los modelo propios 20210721
##from django.contrib import admin

# Register your models here.

#Se agregan las lineas para la administración de blog 20210721
from django.contrib import admin
from .models import Post

admin.site.register(Post)
