# ==========================================================
# else and finally
# ==========================================================
#
# THEORY:
#
# else:
#     Executes only when the try block succeeds without
#     an exception.
#
# finally:
#     Executes whether an exception occurs or not.
#
# This is useful for cleanup operations such as closing
# resources.
#
# ==========================================================


try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")

else:
    print("Valid number:", number)

finally:
    print("Execution completed.")