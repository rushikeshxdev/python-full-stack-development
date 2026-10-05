# # Week1 : Task1 - Python Basics

# # 1. Variables:

# name = "Rushikesh"
# age = 23
# height = 6.1
# is_developer = True

# print("Name: ", name)
# print("Age: ", age)
# print("Height: ", height)
# print("Developer: ", is_developer)


# # 2. DataTypes:

# integer_value = 10
# float_value = 10.5
# string_value = "Python"
# boolean_value = True

# print(type(integer_value))
# print(type(float_value))
# print(type(string_value))
# print(type(boolean_value))


# # 3. Operators:

# a = 20
# b = 5

# print("Addition: ", a+b)
# print("Substraction: ", a-b)
# print("Multiplication: ", a*b)
# print("Division: ", a/b)
# print("Modulus: ", a%b)


# # 4. Input

# user_name = input("Enter your name: ")
# print("Hello,", user_name)


# # 5. Conditions

# marks = 75

# if marks >= 40:
#     print("Pass")
# else:
#     print("Fail")


# # 6. Loops

# for number in range(1, 6):
#     print("Number: ", number)

# count = 1

# while count <= 5:
#     print("Count:", count)
#     count += 1


#Check the mutability and immutabbility by an example
#String - Immutable:
# s = "hello"
# print(id(s))

# s= s+ " world"
# print(id(s))

# #List - Mutable
# lst = [1, 2]
# print(id(lst))

# lst.append(3)
# print(id(lst))


# original = ["task1", "task2"]

# alias = original
# clone = original.copy()

# alias.append("task3")
# print(original)
# print(alias)
# print(clone)

# def format_task(task_id: int, title: str, is_done: bool) -> str:
#     if is_done:
#         status = "[X]"
#     else:
#         status = "[ ]"

#     return f"{status} #{task_id} - {title}"

# #Let's test it:
# print(format_task(task_id=1, title="Complete assignment", is_done=False))
# print(format_task(task_id=2, title="Complete assignment", is_done=True))

# tasks = ["Learn Python", "Setup DB", "Write Tests", "Deploy"]
# search_query = "Setup DB"

# for index, task in enumerate(tasks, start=1):
#     if task == search_query:
#         print(f"Found {task} at position {index}!")
#         break


# def create_task(title, *tags, **metadata):
#     print("Title:", title)
#     print("Tags: ", tags)
#     print("Metadata: ", metadata)

# create_task("Learn Python", "Programming", "Educational", priority="High", deadline="2023-12-31")

# def build_task(task_id: int, title: str, status: str = "pending", **details) -> dict:
#     task = {
#         "id": task_id,
#         "title": title,
#         "status": status
#     }
    
#     task.update(details)
#     return task

# task1 = build_task(101, "Setup Database", priority="Urgent", assigned_to="Rushikesh")
# print(task1)
# task2 = build_task(102, "write test", status="complete", priority="Low")
# print(task2)

incoming_payload = {
    "title": "Build Authentication",
    "tags": ["security", "backend", "auth", "backend", "security"],
    "created_by": "rushikesh"
    # Note: "priority" is NOT provided!
}

def process_incoming_payload(payload):
    united_tags = set(payload.get("tags", []))
    tags = list(united_tags)

    task_priority = payload.get("priority", "medium")   
    
    admins = {"admin", "lead"}
    if payload.get("created_by") in admins:
        print(f"Task created by Authorized Admin: {payload['created_by']}")
    else:
        print(f"Task created by Unauthorized User: {payload['created_by']}")

    print("Tags:", tags)
    print("Priority:", task_priority)

process_incoming_payload(incoming_payload)