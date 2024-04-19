def start_task(a):
    print(f"\ntask{a}-->\n")


def end_task(b):
    print(f"\n<--task{b}\n")


start_task(1)

print(input("Please enter your name: "), input("Please enter your age: "), input("Please enter your phone number: "))
end_task(1)

start_task(2)
print("""
           .“““.              
          :_____:
          |     | 
          |     |           
          |     |           
          |     |           
         /|     |\ 
       /__|_____|__\ 
         /\     /\ 
        /  \   /  \  
        ““““   ““““              
""")
end_task(2)
