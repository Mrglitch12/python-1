def check_loan_eligibility(age, income, credit_score, has_criminal_record):
    if age < 18:
        print("Rejected: Age below 18")
    elif income < 50000:
        print("Rejected: Income below 50,000")
    elif credit_score < 600:
        print("Rejected: Credit score below 600")
    elif has_criminal_record:
        print("Rejected: Criminal record found")
    else:
        print("Approved: Loan Approved")

age = int(input("Enter age: "))
income = int(input("Enter income: "))
credit_score = int(input("Enter credit score: "))
has_criminal_record = input("Criminal record? (yes/no): ").strip().lower() == "yes"

check_loan_eligibility(age, income, credit_score, has_criminal_record)