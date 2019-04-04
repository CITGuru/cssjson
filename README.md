# CSSJSON :rocket:

A Python scripts that converts css to json. I usually use this when I do web scrapping and I need to scrape something from css using classnames or ids.

# Installation

## GitHub

```bash
$ git clone https://github.com/CITGuru/cssjson.git
$ cd cssjson
$ python setup.py install
```

## PyPI

```bash
$ pip install cssjson
```

# Usage

```python

from cssjson import toJSON, toCSS

json = toJSON("example.css", path=True)
print(json)
css = toCSS(json)
print(css)

```

# Methods

## toJSON (text, path, url)

Converts css to json and can either be a text, file or url.

### Text

```python 
print(toJSON(".a{background:yellow}")
```

### Path

```python 
print(toJSON("example.css", path=True)
```

### Url

```python 
print(toJSON("https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css", url=True)
```

## toCSS (dict)

Converts json serialized css to css.

```python
print(toCSS({"rules":{}}))
```

# Contribution

You can contribute by sending a PR.

# Author

Oyetoke Toby (oyetoketoby80@gmail.com)

