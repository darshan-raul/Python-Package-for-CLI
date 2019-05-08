# Python CLI for AWS

This package can be used to get a CLI interface for interacting with AWS services.

## Instructions to install

> pip install pyawscli

## Instructions to use:

> python -m pyawscli

## References

- https://dzone.com/articles/executable-package-pip-install
- https://python-packaging.readthedocs.io/en/latest/minimal.html

## Pypi uploading instructions:

```
sudo python -m pip install --upgrade pip setuptools wheel
sudo python -m pip install tqdm
sudo python -m pip install  --upgrade twine
```

- Create wheel file

```
python setup.py bdist_wheel
```

- Test in Local machine:
```
python -m pip install dist/<wheel name>
```

- Create .pypric file in home directory

```
[distutils] 
index-servers=pypi
[pypi] 
repository = https://upload.pypi.org/legacy/ 
username =<username>
```


- Upload to pypi:

```
python -m twine upload dist/*
```

> python setup.py register is depricated now no need to use it



# TODO/BUGFIXES:


- [ ] pip install on linux (version number error)
- [ ] avoid using python - m everytime to run the package (env/path variable)