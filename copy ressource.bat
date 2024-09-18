@echo off

:: Définir le dossier source et le dossier de destination
set "SOURCE_ASSETS=assets"
set "SOURCE_MODS=mods"
set "DEST_DIST=dist\Re-world"

:: Créer le dossier dist s'il n'existe pas
if not exist "%DEST_DIST%" (
    mkdir "%DEST_DIST%"
)

:: Copier le dossier assets dans dist
if exist "%SOURCE_ASSETS%" (
    xcopy "%SOURCE_ASSETS%" "%DEST_DIST%\%SOURCE_ASSETS%" /s /e /i /y
) else (
    echo Le dossier "%SOURCE_ASSETS%" est introuvable.
)

:: Copier le dossier mods dans dist
if exist "%SOURCE_MODS%" (
    xcopy "%SOURCE_MODS%" "%DEST_DIST%\%SOURCE_MODS%" /s /e /i /y
) else (
    echo Le dossier "%SOURCE_MODS%" est introuvable.
)

echo SUCCES
start dist\Re-world

