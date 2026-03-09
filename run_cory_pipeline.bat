@echo off
cd /d C:\Users\kalki\Documents\ColaberryDAClass\Cory\cory_learning_pipeline
call venv\Scripts\activate
python -m src.run_pipeline --start 2025-11-01 --end 2026-02-01
pause