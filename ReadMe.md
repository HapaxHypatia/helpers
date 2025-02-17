Also requires torch to be installed, but there are no wheels available for latest python version.
Download and install from [source](https://github.com/pytorch/pytorch#get-the-pytorch-source)  as per these steps

1. pip install astunparse numpy ninja pyyaml setuptools cmake cffi typing_extensions future six requests dataclasses
2. git clone --recursive https://github.com/pytorch/pytorch
3. cd pytorch
4. python setup.py develop

This final installation step will take a long time