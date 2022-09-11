def main():
    import NDEM

    # Creates an instance of Data class with the encoded string "It's a template how it works.
    # Height and width of image of the instance is equal to 4 and 7 respectively"
    data = NDEM.Data("It's a template how it works", (4, 7))

    # Prints: It's a template how it works.
    print(data.string)

    # Shows the string encoded in an image
    data.image.show('Template')

    # Saves the image with name template.png
    data.image.save('./template.png')

    # Creates an instance of Data class with the string encoded in an image (keeps the shape of the image)
    data_from_image = NDEM.Data.from_image('./template.png')

    # Prints: From image: | and decoded data from the image
    print('From image:', data_from_image.string)


if __name__ == '__main__':
    main()
