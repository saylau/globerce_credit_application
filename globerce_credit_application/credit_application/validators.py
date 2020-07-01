from datetime import datetime
from requests import Request, Session

from globerce_credit_application.credit_application.models import CreditProgramm, BlackList
from globerce_credit_application.credit_application.exceptions import InvalidLoanAmount, InvalidBorrowerAge, BorrowerIsIndividualEnterpreneurError, BorrowerIsInBlacklistError

class CreditProgrammValidator():
    credit_programm: CreditProgramm = None

    def validate(self, iin, loan_amount):
        raw_date_of_birth = iin[:6]
        date_of_birth = datetime.strptime(raw_date_of_birth, '%y%m%d').date()

        today = datetime.today()
        borrower_age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))

        if self.credit_programm.minimum_borrower_age > borrower_age or self.credit_programm.maximum_borrower_age < borrower_age:
            rejection_cause = f'Borrower age must be between {self.credit_programm.minimum_borrower_age} and {self.credit_programm.maximum_borrower_age}'
            raise InvalidBorrowerAge(rejection_cause)

        if self.credit_programm.minimum_loan_amount > loan_amount or self.credit_programm.maximum_loan_amount < loan_amount:
            rejection_cause = f'Loan amount must be between {self.credit_programm.minimum_loan_amount} and {self.credit_programm.maximum_loan_amount}'
            raise InvalidLoanAmount(rejection_cause)

        return True

    def __init__(self, credit_programm_id):
        self.credit_programm = CreditProgramm.objects.get(id=credit_programm_id)



class BorrowerIndividualEnterpreneurValidator():

    def validate(self, iin):
        session = Session()

        request = Request(method='GET', url=f'https://stat.gov.kz/api/juridical/gov/?bin={iin}&lang=ru')
        prepared_request = session.prepare_request(request)
        response = session.send(request=prepared_request)

        print(response.json())


        if response.json()['success'] == True:
            raise BorrowerIsIndividualEnterpreneurError()

        return True

class BorrowerBlacklistValidator():

    def validate(self, iin):
        try:
            BlackList.objects.get(iin=iin)
        except BlackList.DoesNotExist:
            return True

        raise BorrowerIsInBlacklistError()
            
