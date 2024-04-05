class leave_application:
    def __init__(self, employee_name,start_date,end_date,reason):
        self.employee_name =employee_name
        self.start_date=start_date
        self.end_date=end_date
        self.reason=reason
        self.status=""
    def approve(self):
        self.status="accepted"
        print(self.status)
    def reject(self):
       self.status="rejected"
       print(self.rejected)
    def display(self):
       print("employ name:",self.employee_name) 
       print("start date:",self.start_date)
       print("end date:",self.end_date)
       print("reason:",self.reason )
       print("status:",self.status) 

a1=leave_application ("MR NUMAN","2024-04-05","05-05-2024","i am ill")
a1.display()
a1.approve()