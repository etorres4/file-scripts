#!/usr/bin/env bash

MAJOR_VERSION=1
MINOR_VERSION=2
PATCH_VERSION=0

if [[ "$1" == '--print' ]]; then
	echo "${MAJOR_VERSION}.${MINOR_VERSION}.${PATCH_VERSION}"
fi
