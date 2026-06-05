param(
    [string]$CommitMessage,
    [switch]$SkipPull
)

$ErrorActionPreference = "Stop"

function Invoke-Git {
    param([string[]]$Args)
    & git @Args
    if ($LASTEXITCODE -ne 0) {
        throw "git $($Args -join ' ') failed with exit code $LASTEXITCODE"
    }
}

Write-Host "[1/6] Verifying git repository..."
& git rev-parse --is-inside-work-tree *> $null
if ($LASTEXITCODE -ne 0) {
    throw "Current directory is not a git repository. Run this script from your repo root."
}

$currentBranch = (git branch --show-current).Trim()
if ([string]::IsNullOrWhiteSpace($currentBranch)) {
    throw "Could not determine current branch."
}

$remoteName = "origin"
& git remote get-url $remoteName *> $null
if ($LASTEXITCODE -ne 0) {
    throw "Remote '$remoteName' is not configured."
}

if (-not $SkipPull) {
    Write-Host "[2/6] Pulling latest changes from $remoteName/$currentBranch..."
    Invoke-Git -Args @("pull", "--rebase", $remoteName, $currentBranch)
} else {
    Write-Host "[2/6] Skipping pull (--SkipPull used)."
}

Write-Host "[3/6] Scanning and staging all changes (tracked + new files)..."
Invoke-Git -Args @("add", "-A")

Write-Host "[4/6] Checking if there is anything to commit..."
$pending = git status --porcelain
if ([string]::IsNullOrWhiteSpace(($pending -join "").Trim())) {
    Write-Host "No changes detected. Nothing to commit."
    exit 0
}

if ([string]::IsNullOrWhiteSpace($CommitMessage)) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $CommitMessage = "Auto update: $timestamp"
}

Write-Host "[5/6] Creating commit..."
Invoke-Git -Args @("commit", "-m", $CommitMessage)

Write-Host "[6/6] Pushing to $remoteName/$currentBranch..."
Invoke-Git -Args @("push", $remoteName, $currentBranch)

Write-Host "Done. Changes committed and pushed successfully."