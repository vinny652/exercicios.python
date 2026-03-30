import sys

try:
    raio = float(sys.stdin.read().strip())
except ValueError:
    raio = float(input().strip())

area = 3.14159 * raio * raio
print(f"A={area:.4f}")