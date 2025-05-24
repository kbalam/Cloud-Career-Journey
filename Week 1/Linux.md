# Week 1 – Linux Progress

This week I focused on foundational Linux skills needed for working with cloud environments, especially EC2 instances. Here’s what I covered:

---

## 📁 Linux File System Navigation

- `cd` – Change directory  
- `ls` – List contents of a directory  
- `pwd` – Print current working directory  

---

## 📄 Viewing File Contents

- `cat` – Display full file content  
- `less` – View long files page-by-page  
- `head` – View the first lines of a file  
- `tail` – View the last lines of a file  

---

## 📂 Creating Files & Directories

- `mkdir` – Create new directories  
- `touch` – Create new empty files  

---

## 🔁 Copying, Moving & Deleting Files

- `cp` – Copy files/directories  
- `mv` – Move or rename files  
- `rm` – Remove files or directories  

---

## ➡️ Pipes and Redirection

- `>` – Redirect output to a file (overwrite)  
- `>>` – Append output to a file  
- `2>` – Redirect error output  
- `&>` – Redirect both stdout and stderr  
- `cut` – Cut specific columns from text  
- `tee` – Output to terminal and file simultaneously  

---

## 🔍 Searching Files and Directories

- `plocate` – Fast file name search (index-based)  
- `find` – Search files by name, type, size, etc.

---

## 🔎 Searching for Text in Files

- `grep` – Search for strings or patterns inside files  

---

## 🆚 Comparing Files

- `cmp` – Compare two binary/text files  
- `sha256sum` – Check file integrity via hash  
- `diff` – Compare line-by-line differences  

---

## ✍️ Working with Text Editors

- `vim` – Editing files from terminal efficiently  
  - Open: `vim filename`  
  - Insert mode: press `i`  
  - Save and exit: `Esc → :wq`  
  - Exit without saving: `Esc → :q!`  

---

## 🔐 File Permissions and Ownership

- `chmod` – Change file permission bits  
- `chown` – Change file ownership (user)  
- `chgrp` – Change file group ownership  

---

## 🧪 Real Environment Practice

- ✅ Navigated an **Ubuntu EC2 instance** via SSH  
- ✅ Practiced all commands directly on EC2 terminal  
- ✅ Edited files, checked logs, and set permissions

---

## 🧠 Key Learnings & Reflections

- Understood how Linux handles files and permissions
- Practiced combining commands using `|` and redirection
- Realized how important `grep`, `cut`, and `find` are in real troubleshooting

---

## 🔗 Useful Resources

- [Linux Journey](https://linuxjourney.com/)
- [Explainshell](https://explainshell.com/) – Understand what a command does
- [Ubuntu Man Pages](https://manpages.ubuntu.com/)

