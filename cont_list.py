import subprocess

result = subprocess.run(
    ["git", "log", "--format=%aN"],
    capture_output=True,
    text=True
)

names = result.stdout.split("\n")
unique_names = set(names)

print("Contributors:")
for name in unique_names:
    print(name)
