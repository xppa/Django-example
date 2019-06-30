from django.contrib import admin

# Register your models here.

from .models import Doctor, Client, Event

#Minimal registration of Models.
admin.site.register(Client)
admin.site.register(Doctor)
admin.site.register(Event)

#
# class BooksInline(admin.TabularInline):
#     """Defines format of inline book insertion (used in DoctorAdmin)"""
#     model = Client
#
#
# @admin.register(Doctor)
# class DoctorAdmin(admin.ModelAdmin):
#     """Administration object for Doctor models.
#     Defines:
#      - fields to be displayed in list view (list_display)
#      - orders fields in detail view (fields),
#        grouping the date fields horizontally
#      - adds inline addition of books in doctor view (inlines)
#     """
#     list_display = ('last_name',
#                     'first_name', 'date_of_birth', 'date_of_death')
#     fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
#     inlines = [BooksInline]
#
#
# class BooksInstanceInline(admin.TabularInline):
#     """Defines format of inline book instance insertion (used in BookAdmin)"""
#     model = Event
#
#
# class BookAdmin(admin.ModelAdmin):
#     """Administration object for Client models.
#     Defines:
#      - fields to be displayed in list view (list_display)
#      - adds inline addition of book instances in book view (inlines)
#     """
#     list_display = ('title', 'doctor', 'display_genre')
#     inlines = [BooksInstanceInline]
#
#
# admin.site.register(Client, BookAdmin)
#
#
# @admin.register(Event)
# class BookInstanceAdmin(admin.ModelAdmin):
#     """Administration object for Event models.
#     Defines:
#      - fields to be displayed in list view (list_display)
#      - filters that will be displayed in sidebar (list_filter)
#      - grouping of fields into sections (fieldsets)
#     """
#     list_display = ('book', 'status', 'borrower', 'due_back', 'id')
#     list_filter = ('status', 'due_back')
#
#     fieldsets = (
#         (None, {
#             'fields': ('book', 'imprint', 'id')
#         }),
#         ('Availability', {
#             'fields': ('status', 'due_back', 'borrower')
#         }),
#     )
