import subprocess

def execute_command(user_input):
    """Execute system command"""
    command = f"ls {user_input}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout
