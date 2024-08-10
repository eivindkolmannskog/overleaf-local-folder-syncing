import subprocess


def run_powershell_command(command) -> bool:
    try:
        # Run PowerShell command and capture output
        result = subprocess.run(
            ["powershell", "-Command", command],
            capture_output=True,
            text=True,
            check=True,
        )
        # Print the output
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        # If the command fails, print the error
        print("Error:", e)
        return False


def run_wisdem_gui() -> bool:
    return run_powershell_command("wisdem")
