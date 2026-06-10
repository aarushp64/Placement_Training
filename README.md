# Placement Training

This repository contains my day-wise placement training practice across web development, C++, and Python.

## Repository Structure

- `day 1/`: HTML, CSS, and JavaScript basics.
- `day 2/`: JavaScript mini projects and React/Vite practice apps.
- `day 3/`: C++ practice problems.
- `day 4/`: C++ practice problems and earlier Python practice files.
- `day 5/`: Python practice files (`dict.py`, `func.py`, `list.py`, `set.py`, `string.py`, `tuple.py`).
- `day 6/`: Python OOP and utility practice (`decorator.py`, `filehandling.py`, `generator.py`, `multiThreading.py`, `oops.py`).
- `auto_sync.ps1`: PowerShell script to stage, commit, and push repo changes.

## Tech Stack

- HTML5, CSS3, JavaScript
- React + Vite
- C++
- Python
- PowerShell for repo automation

## How To Run

### Static HTML/CSS/JS files

Open the required `.html` file directly in your browser.

### React projects

There are two Vite apps:

- `day 2/my proj/`
- `day 2/react/`

Run either project with:

```bash
npm install
npm run dev
```

### Auto sync script

Run the root automation script from PowerShell:

```powershell
.\auto_sync.ps1
```

Optional parameters:

- `-CommitMessage "message"`
- `-SkipPull`

## Goal

This repo is used to track consistent daily problem-solving and development practice for placement preparation.