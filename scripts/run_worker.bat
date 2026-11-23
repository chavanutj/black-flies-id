@echo off
rem Usage: run_worker.bat <batch> "<task text>"
cd /d E:\claude-workspace\black-flies-id\repo
jcode run -p antigravity -m gemini-4-neon-medium --no-update "You are a worker on the black fly identification-key project in E:\claude-workspace\black-flies-id\repo. FIRST read inbox\WORKER_BRIEF.md and follow it exactly (staging mode, batch name '%~1'). YOUR TASK: %~2 . Work until the task is complete and merge_staging --check passes, then finish with a short report." < nul > inbox\worker_%~1.log 2>&1
