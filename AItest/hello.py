colors = ['\033[31m', '\033[33m', '\033[32m', '\033[36m', '\033[34m', '\033[35m']
reset = '\033[0m'

message = "Hello, World!"
colored = ''.join(colors[i % len(colors)] + ch + reset for i, ch in enumerate(message))
print(colored)
