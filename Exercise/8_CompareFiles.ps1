# 1st: Copy this PowerShell code file into the folder where two files needs to be compared.
# 2nd: Change the file names and path below in the varialbes: $File1, $File2 and $Path
# 3rd: Save this script file and above changes.
# 4th: Open PowerShell from Start Menu. 
# 5ht: Then type following commands:
    # cd <your current folder>
    # ./CompareFiles.ps1
        # RESULTS:
        # If the files are not exactly identical, a message with hash value of files will be displayed. 
        # Otherwise they are identical.

$File1 = "Book4.xlsx"
$File2 = "02 PO draft 8Mar23 - Hotel Lhasa.xlsx"
$Path = "C:\Users\Bijeta\Downloads\Compare_files"

$FilePath1 = $Path + "\" + $File1
$FilePath2 = $Path + "\" + $File2
Compare-Object (Get-FileHash $FilePath1) (Get-FileHash $FilePath2) -Property Hash