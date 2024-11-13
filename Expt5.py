def move_disk(src, dest):
    print(f"Move disk from {src} to {dest}")

def solve_hanoi(n, src, aux, dest):
    if n == 1:
        move_disk(src, dest)
        return
    solve_hanoi(n - 1, src, dest, aux)
    move_disk(src, dest)
    solve_hanoi(n - 1, aux, src, dest)

def main():
    n = int(input("Enter the number of disks: "))
    solve_hanoi(n, 'A', 'B', 'C')
main()
