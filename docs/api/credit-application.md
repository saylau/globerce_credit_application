# Credit Application
Supports registering, viewing, and updating user accounts.

## Create a new credit application

**Request**:

`POST` `/credit-application/create/`

Body:

Name                | Type   | Required | Description
--------------------|--------|----------|------------
iin                 | string | Yes      | IIN of a borrower.
credit_programm_id  | int    | Yes      | Credit programm ID
loan_amount         | int    | Yes      | Loan amount

**Response**:

```json
Content-Type application/json
201 Created

{
    "status": "approved",
    "rejection_cause": null,
    "id": 8
}
```


## Get a credit programms list

**Request**:

`GET` `/credit-application/programms/`

**Response**:

```json
Content-Type application/json
200 OK

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "minimum_loan_amount": 100000,
            "maximum_loan_amount": 1000000,
            "minimum_borrower_age": 18,
            "maximum_borrower_age": 50
        }
    ]
}
```


## Get credit application by id

**Request**:

`GET` `/credit-application/:id/`

**Response**:

```json
Content-Type application/json
200 OK

{
    "status": "approved",
    "rejection_cause": null,
    "id": 8
}
```
