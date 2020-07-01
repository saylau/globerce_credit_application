from django.db import models
from django.core.validators import RegexValidator

CREDIT_STATUS_CHOICES=(
    ("rejected", "rejected"),
    ("approved", "approved")
)

class CreditProgrammManager(models.Manager):
    pass

class CreditProgramm(models.Model):
    minimum_loan_amount = models.PositiveIntegerField()
    maximum_loan_amount = models.PositiveIntegerField()
    minimum_borrower_age = models.PositiveIntegerField()
    maximum_borrower_age = models.PositiveIntegerField()

    objects = CreditProgrammManager()


class BorrowerManager(models.Manager):
    pass

class Borrower(models.Model):
    iin = models.CharField(validators=[RegexValidator(regex=r'^[\d]{12}$', message='IIN has to be 12 digits', code='nomatch')], primary_key=True, max_length=12)
    date_of_birth = models.DateField()

    objects = BorrowerManager()

class CreditApplicationManager(models.Manager):
    pass

class CreditApplication(models.Model):
    borrower = models.ForeignKey("credit_application.Borrower",related_name="credit_applications", on_delete=models.DO_NOTHING)
    credit_programm = models.ForeignKey("credit_application.CreditProgramm", related_name="credit_applications", on_delete=models.DO_NOTHING)
    loan_amount = models.PositiveIntegerField()
    status = models.CharField(choices=CREDIT_STATUS_CHOICES, max_length=30)
    rejection_cause = models.CharField(blank=True, null=True, max_length=256)

    objects = CreditApplicationManager()
    
    class Meta:
        unique_together = ('borrower', 'credit_programm', 'loan_amount',)

class BlackListManager(models.Manager):
    pass

class BlackList(models.Model):
    iin = models.CharField(validators=[RegexValidator(regex=r'^[\d]{12}$', message='IIN has to be 12 digits', code='nomatch')], primary_key=True, max_length=12)

    objects = BlackListManager()