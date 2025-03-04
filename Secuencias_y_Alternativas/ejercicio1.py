def update_arrival(h,m,d):
    min_total = h * 60 + m + d
    new_hrs = int(min_total / 60) % 24
    new_min = min_total % 60
    return new_hrs,new_min

print(update_arrival(10,23,20))