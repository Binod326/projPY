# Set the path and file name.
$myPath = "C:\MyFolder"
$myFileName = "myfile.ps1"
$myFilePath = $myPath + "\" + $myFileName

$Content = @"
# Set the path and file name.
$myPath = "C:\MyFolder"
$myFileName = "myfile.ps1"
$myFilePath = $myPath + "\" + $myFileName
if (Test-Path $myPath) {
	echo "MyFolder already exist."
	if (Test-Path $myFilePath) {		
		$Content = "# Next powershell code executed on " + (Get-Date) + "."
		Add-Content -Path $myFilePath -Value $Content
		echo "Additional content is also added to existing file $myFilePath"	
	} else {
		$Content = "This is a file created by powerShell script on " + (Get-Date)
		Set-Content -Path $myFilePath -Value $Content
		echo "New Folder '$myPath' created."
		echo "New file with given cotent also created in $myFilePath"
	}
} else {
	New-Item -ItemType Directory -Path "C:\MyFolder"
	$Content = "This is a file created by powerShell script on " + (Get-Date)
	Set-Content -Path $myFilePath -Value $Content
	echo "New Folder '$myPath' created."
	echo "New file with given cotent also created in $myFilePath"
}
"@


if (Test-Path $myPath) {
	echo "MyFolder already exist."
	if (Test-Path $myFilePath) {		
		$Content = "# The next powershell code was executed on " + (Get-Date) + "."
		Add-Content -Path $myFilePath -Value $Content
		echo "Additional content is also added to existing file $myFilePath"	
	} else {
		Set-Content -Path $myFilePath -Value $Content
		echo "New Folder '$myPath' created."
		echo "New file with given cotent also created in $myFilePath"
	}

} else {
	New-Item -ItemType Directory -Path "C:\MyFolder"	
	Set-Content -Path $myFilePath -Value $Content
	echo "New Folder '$myPath' created."
	echo "New file with given cotent also created in $myFilePath"
}