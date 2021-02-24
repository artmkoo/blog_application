from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register (Post)

class PostAdmin (admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status') # dodaje naglowki dla posta
    list_filter = ('status', 'created', 'publish', 'author') # wstawia panel filtrowanie po prawej stronie
    search_fields = ('title', 'body') # dodaje pole wyszukiwania
    prepopulated_fields = {'slug': ('title',)} # uzupelnia automatycznie slug na podstawie tego co jest wpisane w title
    raw_id_fields = ('author',) # przy dodawaniu posta przy polu author jest teraz dostepna lupka zamiast listy rozwijanej - w przypadku duzej ilosci userow mozna ich filtrowac
    date_hierarchy = 'publish' # pasek nawigacyjny pod wyszukiwaniem, nawigowanie po datach
    ordering = ('status', 'publish') # ustawia domyslne sortowanie po polu status i publish

