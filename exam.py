total_classes = int(input("Enter total number of classes: "))
attended_classes = int(input("Enter number of classes attended: "))

attendance = (attended_classes / total_classes) * 100

if attendance >= 75:
    print("Eligible for exam.")
else:
    print("Not eligible for exam.")