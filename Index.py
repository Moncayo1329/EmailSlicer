def main():
    print("welcome to the  email slicer") 
    print("")

    email_input = input("input your email adress")

    (username , domain) = email_input.split("@")
    (domain, extension) = domain.split(".") 

    print("Username: ", username)
    print("Domain: ", domain )
    print("extension:", extension)

main()