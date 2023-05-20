#!/bin/bash

DIR="$(dirname "$(realpath $0)")"
APPDIR="$(cat "$DIR/appdir")"

python3 "$DIR/preload.py" "$1"
