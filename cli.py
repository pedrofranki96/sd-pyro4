from rich import print
from rich.prompt import Prompt

command = Prompt.ask("Enter your command", choices=["pedro", "exit"], default="Paul")

print(f"Hello, {command}!")

while True:

  if(command == 'exit'):
    break

