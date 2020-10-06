print("What level of brightness is required?")
brightness_desired = int(input())

# Adjust brightness
print("\nAdjusting brightness...\n")

for brightness in range(2, brightness_desired + 1, 2): # start of 2, limit bd+1, step 2
    print("Beep's brightness level:", "*" * brightness)
    print("Bop's brightness level:", "*" * brightness)
    
print("Adjustments complete!")