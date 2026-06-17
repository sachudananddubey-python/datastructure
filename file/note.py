try:
    num = int(input("Enter number: "))
    result = 10 / num

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

except FileNotFoundError:
    print("File not found")

except FileExistsError:
    print("File already exists")

except TypeError:
    print("Type mismatch")

except IndexError:
    print("Index out of range")

except KeyError:
    print("Key not found")

except Exception as e:
    print("Some error occurred:", e)