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

## Lesson 7-9 — 2026-06-03
**Topic:** Jenkins, Pipelines, CI/CD, GitHub Webhook

**What I built:**
- First Jenkins freestyle job — ran shell commands
- Declarative pipeline with 3 stages (Checkout, System Info, Verify Structure)
- Connected Jenkins to GitHub repo via SCM
- Exposed local Jenkins via ngrok tunnel
- GitHub webhook auto-triggers Jenkins on every git push

**Key concepts:**
- Exit code 0 = success, non-zero = failure
- Jenkinsfile lives in repo = pipeline is version controlled
- -xe flags: -x prints commands, -e stops on failure
- Webhook = GitHub tells Jenkins "something changed, go run"
- ngrok = secure tunnel from internet to localhost

**What CI/CD means in practice:**
- Every git push automatically: pulls code → runs tests → reports result
- No manual deployment steps
- Broken code is caught immediately

## Lesson 10-11 — 2026-06-03
**Topic:** Security scanning, Docker foundations

**What I learned:**
- Trivy scans repos for secrets and misconfigs — runs inside Jenkins pipeline
- git-secrets installs hooks to block commits containing secrets
- --exit-code 0 means Trivy reports findings but doesn't fail the pipeline (use 1 to enforce blocking)
- Docker Desktop runs containers inside a lightweight VM (3.8GB RAM allocated)
- Client vs Server version difference in Docker Desktop setup
- Virtual environments NOT needed inside containers — Docker itself provides isolation
- venv useful locally, Docker image = isolated environment by design

**Docker core concepts:**
- IMAGE = blueprint (like a class)
- CONTAINER = running instance (like an object)
- Dockerfile = build instructions
- .dockerignore = exclude files from image (like .gitignore)
- One image can run many containers simultaneously

**My existing Docker work found:**
- cloud-mini-project:latest — built previously
- digensclub/data-middleware:latest — pushed to Docker Hub previously

**Commands learned:**
- docker images
- docker ps / docker ps --all
- docker history imagename
- docker run hello-world
- docker version / docker info

## Lesson 11-12 — 2026-06-04
**Topic:** Docker deep dive + full CI/CD pipeline

**What I built:**
- Python web app containerised from scratch
- Dockerfile with FROM, LABEL, WORKDIR, COPY, EXPOSE, CMD
- Image built, run, explored from inside, stopped, started
- Pushed to Docker Hub with versioned tags
- Jenkins pipeline: checkout → security scan → build → push → verify
- Every git push now automatically builds and pushes a new versioned image

**Key concepts:**
- Container = isolated Linux environment (Debian inside Kali)
- slim image = minimal tools = small attack surface (28MB RAM usage)
- Image layers = cached = fast rebuilds
- v{BUILD_NUMBER} = automatic versioning
- Pin production to specific versions, never latest
- withCredentials = secrets injected at runtime, never in code
- docker exec -it = shell inside running container
- 0.0.0.0:8000->8000/tcp = host port maps to container port

**Commands mastered:**
- docker build --tag
- docker run --detach --publish --name
- docker exec --interactive --tty
- docker logs --follow
- docker stats --no-stream
- docker stop / start / rm
- docker push / pull
- docker images / docker ps --all
- docker tag

**Pipeline fixes learned:**
- Double quotes in sh "" expand Jenkins variables
- Single quotes in sh '' keep shell variables for bash
- BUILD_NUMBER must be set via script{} block in environment
- Jenkins needs docker group membership: usermod -aG docker jenkins
