# DevOps Engineer — Quick Reference Handbook
**Built during hands-on training sessions with digensclub**  
**Last updated:** 2026-06-02  
**Machine:** Kali Linux 2026.2 | Shell: zsh

---

## TABLE OF CONTENTS
1. [Navigation & Filesystem](#1-navigation--filesystem)
2. [File Operations](#2-file-operations)
3. [Viewing & Searching Files](#3-viewing--searching-files)
4. [Permissions & Ownership](#4-permissions--ownership)
5. [Processes & Services](#5-processes--services)
6. [Networking Commands](#6-networking-commands)
7. [Disk & Memory](#7-disk--memory)
8. [Git — Complete Reference](#8-git--complete-reference)
9. [SSH — Complete Reference](#9-ssh--complete-reference)
10. [Shell Features & Tricks](#10-shell-features--tricks)
11. [Linux Filesystem Map](#11-linux-filesystem-map)
12. [Troubleshooting Playbook](#12-troubleshooting-playbook)
13. [Security Checklist](#13-security-checklist)
14. [Conventional Commit Messages](#14-conventional-commit-messages)
15. [Environment & Config](#15-environment--config)

---

## 1. Navigation & Filesystem

```bash
pwd                        # Print Working Directory — where am I right now?
cd /etc                    # Change Directory to /etc
cd ~                       # Go to home directory (/home/digensclub)
cd -                       # Go back to previous directory
cd ..                      # Go up one level
ls                         # List files
ls -l                      # Long format (permissions, size, date)
ls -a                      # Show hidden files (starting with .)
ls -la                     # Long format + hidden files
ls -lh                     # Long format + human-readable sizes (KB, MB, GB)
ls -lt                     # Sort by modification time (newest first)
tree                       # Visual directory tree (install: apt install tree)
find /etc -type f          # Find all FILES inside /etc
find /etc -type d          # Find all DIRECTORIES inside /etc
find ~ -name "*.md"        # Find files matching pattern
find ~ -mtime -7           # Files modified in last 7 days
find ~ -size +100M         # Files larger than 100MB
```

**Flag breakdown — ls:**
| Flag | Long form | Meaning |
|------|-----------|---------|
| `-l` | `--format=long` | Show permissions, owner, size, date |
| `-a` | `--all` | Include hidden files (dotfiles) |
| `-h` | `--human-readable` | Sizes as KB/MB/GB |
| `-t` | | Sort by time modified |
| `-r` | `--reverse` | Reverse sort order |
| `-S` | | Sort by file size |

---

## 2. File Operations

```bash
touch filename.txt              # Create empty file
mkdir foldername                # Make directory
mkdir -p a/b/c                  # Make nested dirs, no error if exists
mkdir -p proj/{src,tests,docs}  # Brace expansion — creates 3 dirs at once
cp file.txt backup.txt          # Copy file
cp -r folder/ backup/           # Copy directory recursively
mv file.txt newname.txt         # Move or rename
rm file.txt                     # Delete file (NO RECYCLE BIN — permanent)
rm -r folder/                   # Delete directory and contents
rm -ri folder/                  # Delete with confirmation prompt (safer)
ln -s /original /path/link      # Create symbolic link (shortcut)
cat > file.txt << 'EOF'         # Write multi-line content to file
line 1                          # (everything between EOF markers)
line 2
EOF
cat >> file.txt                 # Append to file (>> adds, > overwrites)
```

**⚠️ WARNING:** `rm` is permanent. There is no undo. Always double-check before running.

**Flag breakdown — mkdir:**
| Flag | Long form | Meaning |
|------|-----------|---------|
| `-p` | `--parents` | Create parent dirs too, no error if exists |
| `-v` | `--verbose` | Print each directory as it's created |

---

## 3. Viewing & Searching Files

```bash
cat file.txt                    # Print entire file to screen
cat -n file.txt                 # Print with line numbers
head file.txt                   # First 10 lines
head --lines=20 file.txt        # First 20 lines  (short: -n 20)
tail file.txt                   # Last 10 lines
tail --lines=20 file.txt        # Last 20 lines
tail --follow file.txt          # Live follow (great for logs) (short: -f)
less file.txt                   # Scroll through file (q to quit)
grep "word" file.txt            # Find lines containing "word"
grep --ignore-case "word" f.txt # Case-insensitive search (short: -i)
grep --recursive "word" /etc/   # Search all files in directory (short: -r)
grep --line-number "word" f.txt # Show line numbers (short: -n)
grep --invert-match "word" f.txt# Lines NOT containing word (short: -v)
grep --extended-regexp "a|b"    # Use regex OR (short: -E)
grep --files-with-matches "w" / # Show only filenames (short: -l)
cat file.txt | grep "word"      # Pipe: filter output of cat through grep
```

**Grep regex quick reference:**
| Pattern | Matches |
|---------|---------|
| `^word` | Lines STARTING with "word" |
| `word$` | Lines ENDING with "word" |
| `^word$` | Lines that are EXACTLY "word" |
| `wo.d` | Any single character where `.` is |
| `wo*d` | Zero or more 'o' characters |
| `a\|b` | "a" OR "b" (needs -E flag) |

---

## 4. Permissions & Ownership

```bash
ls -la                          # View permissions of files
chmod 600 file                  # Owner: rw, Group: none, Others: none
chmod 644 file                  # Owner: rw, Group: r, Others: r
chmod 755 file                  # Owner: rwx, Group: rx, Others: rx
chmod 700 directory/            # Owner: rwx only (private directory)
chown user:group file           # Change owner and group
chown digensclub:digensclub f   # Give file to digensclub user
sudo chown root:root file       # Give file to root
```

**Permission number reference:**
```
Number → Binary → Permissions
  7    →  111   → read + write + execute  (rwx)
  6    →  110   → read + write            (rw-)
  5    →  101   → read + execute          (r-x)
  4    →  100   → read only               (r--)
  0    →  000   → no permissions          (---)

Three digits = [owner][group][others]
chmod 644 = owner(6=rw) group(4=r) others(4=r)
```

**SSH-specific permissions (MUST follow exactly):**
```bash
chmod 700 ~/.ssh/               # SSH directory
chmod 600 ~/.ssh/private_key    # Private key
chmod 644 ~/.ssh/private_key.pub# Public key
chmod 600 ~/.ssh/config         # SSH config
chmod 600 ~/.ssh/authorized_keys# Authorized keys
```

---

## 5. Processes & Services

```bash
ps aux                          # All running processes
ps aux | grep jenkins           # Find specific process
top                             # Live process monitor (q to quit)
htop                            # Better live monitor (apt install htop)
kill 1234                       # Send SIGTERM to process ID 1234 (graceful)
kill -9 1234                    # Send SIGKILL (force kill, no cleanup)
killall nginx                   # Kill all processes named nginx
pgrep nginx                     # Find PID of process by name
pstree                          # Visual process tree

# systemctl — service management
systemctl status nginx          # Is it running? Any errors?
systemctl start nginx           # Start service now
systemctl stop nginx            # Stop service now
systemctl restart nginx         # Stop then start
systemctl reload nginx          # Reload config without stopping
systemctl enable nginx          # Auto-start on boot
systemctl disable nginx         # Don't auto-start on boot
systemctl list-units --type=service  # List all services
journalctl -u nginx             # View logs for a service
journalctl -u nginx --follow    # Live logs for a service (short: -f)
journalctl --since "1 hour ago" # Logs from last hour
```

**ps aux columns explained:**
```
USER    PID  %CPU  %MEM  VSZ    RSS   TTY  STAT  START  TIME  COMMAND
root      1   0.0   0.1  168MB  13MB  ?    Ss    08:00  0:01  /sbin/init
         ↑                                  ↑
     Process ID                         S=sleeping, R=running, Z=zombie
```

---

## 6. Networking Commands

```bash
ip address                      # Show all network interfaces and IPs
ip address show eth0            # Show specific interface
ip route                        # Show routing table
ping google.com                 # Test connectivity (Ctrl+C to stop)
ping --count=3 google.com       # Send exactly 3 pings (short: -c 3)
ping --interval=0.2 google.com  # Ping every 0.2 seconds (short: -i)
traceroute google.com           # Trace network path to destination
nslookup google.com             # DNS lookup
dig google.com                  # Detailed DNS lookup
dig google.com +short           # Just the IP address
curl https://example.com        # Fetch URL content
curl --head https://example.com # Headers only (short: -I)
curl --output file.zip URL      # Download file (short: -o)
curl --location URL             # Follow redirects (short: -L)
wget URL                        # Download file

# ss — socket statistics (modern netstat)
ss --listen --tcp --numeric --processes   # TCP listening ports
ss --listen --udp --numeric --processes   # UDP listening ports
ss --all --numeric                        # All connections
ss --established                          # Active connections only

# ss flag reference:
# -t / --tcp          → TCP sockets
# -u / --udp          → UDP sockets  
# -l / --listen       → Only listening sockets
# -n / --numeric      → Numbers not names (22 not 'ssh')
# -p / --processes    → Show owning process
# -a / --all          → All sockets (listening + connected)

netstat -tulpn                  # Old equivalent of ss (still works)
```

---

## 7. Disk & Memory

```bash
df --human-readable             # Disk space on all filesystems (short: -h)
df --human-readable /           # Disk space on root only
du --summarize --human-readable /var/*   # Size of each item in /var
du --human-readable --max-depth=1 ~     # Size of home subdirectories
du --human-readable . | sort --reverse --human-numeric-sort | head

free --human                    # RAM and swap usage (short: -h)
free --human --seconds=2        # Refresh every 2 seconds (short: -s 2)
cat /proc/meminfo               # Detailed memory information
cat /proc/cpuinfo               # CPU details
nproc                           # Number of CPU cores
lscpu                           # Detailed CPU information
lsblk                           # List block devices (disks, partitions)
lsblk --output NAME,SIZE,TYPE,MOUNTPOINT  # Custom columns
```

**Memory terms explained:**
```
MemTotal     → Total physical RAM installed
MemFree      → RAM completely unused
MemAvailable → RAM available for new processes (free + reclaimable cache)
              ↑ Always use this one, not MemFree
Swap         → Disk space used as overflow RAM (slow)
buff/cache   → RAM used for disk caching (OS reclaims this when needed)
```

---

## 8. Git — Complete Reference

### Setup
```bash
git config --global user.name "Your Name"
git config --global user.email "you@email.com"
git config --global init.defaultBranch main
git config --global core.editor nano
git config --global --list              # View all global config
```

### Daily workflow
```bash
git status                      # What's changed? What's staged?
git diff                        # What changed in unstaged files?
git diff --staged               # What's in staging area?
git add filename                # Stage specific file
git add .                       # Stage everything
git add --patch                 # Interactively choose what to stage
git commit --message "feat: add login page"   # Commit (short: -m)
git commit --amend --message "fixed msg"      # Fix last commit message
git push                        # Push to remote
git push --set-upstream origin main   # First push of new branch (short: -u)
git pull                        # Fetch + merge from remote
```

### Branching
```bash
git branch                      # List local branches
git branch --all                # List all branches including remote
git branch feature/login        # Create new branch
git switch feature/login        # Switch to branch (modern)
git checkout feature/login      # Switch to branch (older syntax)
git switch --create feature/x   # Create and switch (short: -c)
git merge feature/login         # Merge branch into current
git branch --delete feature/x   # Delete branch (short: -d)
```

### History & inspection
```bash
git log                         # Full commit history
git log --oneline               # One line per commit
git log --oneline --graph       # Visual branch graph
git log --oneline --all         # Include all branches
git show a02adee                # Show details of a commit
git diff main..feature/x        # Difference between two branches
```

### Undoing things
```bash
git restore filename            # Discard unstaged changes to file
git restore --staged filename   # Unstage a file
git reset HEAD~1                # Undo last commit, keep changes staged
git reset --hard HEAD~1         # Undo last commit, DISCARD changes (dangerous)
git revert a02adee              # Create new commit that undoes a commit (safe)
```

### Remote
```bash
git remote --verbose            # Show remotes (short: -v)
git remote add origin URL       # Add remote named 'origin'
git remote set-url origin URL   # Change remote URL
git fetch                       # Download changes without merging
git clone URL                   # Clone a repository
```

---

## 9. SSH — Complete Reference

```bash
ssh user@hostname               # Connect to server
ssh -i ~/.ssh/keyfile user@host # Connect with specific key
ssh -p 2222 user@host           # Connect on non-standard port
ssh -L 8080:localhost:80 user@host   # Local port forwarding
ssh -v user@host                # Verbose (debug connection issues)
ssh -T git@github.com           # Test GitHub SSH auth

ssh-keygen -t ed25519 -C "email@example.com" -f ~/.ssh/keyname
# -t ed25519   → key type (ed25519 is modern and secure)
# -C "comment" → label for the key (usually your email)
# -f filename  → where to save the key

ssh-keygen -t rsa -b 4096       # RSA key (older, still accepted everywhere)

eval "$(ssh-agent -s)"          # Start SSH agent
ssh-add ~/.ssh/keyname          # Add key to agent
ssh-add --list                  # List loaded keys (short: -l)

# Key file rules — MUST follow:
# private key (no extension) → chmod 600
# public key (.pub)          → chmod 644
# ~/.ssh/ directory          → chmod 700
# ~/.ssh/config              → chmod 600
```

**~/.ssh/config format:**
```
Host nickname
  HostName actual.server.ip.or.domain
  User username
  IdentityFile ~/.ssh/keyfilename
  Port 22
```

**Private vs Public key — NEVER confuse:**
```
~/.ssh/github_devops      ← PRIVATE — never share, never paste anywhere
~/.ssh/github_devops.pub  ← PUBLIC  — paste to GitHub, servers, anywhere
```

---

## 10. Shell Features & Tricks

```bash
# Brace expansion
mkdir -p project/{src,tests,docs}    # Creates 3 dirs
echo {1..5}                          # Prints: 1 2 3 4 5
touch file{1..10}.txt                # Creates file1.txt through file10.txt

# Redirections
command > file.txt          # Stdout to file (overwrites)
command >> file.txt         # Stdout to file (appends)
command 2> errors.txt       # Stderr to file
command 2>/dev/null         # Discard errors
command &> all.txt          # Both stdout and stderr to file

# File descriptors:
# 0 = stdin  (keyboard input)
# 1 = stdout (normal output)
# 2 = stderr (error output)

# Pipes
command1 | command2         # Output of cmd1 becomes input of cmd2
ps aux | grep nginx         # Find nginx in process list
cat /etc/passwd | wc -l     # Count lines in passwd file

# Variables
MY_VAR="hello"              # Set variable
echo $MY_VAR                # Use variable
export MY_VAR="hello"       # Export so child processes see it

# Permanent variables — add to ~/.zshrc (Kali uses zsh)
echo 'export DEVOPS_LAB="$HOME/Documents/coderepos/devops-lab"' >> ~/.zshrc
source ~/.zshrc              # Reload config (or restart terminal)

# Quote rules — critical to understand
echo '$HOME'                # Prints literally: $HOME   (single = no expand)
echo "$HOME"                # Prints: /home/digensclub  (double = expands)
command << 'EOF'            # Single quote EOF = no expansion inside
command << EOF              # No quote = expansion happens inside

# Useful shortcuts
Ctrl+C                      # Kill running command
Ctrl+Z                      # Suspend command (bg to resume in background)
Ctrl+L                      # Clear screen
Ctrl+R                      # Search command history
!!                          # Repeat last command
!ssh                        # Repeat last command starting with 'ssh'
sudo !!                     # Run last command with sudo
```

---

## 11. Linux Filesystem Map

```
/                   Root of everything
├── etc/            ★ CONFIGS — all service configuration files live here
│   ├── hosts       Local DNS overrides
│   ├── resolv.conf DNS nameserver settings
│   ├── passwd      User accounts (no passwords — just metadata)
│   ├── shadow      Hashed passwords (root only)
│   ├── ssh/        SSH server config
│   ├── apt/        Package manager config
│   └── cron*/      Scheduled task configs
├── var/            ★ VARIABLE DATA — changes at runtime
│   ├── log/        All system and service logs
│   ├── lib/        Database files, Docker images, Jenkins data
│   ├── cache/      Cached data (apt packages etc)
│   ├── www/        Web server files
│   └── tmp/        Temp files (NOT cleared on reboot, unlike /tmp)
├── home/           User home directories
│   └── digensclub/ Your files live here
├── root/           Root user's home (separate from /home)
├── tmp/            ★ Temp files — CLEARED on reboot
├── proc/           ★ VIRTUAL — live kernel/process data (not real files)
│   ├── version     Kernel version
│   ├── meminfo     Memory usage
│   ├── cpuinfo     CPU details
│   └── [PID]/      Directory for each running process
├── sys/            Virtual — hardware/kernel parameters
├── dev/            Devices as files
│   ├── nvme0n1     Your NVMe SSD
│   ├── null        Black hole (discards everything)
│   └── zero        Infinite zeros (useful for wiping)
├── bin/ → usr/bin  Essential binaries (ls, cp, bash, cat...)
├── sbin/→ usr/sbin System binaries (mount, iptables...)
├── lib/ → usr/lib  Shared libraries
├── usr/            Most installed software
│   ├── bin/        User commands
│   ├── local/      Manually installed software
│   └── share/      Documentation, icons, data
├── opt/            Optional/third-party software (OCI CLI goes here)
├── boot/           Kernel and bootloader (rarely touched)
├── mnt/            Manual mount points
└── snap/           Snap packages
```

---

## 12. Troubleshooting Playbook

### "Something is listening on a port — what is it?"
```bash
sudo ss --listen --tcp --numeric --processes
sudo ss --listen --udp --numeric --processes
sudo lsof -i :8080              # Who is using port 8080?
```

### "Service won't start"
```bash
systemctl status servicename            # Read the error
journalctl -u servicename --no-pager    # Full logs
journalctl -u servicename --since "5 minutes ago"
```

### "Disk is full"
```bash
df --human-readable                                    # Which filesystem is full?
sudo du --human-readable --max-depth=1 /var | sort --reverse --human-numeric-sort
sudo du --human-readable --max-depth=1 / | sort --reverse --human-numeric-sort
```

### "Can't connect to server"
```bash
ping hostname                   # Is it reachable at all?
traceroute hostname             # Where does it fail?
dig hostname                    # Is DNS resolving?
curl --verbose https://hostname # What happens at HTTP level?
ssh -v user@hostname            # Debug SSH connection
```

### "Permission denied"
```bash
ls -la filename                 # Check permissions
whoami                          # What user am I?
groups                          # What groups am I in?
sudo -l                         # What can I run with sudo?
```

### "Command not found"
```bash
which commandname               # Is it installed? Where?
type commandname                # Shell built-in or external?
apt list --installed | grep pkg # Is package installed?
sudo apt install packagename    # Install it
```

### "Port I need is already in use"
```bash
sudo lsof --internet -P | grep :8080    # What process owns port 8080?
sudo kill $(sudo lsof -t -i:8080)       # Kill it
```

---

## 13. Security Checklist

### Every new server — run this audit
```bash
# 1. Who can log in?
cat /etc/passwd | grep --extended-regexp "/bin/bash|/bin/zsh"

# 2. Who has sudo?
cat /etc/sudoers
sudo cat /etc/sudoers.d/*

# 3. What ports are open?
sudo ss --listen --tcp --numeric --processes
sudo ss --listen --udp --numeric --processes

# 4. What services start on boot?
systemctl list-units --type=service --state=enabled

# 5. Last logins
last | head -20

# 6. Failed login attempts
sudo journalctl --grep="Failed password" | tail -20

# 7. Check SSH config
sudo grep --extended-regexp "^PermitRootLogin|^PasswordAuthentication|^Port" /etc/ssh/sshd_config
```

### SSH hardening (production servers)
```bash
# In /etc/ssh/sshd_config — these should be set:
PermitRootLogin no              # Never allow root SSH login
PasswordAuthentication no       # Keys only, no passwords
PubkeyAuthentication yes        # Confirm key auth is on
Port 2222                       # Non-standard port (obscurity, not security)
```

### .gitignore — always include these
```
*.env
.env*
*secret*
*password*
*credential*
*.key
*.pem
.ssh/
```

---

## 14. Conventional Commit Messages

```
format: <type>: <short description>

feat:     New feature or capability
fix:      Bug fix or correction
docs:     Documentation, journal entries, README
chore:    Setup, config, tooling, dependencies
security: Security fixes or hardening
refactor: Code restructure (no feature change)
test:     Adding or fixing tests
ci:       CI/CD pipeline changes
infra:    Infrastructure / Terraform changes

Examples:
git commit -m "feat: add Docker containerisation for web app"
git commit -m "fix: correct SSH key permissions to 600"
git commit -m "docs: add lesson 5 journal entry"
git commit -m "security: remove hardcoded credentials from config"
git commit -m "chore: add .gitignore for terraform state files"
git commit -m "infra: provision OCI compute instance with Terraform"
```

---

## 15. Environment & Config

```bash
# Your key paths — Kali Linux setup
~/.zshrc                        # Shell config (Kali uses zsh not bash)
~/.ssh/config                   # SSH connection profiles
$DEVOPS_LAB                     # = /home/digensclub/Documents/coderepos/devops-lab
$HOME                           # = /home/digensclub

# Reload shell config
source ~/.zshrc

# Add permanent alias
echo 'alias lab="cd $DEVOPS_LAB"' >> ~/.zshrc
source ~/.zshrc
lab                             # Now 'lab' takes you to your devops-lab

# Check all environment variables
env
printenv PATH                   # See command search path

# apt package management 
sudo apt update                 # Refresh package list
sudo apt upgrade                # Upgrade installed packages
sudo apt install packagename    # Install package
sudo apt remove packagename     # Remove package
sudo apt search keyword         # Search for package
apt show packagename            # Show package details
```

---

*This handbook grows with every lesson. Update it after each session.*  
*Handbook lives at: $DEVOPS_LAB/reference-handbook.md*
