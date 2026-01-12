@echo off
echo ========================================
echo   DEMARRAGE APPLICATION DENEGEMENT
echo   (Depuis le dossier github app)
echo ========================================
echo.

echo [1/3] Activation de l'environnement virtuel...
if not exist "..\venv\Scripts\activate.bat" (
    echo Creation de l'environnement virtuel...
    python -m venv ..\venv
)
call ..\venv\Scripts\activate.bat

echo [2/3] Installation des dependances...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo [3/3] Initialisation de la base de donnees...
python init_db.py

echo.
echo ========================================
echo   Application disponible sur:
echo   http://localhost:5000/dashboard
echo ========================================
echo.
echo Appuyez sur Ctrl+C pour arreter l'application
echo.

python app.py

pause

