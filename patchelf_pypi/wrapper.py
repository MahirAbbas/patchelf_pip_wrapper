import subprocess



def run_patchelf(arguments):
    command = ['patchelf'] + arguments
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout, result.stderr


try:
    stdout, stderr = run_patchelf(['--version'])
    if stderr:
        print(f"Error: {stderr}")
    else:
        print(f"Output: {stdout}")
except FileNotFoundError:
    print("patchelf is not installed or not found in PATH.")

