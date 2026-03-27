class UserExsistingError(Exception):
    pass
class UserPasswordStrengthError(Exception):
    pass
class User:
    user_name=set()
    def __init__(self,username,password,email,number):
        self.u_userName=username
        self.u_password=password
        self.u_email=email
        self.u_number=number
        self.addUser()
        self.passwordValidate()
        print("Account created...")
    def addUser(self):
        if self.u_userName in User.self_user_Name:
            raise UserExsistingError("user already exsist..try with different username")
        else:
            User.user_name.add(self.u_userName)
    def passwordValidate(self):
        uc=lc=num=sc=0
        for i in self.u_password:
            if i.isupper():
                uc=uc+1
            elif i.islower():
                lc=lc+1
            elif i.isdigit():
                num=num+1
            else:
                sc=sc+1
        if len(self.u_password)<8 or uc==0 or lc==0 or num==0 or sc==0:
            raise UserPasswordStrengthError("Your password is not strong")
def main():     
    try:         
        userName=input("Enter your username:")
        password=input("Enter your password:")
        email=input("Enter your email:")
        number=input("Enter your mobile number:")
        u=User(userName,password,email,number)
    except UserPasswordStrengthError as e:
        print(e)
    except UserExsistingError as e:
        print(e)
    except Exception as e:
        print("Something wrong...")
main()
main()