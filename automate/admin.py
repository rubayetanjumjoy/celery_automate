from django.contrib import admin
from .models import Product
from django.urls import path
from django.shortcuts import render, redirect

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_at', 'updated_at')
    actions = ['set_category_to_books']

    # def do_migration(self, request):
    #     step_1_disabled = True
    #     step_2_disabled = True
        
    #     # Get all products queryset
    #     queryset = self.model.objects.all()
        
    #     # Update all products' category to "Books"
    #     queryset.update(category='books')
        
    #     context = dict(
    #         self.admin_site.each_context(request),
    #         model="Migration Data",
    #         url="migrationdata",
    #         step="RUNNING...",
    #         items="migrate_data",
    #         step_1_disabled=step_1_disabled,
    #         step_2_disabled=step_2_disabled,
    #     )
    #     # Redirect back to the change list page
    #     return render(request, "admin/migrate.html", context)
    
    # def set_category_to_books(self, request, queryset):
    #     # Call do_migration() method
    #     return self.do_migration(request)
    
    # do_migration.short_description = "Migrate"

    # def get_urls(self):
    #     urls = super().get_urls()
    #     new_urls = [
    #         path('migration/', self.do_migration),
    #     ]
    #     return new_urls + urls

admin.site.register(Product, ProductAdmin)