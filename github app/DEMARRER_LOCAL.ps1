Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  DEMARRAGE APPLICATION DENEGEMENT" -ForegroundColor Cyan
Write-Host "  (Depuis le dossier github app)" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "[1/3] Activation de l'environnement virtuel..." -ForegroundColor Yellow
if (-not (Test-Path "..\venv\Scripts\Activate.ps1")) {
    Write-Host "Creation de l'environnement virtuel..." -ForegroundColor Yellow
    python -m venv ..\venv
}
& ..\venv\Scripts\Activate.ps1

Write-Host "[2/3] Installation des dependances..." -ForegroundColor Yellow
python -m pip install --upgrade pip
pip install -r requirements.txt

Write-Host "[3/3] Initialisation de la base de donnees..." -ForegroundColor Yellow
python init_db.py

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "  Application disponible sur:" -ForegroundColor Green
Write-Host "  http://localhost:5000/dashboard" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Appuyez sur Ctrl+C pour arreter l'application" -ForegroundColor Yellow
Write-Host ""

python app.py

