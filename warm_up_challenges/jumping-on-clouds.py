def jumping_on_clouds(clouds):
    current_cloud = 0
    clouds_length = len(clouds)
    last_cloud = clouds_length - 1
    jumps = 0

    while current_cloud != last_cloud:
        if current_cloud + 2 < clouds_length and clouds[current_cloud + 2] == 0:
            current_cloud += 2
        else:
            current_cloud += 1
        jumps += 1

    return jumps

print(jumping_on_clouds([0, 0, 1, 0, 0, 1, 0]))
print(jumping_on_clouds([0, 0, 0, 0, 1, 0]))
