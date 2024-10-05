def calculate_pyramid_height(number_of_blocks):
    height = math.sqrt(number_of_blocks) if math.sqrt(number_of_blocks).is_integer() else int(math.sqrt(number_of_blocks)) + 1
    return height
