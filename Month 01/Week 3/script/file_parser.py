import re

def parse_file(file_path):
    with open(file_path, "r") as f:
        content = f.read()

    sections = re.split(r'\n=+\n', content)

    important_info = {}

    # OS section
    for section in sections:
        if "Linux" in section and "Filesystem" not in section:
            lines = section.strip().splitlines()
            for line in lines:
                if "Linux" in line:
                    important_info["OS"] = line
                    break

    # Loggedin user
    for section in sections:
        if "bala" in section and "Filesystem" not in section:
            users = []
            lines = section.strip().splitlines()
            for line in lines:
                if re.match(r'\s*\w+\s+', line):
                    users.append(line.strip())
                important_info["Logged-in Users"] = users
                break

    # CPU info
    for section in sections:
        if "Architecture:" in section:
            cpu_info = {}
            lines = section.strip().splitlines()
            for line in lines:
                if ":" in line:
                    key, value = line.split(":", 1)
                    cpu_info[key.strip()] = value.strip()
            important_info["CPU Info"] = cpu_info
            break

    return important_info



file = "Month 01\Week 3\script\monitor.txt"
output = "Month 01\Week 3\output\log_output.txt"
parsed_info = parse_file(file)

with open(output, "w") as f:
    f.write("\n=== Important System Information ===")
    for key, value in parsed_info.items():
        f.write(f"\n>> {key}:")
        if isinstance(value, list):
            for item in value:
                f.write(f"  {item}")
        elif isinstance(value, dict):
            for k,v in value.items():
                f.write(f"  {k}:  {v}")
        else:
            f.write(f" {value}")