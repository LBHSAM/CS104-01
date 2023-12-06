names = []

for i in range(10):
    acceptedName = input("Enter a name: ")
    names.append(acceptedName)

print("Queue after input:")
print(names)

print("\nDequeuing names:")
for i in range(len(names)):
    print(names.pop(0))

print("\nQueue after dequeuing:")
print(names)