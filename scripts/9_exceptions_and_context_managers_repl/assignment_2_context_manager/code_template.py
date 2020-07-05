import os


class cd:
    # your code here
    def __init__(self, path):
        pass
    #
    #     if not os.path.isdir(path):
    #         raise ValueError(f'{path} does not exists or not a dir')
    #
    #     self._path = path
    #     self._prev_path = os.getcwd()
    #
    # def __enter__(self):
    #     print(f'Change current dir to {self._path}')
    #     os.chdir(self._path)
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     print(f'Change current dir to {self._prev_path}')
    #     os.chdir(self._prev_path)


if __name__ == '__main__':
    with cd('.') as cm:
        print(f'I am in {os.getcwd()}')