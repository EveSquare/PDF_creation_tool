@echo off
 
if not "%~0"=="%~dp0.\%~nx0" (
     start /min cmd /c,"%~dp0.\%~nx0" %*
     exit
)

python G:\GoogleDrive\Python\pdf_creater\create_pdf.py %*