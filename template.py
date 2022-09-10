def main():
    import NDEM
    data = NDEM.Data("It's a template how it works.")
    print(data.string)
    data.image.show('Template')
    data.image.save('./template.png')

    date_from_image = NDEM.Data.from_image('./template.png')
    print('From image:', date_from_image.string)


if __name__ == '__main__':
    main()
