def conver_pixel_to_distance_to_meters(pixel_distance, reference_ht_in_mts, referencce_ht_in_pixels):
    return (pixel_distance * reference_ht_in_mts) / referencce_ht_in_pixels

def convert_mts_to_pixel_distance(meters, refernce_ht_in_mts, referencce_ht_in_pixels):
    return (meters * referencce_ht_in_pixels) / refernce_ht_in_mts
