from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from globerce_credit_application.credit_application.models import CreditApplication, CreditProgramm, Borrower, BlackList


@admin.register(CreditApplication)
class CreditApplicationAdmin(admin.ModelAdmin):
    pass

@admin.register(CreditProgramm)
class CreditProgrammAdmin(admin.ModelAdmin):
    pass

@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    pass

@admin.register(BlackList)
class BlackListAdmin(admin.ModelAdmin):
    pass