# NDEM

**NDEM** or **Nazar0360's data encoding method** is my method of encoding data.

## Advantages of NDEM and its disadvantages

Advantages:

* can encode a string to an image, and you can store it in this form
* can encode an image to a string, and you can store it in this form
* encoded image or string can be decoded
* you can use it to protect data from regular users (programmers can easily decode it)

Disadvantages:

* image can only be black and white (NDEM can take color image, but it will be interpreted as black and white)
* can encode only 256 first unicode characters
* slow (but not too much)
* and many more

## How it works

NDEM converts each character to a black and white pixel with decimal value of the symbol. That's why it can encode
only 256 first unicode characters (minimal value of a pixel is 0, maximal value of a pixel is 255).

## Documentation?

Class constructor takes two arguments:

```python
Data(data, shape)
```

* `data`: can be an image, a string or a numpy array
* `shape`: tuple with height (integer) and width (integer) of image or None. If None, height of image will be 1

You can also create an instance of Data class using `Data.from_image`. It takes two arguments:

```python
Data.from_image(path, shape)
```

* `path`: The path to the image file
* `shape`: The shape of the image. If None, the shape will be the same as the image

Properties

```python
Data.shape
```

* shape: returns height and width of image. Can be changed

```python
Data.string
```

* string: returns decoded string

```python
Data.image
```

* image: returns decoded image

```python
Data.data
```

* string: returns data of an instance. Can be changed

### Template

```python
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
```