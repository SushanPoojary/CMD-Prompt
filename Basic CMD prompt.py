from sys import argv

script, user_name = argv
prompt = '> ' #basic prompt
#prompt = f'{script} {user_name}> ' #Typical cmd line type prompt (eg dir shown is windows)

print(f"Hi {user_name}, I'm {script} script.")
print(f"Do you like {user_name}?.")
like = input(prompt)

print(f"Where do you live {user_name}?")
loc = input(prompt)

print(f"""
This is {script}.
Usrname is {user_name}
and {user_name} lives in {loc}.""")