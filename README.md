# DTC-Database
A database of diagnostic trouble code descriptions.

There are currently 6665 unique codes in the database

## Format
The only available format at the moment is XML. In the future, CSV and JSON will be added

### XML
The XML format is as follows:
```
<codes>
    <code code="P1000">Example code</code>
    <code ...>...</code>
</codes>
```

## Errors
These descriptions are a combination of many databases and I cannot check for correctnesss in each one so some descriptions may be malformed. If you happen to find an error, please submit an issue or pull request.
