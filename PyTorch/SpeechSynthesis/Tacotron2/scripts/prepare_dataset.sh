#!/usr/bin/env bash

set -e

DATADIR="mozilla-1"
ZIPARCHIVE="${DATADIR}.zip"
ENDPOINT="https://storage.yandexcloud.net/synthesis/$ZIPARCHIVE"

if [ ! -d "$DATADIR" ]; then
  echo "dataset is missing, unpacking ..."
  if [ ! -f "$ZIPARCHIVE" ]; then
    echo "dataset archive is missing, downloading ..."
    wget "$ENDPOINT"
  fi
  unzip "$ZIPARCHIVE"
fi