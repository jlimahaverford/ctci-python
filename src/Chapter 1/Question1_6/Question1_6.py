from typing import Iterable

class Question1_6:

    def __init__(self, image):
        self.image = image

    def check(self):
        if not isinstance(self.image, Iterable):
            print('Image is not iterable')
            return False
        n = len(self.image)
        if not all(isinstance(x, Iterable) and len(x) == n for x in self.image):
            print('Image does not have even lengths')
            return False
        return True

    def rotate_image(self):
        if not self.check():
            return -1

        n = len(self.image)
        n_over_two_ceil = n//2 if (n % 2) == 0 else (n+1)//2
        n_over_two_floor = n//2 if (n % 2) == 0 else (n-1)//2

        for i in range(n_over_two_ceil):
            for j in range(n_over_two_floor):
                hold = self.image[i][j]
                self.image[i][j] = self.image[n-j-1][i]
                self.image[n-j-1][i] = self.image[n-i-1][n-j-1]
                self.image[n-i-1][n-j-1] = self.image[j][n-i-1]
                self.image[j][n-i-1] = hold

    def print_image(self):
        if not self.check():
            return -1
        for line in self.image:
            print(line)


if __name__ == '__main__':
    image1 = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
    obj1 = Question1_6(image1)
    print('Image 1 Original:')
    obj1.print_image()
    obj1.rotate_image()
    print('Image 1 Rotated:')
    obj1.print_image()

    image2 = [[1,2,3], [4,5,6], [7,8,9]]
    obj2 = Question1_6(image2)
    print('Image 2 Original:')
    obj2.print_image()
    obj2.rotate_image()
    print('Image 2 Rotated:')
    obj2.print_image()

    image3 = [[1,2,3], [4,5,6], [7,8]]
    obj3 = Question1_6(image3)
    print('Image 3 Original:')
    obj3.print_image()
    obj3.rotate_image()
    print('Image 3 Rotated:')
    obj3.print_image()

    image4 = 7
    obj4 = Question1_6(image4)
    print('Image 4 Original:')
    obj4.print_image()
    obj4.rotate_image()
    print('Image 4 Rotated:')
    obj4.print_image()

    print('Complete.')