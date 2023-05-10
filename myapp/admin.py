from django.contrib import admin
from .models import Category,product,Relatedimage
# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display=('title','slug','category_image','is_active','is_featured')
    list_editable=('is_active','is_featured')
    list_filter=('is_active','is_featured')
    prepopulated_fields={'slug':('title',)}
admin.site.register(Category,categoryAdmin)

class RelatedimageAdmin(admin.StackedInline):
    model=Relatedimage
class productAdmin(admin.ModelAdmin):
    list_display=('title','slug','product_image','productStock','description','price','is_active','is_featured','category')
    list_editable=('is_active','is_featured')
    list_filter=('is_active','is_featured')
    prepopulated_fields={'slug':('title',)}
    inlines=[RelatedimageAdmin]
admin.site.register(product,productAdmin)    

