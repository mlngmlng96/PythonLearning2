command = ""
started = False
while True:
    command = input ("> ").lower()
    if command == "start":
        if started:
            print("car already started")
        else:
            print("car started,ready to go")
            started = True

    elif command == "stop":
        if not started:
            print("car is already stopped.")
        else:
            started = False
            print("car is stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("sorry, I don't understand that")
