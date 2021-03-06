# Webserver Files Discoverer

WFD is a Python discovery tool to scan a domain using a list of supposedly present files

## Requirements
    - python3.5+
    - python-requests

## Usage

    > ./files-discoverer.py [http://|https://][domain] [files_lists URLs, separated by a whitespace]

## Example

    > ./files-discoverer.py http://mynonexisting.domain.org https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web_Content/Common_PHP_Filenames.txt
    
## License

```
Webserver files discoverer
Copyright (C) 2017 lp1.eu

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
```