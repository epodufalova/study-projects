import numpy as np
from PIL import Image

def create_structuring_element(shape, n, m):
    if shape == "rectangle":
        return np.ones((n, m), dtype=np.uint8)
    
    elif shape == "cross":
        se = np.zeros((n, m), dtype=np.uint8)
        se[n // 2, :] = 1 
        se[:, m // 2] = 1 
        return se
    
    elif shape == "circle":
        se = np.zeros((n, m), dtype=np.uint8)
        cy, cx = n // 2, m // 2
        for y in range(n):
            for x in range(m):
                if (x - cx) ** 2 + (y - cy) ** 2 <= (min(n, m) // 2) ** 2:
                    se[y, x] = 1
        return se
    
    else:
        raise ValueError("Unknown structuring element")

def dilate(image, se):
    h, w = image.shape
    sh, sw = se.shape
    pad_h, pad_w = sh // 2, sw // 2
    padded = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)
    result = np.zeros_like(image)

    for i in range(h):
        for j in range(w):
            if np.any(padded[i:i+sh, j:j+sw][se == 1] > 0):  
                result[i, j] = np.max(padded[i:i+sh, j:j+sw][se == 1])  
    return result

def erode(image, se):
    h, w = image.shape
    sh, sw = se.shape
    pad_h, pad_w = sh // 2, sw // 2
    padded = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=255) 
    result = np.zeros_like(image)

    for i in range(h):
        for j in range(w):
            if np.all(padded[i:i+sh, j:j+sw][se == 1] == 255):  
                result[i, j] = np.min(padded[i:i+sh, j:j+sw][se == 1])
            else:
                result[i, j] = 0
    return result

def opening(image, se):
    return dilate(erode(image, se), se)

def closing(image, se):
    return erode(dilate(image, se), se)

def main():
    input_path = "simpletest.bmp"
    output_path = "output.bmp"
    
    image = Image.open(input_path).convert("L")
    image = np.array(image)

    if image.ndim != 2:  
        print("The input image is not in grayscale. Please provide a grayscale image.")
        return

    invert = False
    if np.mean(image) > 127: 
        invert = True
        image = 255 - image  

    operation = input("Enter operation (dilation, erosion, opening, closing): ").strip().lower()
    if operation not in ["dilation", "erosion", "opening", "closing"]:
        print("Error: Unknown operation")
        return

    shape = input("Choose structuring element (rectangle, circle, cross): ").strip().lower()
    if shape not in ["rectangle", "circle", "cross"]:
        print("Error: Unknown structuring element")
        return

    if shape == "circle":
        m = int(input("Enter radius: "))
        se = create_structuring_element(shape, 2 * m + 1, 2 * m + 1)
    else:
        n = int(input("Enter height: "))
        m = int(input("Enter width: "))
        se = create_structuring_element(shape, n, m)

    if operation == "dilation":
        result = dilate(image, se)
    elif operation == "erosion":
        result = erode(image, se)
    elif operation == "opening":
        result = opening(image, se)
    elif operation == "closing":
        result = closing(image, se)

    if invert:
        result = 255 - result

    output_image = Image.fromarray(result)
    output_image.save(output_path)
    print(f"Result saved as {output_path}")

if __name__ == "__main__":
    main()
