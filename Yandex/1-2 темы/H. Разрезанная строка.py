from collections import deque
import sys

def main():
    data = sys.stdin.read().strip().splitlines()
    n, m = map(int, data[0].split())
    s = data[1].strip()
    pieces = [line.strip() for line in data[2:2+m]]

    k = n // m

    pos_map = {}
    for i in range(0, n, k):
        sub = s[i:i+k]
        pos_map.setdefault(sub, deque()).append(i)

    assigned = []
    for idx, piece in enumerate(pieces, start=1):
        if piece not in pos_map or not pos_map[piece]:
            print("ERROR: piece not found", file=sys.stderr)
            pos = -1
        else:
            pos = pos_map[piece].popleft()
        assigned.append((pos, idx))

    assigned.sort(key=lambda x: x[0])
    result = [str(idx) for _, idx in assigned]
    print(" ".join(result))

if __name__ == "__main__":
    main()
