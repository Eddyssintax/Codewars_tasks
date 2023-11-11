def find_screen_height(width, ratio): 
    form = int(int(width) / (int(ratio.split(":")[0])/int(ratio.split(":")[1])))
    return f"{width}x{form}"

#example
find_screen_height("1024", "4:3")