def start_task(a):
    print(f"\ntask{a}-->\n")


def end_task(b):
    print(f"\n<--task{b}\n")


start_task(1)
while True:
    try:
        name = input("Please enter your name: ")
        age = int(input("Please enter your age: "))
        number = int(input("Please enter your phone number: "))
        print(name, age, number)
        break
    except ValueError:
        print("Please enter an integer")

end_task(1)

start_task(2)

print("""
           .“““.              
          :_____:
          |     | 
          |     |           
          |  МЕ |           
          |     |           
         /|     |\ 
       /__|_____|__\ 
         /\     /\ 
        /  \   /  \  
        ““““   ““““              
""")

end_task(2)

start_task(3)
print("Ruby\n"
      "Swift\n"
      "Kotlin\n"
      "Rust\n"
      "Go\n"
      "TypeScript\n"
      "Scala\n"
      "Lua\n"
      "Dart\n"
      "Julia\n")
end_task(3)
