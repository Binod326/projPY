$PSVersionTable
$PSVersionTable.PSVersion

# Get-Command is to list the all command available in the system
# -Noun and -Verb parameter is used to filter list.
Get-Command -Noun file*
Get-Command -Verb get -Noun file*

# to know more about what the command does and the various ways to call it.
# Typically, you invoke Get-Help by specifying it by name and adding the -Name flag that contains the name 
# of the cmdlet you want to learn about. Here's an example:
Get-Help -Name Get-Help
Update-Help     # To download and install Help files for the module that includes this cmdlet
Update-Help -Force  # Because a call to Update-Help downloads many help files, the command can fetch only once per day by default. You can override this fetching behavior by using the -Force flag.
Update-Help -UICulture en-US -Verbose   # update help files on Linux and macOS.
"""
Filter the help response
If you don't want to display the full help page, narrow the response by adding flags to your Get-Help command. 

Here are some flags you can use:
1. Full: Returns a detailed help page. It specifies information like parameters, inputs, and outputs that you don't get in the standard response.
2. Detailed: Returns a response that looks like the standard response, but it includes a section for parameters.
3. Examples: Returns only examples, if any exist.
4. Online: Opens a web page for your command.
5. Parameter: Requires a parameter name as an argument. It lists a specific parameter's properties.
"""
Get-Help Get-FileHash -Examples
Get-Help Get-FileHash -Online
Get-Help Get-FileHash -Full
Get-Help -Name Get-FileHash -Detailed

help Get-FileHash
help Get-FileHash -Examples

Compare-Object (Get-FileHash file1.txt) (Get-FileHash file2.txt) -Property Hash
Get-ExecutionPolicy # default value is Restricted
Get-ExecutionPolicy -List 
Set-ExecutionPolicy RemoteSigned # to allow the execution of local script or unlocked script.
Set-ExecutionPolicy Undefined # to restricted the execution of script.

# create a new folder named "MyFolder" at the root of the C drive. Then save a file named "myfile.txt" in that folder with the text "This is some text to save in the file."
New-Item -ItemType Directory -Path "C:\MyFolder" 
Set-Content -Path "C:\MyFolder\myfile.txt" -Value "This is some text to save in the file." 

## How to save content with multi-lines
# Set the file path and name
$FilePath = "C:\Users\ExampleUser\Documents\NewTextFile.txt"

# Create the text file
New-Item -ItemType File -Path $FilePath

# Add content to the file with a here-string
$Content = @"
This is an example of text in a PowerShell-generated file.
It includes multiple lines of text.
You can add as many lines as you need.
"@

Add-Content -Path $FilePath -Value $Content

## How to check if the file already exist in that location
# Set the file path and name
$myPath = "C:\Users\ExampleUser\Documents"
$myFileName = "ExistingTextFile.txt"
$FilePath = $myPath + "\" + $myFileName

# Check if the file already exists
if (Test-Path $FilePath) {
    # If the file exists, append new content to it
    Write-Output "File already exists in the Path."
    $Content = @"
This is additional text that will be added to the existing file.
"@
    Add-Content -Path $FilePath -Value $Content -NoClobber
} else {
    # If the file does not exist, create it and add initial content
    $Content = @"
This is the initial text that will be added to a new file.
"@
    New-Item -ItemType File -Path $FilePath
    Add-Content -Path $FilePath -Value $Content
    Write-Output "New file with given cotent also created in $myFilePath."
}

New-Item -Path .\IsReadOnlyTextFile.txt -ItemType File
Set-ItemProperty -Path .\IsReadOnlyTextFile.txt -Name IsReadOnly -Value $True
Get-ChildItem -Path .\IsReadOnlyTextFile.txt
Add-Content -Path .\IsReadOnlyTextFile.txt -Value 'Add value to read-only text file' -Force
Get-Content -Path .\IsReadOnlyTextFile.txt

Add-Content -Path .\IsReadOnlyTextFile.txt -Value 'Add new value to read-only text file' -Force
Get-Content -Path .\IsReadOnlyTextFile.txt

