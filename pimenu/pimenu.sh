#!/bin/bash

DIR="$(dirname "$(dirname "$(realpath $0)")")"
APPDIR="$(cat "$DIR/appdir")"

function load {
	
	echo "[{\"label\": \"App Details\"},{\"name\": \"$1\", \"icon\": \"$DIR/apps/$1/icon-64.png\", \"website\": \"$(cat "$DIR/apps/$1/website" 2>/dev/null)\",\"description\": \"$DIR/apps/$1/description\", \"status\": \"($(cat "$DIR/status/$1"))\",\"color_sheme\":\"#0000ff\"}]" >$DIR/tmp.json
	
}

if [ ! -d "$DIR/preload/$APPDIR/$1" ]&&[ ! "$1" == "back" ]&&[ ! "$1" == ".reload" ] >/dev/null;then

	load "$1"
	exit 1
	
elif [ "$1" == "back" ];then

	"$DIR/pimenu/updateyaml" "$(dirname "$APPDIR")"
	echo "$(dirname "$APPDIR")" >"$DIR/appdir"

elif [ "$1" == ".reload" ];then

	"$DIR/pimenu/updateyaml" "$APPDIR"
	
else

	"$DIR/pimenu/updateyaml" "$APPDIR/$1"
	echo "$APPDIR/$1">"$DIR/appdir"

fi
