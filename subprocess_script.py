import subprocess

# Run a command with arguments
command = 'ls -la'

output = subprocess.check_output(command, shell=True)

print(output)
