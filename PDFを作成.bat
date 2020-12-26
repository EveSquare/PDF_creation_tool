@echo off
 
if not "%~0"=="%~dp0.\%~nx0" (
     start /min cmd /c,"%~dp0.\%~nx0" %*
     exit
)

python G:\Python\PDF_creation_tool\create_pdf.py(ここはcreate_pdf.pyの絶対パス) %*
