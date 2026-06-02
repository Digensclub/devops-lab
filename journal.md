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
