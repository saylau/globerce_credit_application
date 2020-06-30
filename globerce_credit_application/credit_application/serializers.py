from datetime import datetime
from django.http import Http404
from rest_framework import serializers
from django.core.validators import RegexValidator

from globerce_credit_application.credit_application.models import CreditApplication, Borrower
from globerce_credit_application.credit_application.validators import  CreditProgrammValidator, BorrowerIndividualEnterpreneurValidator, BorrowerBlacklistValidator

class CreditApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CreditApplication
        fields = "__all__"

class CreateCreditApplicationSerializer(serializers.Serializer):
    iin = serializers.CharField(validators=[RegexValidator(regex=r'^[\d]{12}$', message='IIN has to be 12 digits', code='nomatch')], write_only=True)
    credit_programm_id = serializers.IntegerField(write_only=True)
    loan_amount = serializers.IntegerField(write_only=True)

    status = serializers.CharField(read_only=True)
    rejection_cause = serializers.CharField(read_only=True)

    def create(self, validated_data):
        iin = str(validated_data['iin'])
        credit_programm_id = int(validated_data['credit_programm_id'])
        loan_amount = int(validated_data['loan_amount'])

        raw_date_of_birth = iin[:6]
        date_of_birth = datetime.strptime(raw_date_of_birth, '%y%m%d').date()
        borrower, _created = Borrower.objects.get_or_create(iin=iin, date_of_birth=date_of_birth)

        credit_programm_validator = CreditProgrammValidator(credit_programm_id)
        borrower_individual_enterpreneur_validater = BorrowerIndividualEnterpreneurValidator()
        borrower_blacklist_validator = BorrowerBlacklistValidator()

        credit_programm_validator.validate(iin, loan_amount)
        borrower_individual_enterpreneur_validater.validate(iin)
        borrower_blacklist_validator.validate(iin)

        credit_application = CreditApplication.objects.create(
            borrower=borrower,
            credit_programm=credit_programm_validator.credit_programm,
            loan_amount=loan_amount,
            status='approved',
        )
        return credit_application

    class Meta:
        fields = ('iin', 'credit_programm_id', 'loan_amount',)
