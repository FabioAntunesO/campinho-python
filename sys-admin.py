#import os
import subprocess

#os.system("ls")

#uso do subprocess.run com três argumentos
subprocess.run(["ls","-l","README.md"])

#recuperação de informações do sistema
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

#recuperação de informações sobre o espaço em disco
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])