@echo off
echo BLU Maritime - Procurement Analysis System
echo ==========================================
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Running procurement analysis...
python procurement_analysis.py
echo.
echo Analysis complete! Check generated files.
pause