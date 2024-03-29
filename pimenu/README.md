PiMenu
======

This is a simple fullscreen menu system written in Python TKInter. It has been
developed with a Raspberry Pi Touchscreen in mind and is optimized for small
screens (320x240 is assumed).

The design is inspired by Windows 8's Metro design. Tiles are configured in
```../tmp.json```, they can either open new pages of tiles or execute the action
script ```pimenu.sh``` to execute arbitrary tasks.

On the Raspberry, install python-json if not present(it is normally in the core of python3):

    sudo apt-get install python3-json



The app can be started in fullscreen by passing ```fs``` as second parameter.

    ./pimenu.py "" fs


License
-------

Copyright (c) 2014-2017 Andreas Gohr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
