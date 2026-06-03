# DevOps Learning Journal
**Name:** digensclub  
**Machine:** Kali Linux 2026.2  
**Started:** 2026-06-02  
**Goal:** DevSecOps / Cloud / AI Engineer by end of 2026

---

## Lesson 1 — 2026-06-02
**Topic:** System orientation  
**What I did:**
- Checked OS, RAM, CPU, disk, network
- Confirmed sudo access
- Verified Git, Python, curl, Docker pre-installed

**What I learned:**
- My machine: Kali 2026.2, 16GB RAM, 8 cores, 164GB free
- Docker 29.5.2 already installed — saves Phase 2 setup time
- `ping -c 3` tests network connectivity with 3 packets
- 0% packet loss = healthy network

**Commands used:**
- cat /etc/os-release
- free -h && nproc
- df -h /
- whoami && hostname
- ping -c 3 google.com

---

## Lesson 2 — 2026-06-02
**Topic:** Professional workspace setup  
**What I did:**
- Created full 4-phase devops-lab folder structure

**What I learned:**
- mkdir -p creates nested directories in one command
- Brace expansion {} creates multiple paths at once
- find -type d lists only directories recursively

**Commands used:**
- mkdir -p ~/devops-lab/{...}
- find ~/devops-lab -type d | sort

---

## Lesson 3 & 4 — 2026-06-02
**Topic:** Git setup, SSH authentication, first GitHub push

**What I did:**
- Configured Git global identity
- Generated ED25519 SSH key pair
- Fixed accidental private key exposure (important lesson)
- Set correct SSH permissions (600 private, 644 public)
- Added public key to GitHub
- Pushed first commit to github.com/Digensclub/devops-lab

**What I learned:**
- Private key = no extension = NEVER share
- Public key = .pub = safe to share
- SSH 600/644 permission rules
- git add → git stage → git commit → git push workflow
- git commit --amend fixes last commit message
- $(date) expands in double quotes, not single quotes
- Kali uses zsh not bash → always edit ~/.zshrc

**Commands used:**
- git config --global
- ssh-keygen -t ed25519
- chmod 600 / 644
- ssh -T git@github.com
- git remote add origin
- git push -u origin main
- git log --oneline


## Lesson 5-6 — 2026-06-02
**Topic:** Linux filesystem, flags deep dive, process investigation

**Key findings on my machine:**
- Jenkins running on port 8080 (PID 1069, java process, jenkins user)
- SSH server installed but disabled (correct — only connect OUT not IN)
- postgres and jenkins users have /bin/bash (can log in — audit later)
- MySQL, PostgreSQL, Redis, OpenVAS all installed

**Critical concepts learned:**
- /etc=configs, /var=runtime data, /proc=virtual kernel window, /tmp=cleared on reboot
- MemAvailable not MemFree = true available RAM
- ss --listen --tcp --numeric --processes = open ports
- lsof -i :PORT = what owns a port
- 2>/dev/null = discard errors (/dev/null = Linux black hole)
- Single quotes = no expansion, double quotes = expand variables
- File descriptors: 0=stdin 1=stdout 2=stderr

**Commands mastered:**
- ss, lsof, grep -E, chmod, find, du, df, systemctl, journalctl
- All flags understood in long form

