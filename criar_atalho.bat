@echo off
echo Criando atalho na area de trabalho...
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\Desktop\Dinheiro Smart.lnk'); $Shortcut.TargetPath = '%CD%\run.bat'; $Shortcut.WorkingDirectory = '%CD%'; $Shortcut.IconLocation = 'shell32.dll,21'; $Shortcut.Save()"
echo Atalho criado com sucesso!
pause