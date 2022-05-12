import os
import pyperclip


class Literal:
    def __init__(self, string: str, type: str) -> None:
        """A Literal is a small object that contains the syntax string among others.

        It provides convenient ways to further use this string, e.g. paste it to clipboard,
        print to `stdout` or save to disk. You will not need to initialise `Literal` yourself.
        Rather, it will be returned to you by funtions like `syntax`.

        :param string: [description]
        :type string: str
        :param type: [description]
        :type type: str
        """
        self.string = string
        self.type = type

    def __str__(self) -> str:
        return self.string

    def print(self) -> str:
        return self.__str__()

    def raw(self) -> str:
        return self.string

    def clipboard(self) -> None:
        """This method will copy the syntax string to your clipboard."""
        pyperclip.copy(self.string)

    def save(self, path: str, overwrite: bool = False) -> None:
        """[summary]

        :param path: specifies the file path.
        :type path: str
        :param overwrite: If a file in `path`, exists, it will only be overwritten if
            `overwrite=True`, defaults to False
        :type overwrite: bool, optional
        :raises OSError: If `overwrite=False` but a file exists in this path, an
            OSError will be raised.
        """
        if not overwrite and os.path.isfile(path):
            raise OSError("File exists already and {overwrite=}. Select another filename or set `overwrite=True`.")
        with open(path, "w") as file:
            file.write(self.string)
        # TODO add option to append
