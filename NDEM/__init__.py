import numpy as np
import pathlib as pl
from PIL import Image


class Data:
    @staticmethod
    def from_image(path, shape: tuple[int, int] | None = None):
        """
        It takes a path to an image, and returns a Data object

        :param path: The path to the image file
        :param shape: The shape of the image. If None, the shape will be the same as the image
        :type shape: tuple[int, int] | None
        :return: A Data object with the image and shape
        """
        path = pl.Path(path)
        image = Image.open(path).convert('L')

        if shape is None:
            shape = image.size[::-1]

        return Data(image, shape)

    def __init__(self, data: Image.Image | np.ndarray | str, shape: tuple[int, int] | None = None):
        """
        :param data: The data to be stored in the Image object
        :type data: Image.Image | np.ndarray | str
        :param shape: The shape of the image. If not specified, it will be determined from the data
        """
        self.__data = np.zeros((1, 0), dtype=int)
        self.__image = None
        self.__string = None
        self.__shape = shape
        if type(data) == str:
            self.__data = np.zeros((1, len(data)), dtype=int)
            for n, letter in enumerate(data):
                self[0, n] = ord(letter)
            self.data = self.data
        elif type(data) == np.array:
            self.data = np.copy(data)
        elif type(data) == Image.Image:
            self.data = np.asarray(data)

    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, shape):
        self.__shape = shape
        self.data = self.__data

    @property
    def string(self):
        return self.__string

    @property
    def image(self) -> Image.Image:
        return self.__image

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = np.array(value, dtype=np.uint8)

        if self.__shape is not None:
            self.__data = self.__data.reshape(self.__shape)

        self.__image = Image.fromarray(self.__data, mode='L')

        if not self.data.any():
            self.__string = ''
            return
        letters = []
        for letter in np.concatenate(self.__data):
            letters.append(chr(letter))
        self.__string = ''.join(letters)

    def __getitem__(self, item):
        return self.__data[item]

    def __setitem__(self, key, value):
        self.__data[key] = value

    def __str__(self):
        return str(self.__data)

    def __repr__(self):
        return f'{self.__class__}({self.string}, {self.shape})'
