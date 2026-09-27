# -------------------------------------
#             Scope
# -------------------------------------

count = 10  #Global Variable


def change_count():
    count = 20   #Local Variable
    print("Inside:", count)


change_count()

print("Outside:", count)