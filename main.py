from functions import get_todos, write_todos

while True:
    user_action = input("Type add, show, edit, complete or off: ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo, '\n')
    elif user_action.startswith("show"):
        todos = get_todos()
        for i, j in enumerate(todos):
            j = j.strip('\n')
            print(f"{i+1}-{j}")
    elif user_action.startswith( "edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1
            todos = get_todos()

            new_todo = input("Enter new todo: ")

            todos[number] = new_todo + '\n'
            write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            index = number - 1
            todos = get_todos()

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            write_todos(todos)
        except IndexError:
            print("Your command is not valid")
    elif user_action.startswith("off"):
        break
    else:
        print("Command is not valid.")

print("Bye")
