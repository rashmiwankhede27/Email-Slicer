email = input("Enter Your Email: ")
username = email[:email.index('@')]
domain_name  = email[email.index('@')+1:]
output="Your username is {} & domain is {}".format(username,domain_name)
print(output)
