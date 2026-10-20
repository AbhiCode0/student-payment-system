def process_payment(student_name, course_fee, paid_amount):

    def validate_payment():
        if paid_amount <= 0:
               return False
        if paid_amount > course_fee:
               return False
        return True

    def calculate_balance():
         return course_fee - paid_amount

    def generate_receipt(balance):
       print("Payment Receipt")
       print("---------------")
       print("Student Name:", student_name)
       print("Course Fee:", course_fee)
       print("Paid_Amount:", paid_amount)
       print("Balance:", balance)
            
              
    if validate_payment():
        balance = calculate_balance()
        generate_receipt(balance)
    else:
        print("Invalid Payment")

process_payment(student_name="Abhishek", course_fee=12000, paid_amount=12000)

