def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    k = int(data[1])
    cats = list(map(int, data[2:2+n]))
    
    if k == 0:
        print(0)
        return
    
    count = {}
    used_carriers = 0
    max_cats = 0
    left = 0
    
    for right in range(n):
        breed = cats[right]
        
        if breed in count and count[breed] > 0:
            count[breed] += 1
        else:
            if used_carriers < k:
                count[breed] = 1
                used_carriers += 1
            else:
                while used_carriers >= k:
                    left_breed = cats[left]
                    count[left_breed] -= 1
                    if count[left_breed] == 0:
                        used_carriers -= 1
                        del count[left_breed]
                    left += 1
                
                count[breed] = 1
                used_carriers += 1
        
        current_cats = right - left + 1
        if current_cats > max_cats:
            max_cats = current_cats
    
    print(max_cats)

if __name__ == "__main__":
    solve()