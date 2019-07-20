from django.contrib import admin

# Register your models here.
from blog.models import Gonderi, Yorum


@admin.register(Gonderi)
class GonderiAdmin(admin.ModelAdmin):
    list_display = ["baslik", "icerik_kisa", "olusturulma"]
    fields = ["baslik", "icerik", "olusturulma",]
    readonly_fields = ["icerik_kisa", "olusturulma"]
    list_filter = ["olusturulma"]

    def icerik_kisa(self, obj):
        return obj.icerik_kisa

    icerik_kisa.allow_tags = True
    icerik_kisa.short_description = "İçerik"

def make_published(modeladmin, request, queryset):
        queryset.update(onay=True)
        make_published.short_description = "Mark selected comments as published"

class YorumAdmin(admin.ModelAdmin):
    list_display = ["gonderi_baslik", "icerik_kisa", "olusturulma",'onay','güncelleme']
    #fields = ["gonderi", "icerik",'onay']
    #readonly_fields=['güncelleme']
    #readonly_fields = ["gonderi_baslik", "icerik_kisa", "olusturulma"]
    #list_filter = ["olusturulma"]
    actions=[
        make_published
    ]
    readonly_fields = ['güncelleme',]
    fieldsets = [
        ('Fieldset', {'fields': ["gonderi", "icerik","onay", "güncelleme"]}),
    ]
    
    




    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("gonderi")

    def gonderi_baslik(self, obj):
        return obj.gonderi.baslik

    gonderi_baslik.allow_tags = True
    gonderi_baslik.short_description = "Gönderi"

    def icerik_kisa(self, obj):
        return obj.icerik_kisa

    icerik_kisa.allow_tags = True
    icerik_kisa.short_description = "İçerik"


admin.site.register(Yorum,YorumAdmin)