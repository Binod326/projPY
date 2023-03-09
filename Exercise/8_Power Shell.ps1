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




