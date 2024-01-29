# Install Python
Invoke-WebRequest -UseBasicParsing -Uri 'https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe' -OutFile 'C:/python-3.11.0-amd64.exe'
cd C:\
.\python-3.11.0-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

# Add Python directory to the PATH environment variable
$pythonPath = "C:\Program Files\Python311"
$env:PATH += ";$pythonPath"

# Authentication

# Set COMPANY environment variable
[Environment]::SetEnvironmentVariable("COMPANY", "Tek Experts 1", [System.EnvironmentVariableTarget]::Machine)

# Set USERNAMEMONET environment variable
[Environment]::SetEnvironmentVariable("USERNAMEMONET", "YourUsername", [System.EnvironmentVariableTarget]::Machine)

# Set PASSWORD environment variable
[Environment]::SetEnvironmentVariable("PASSWORD", "YourPassword", [System.EnvironmentVariableTarget]::Machine)


Exit
_______________________________________________________________

# RESTART POWERSHELL, BEFORE INSTALLING SELENIUM

# Install Selenium using pip
pip3 install selenium

