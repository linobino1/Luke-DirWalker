# Luke-DirWalker

Directory Structure to CSV

parses a directory structure like this:

```
├── root/
│   ├── A
│   │   ├── Abrahams, Jim
│   │   │   ├── 2008 - Meet the Spartans
│   │   ├── Akerman, Chantal
│   │   │   ├── 1975 - Je tu il elle
│   ├── B
│   │   ├── ...

```

to a CSV like this:

```
Director,Year,Title
Abrahams, Jim,2008,Meet the Spartans
Akerman, Chantal,1975,Je tu il elle
```

## Usage

```
python dirwalker.py --root path/to/root/dir --output path/to/output.csv --depth 2
```

`depth` is the number of subdirectories that need to be traversed to get to the director name. In the example above, the depth is 2.
