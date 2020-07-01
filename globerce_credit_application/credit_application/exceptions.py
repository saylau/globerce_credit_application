from rest_framework.exceptions import ValidationError

class InvalidLoanAmount(ValidationError):
    default_detail = 'Invalid loan amount'
    default_code = 'invalid_loan_amount'

class InvalidBorrowerAge(ValidationError):
    default_detail = 'Invalid borrower age'
    default_code = 'invalid_borrower_age'

class BorrowerIsIndividualEnterpreneurError(ValidationError):
    default_detail = 'Borrower is individual enterpreneur'
    default_code = 'borrower_is_individual_enterpreneur'

class BorrowerIsInBlacklistError(ValidationError):
    default_detail = 'Borrower is in blacklist'
    default_code = 'borrower_is_in_blacklist'