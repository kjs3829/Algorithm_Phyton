file_name = input("Enter file name to exec : ")
file_name += ".py"
exec(open(file_name).read())
