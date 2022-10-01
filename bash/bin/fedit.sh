#!/usr/bin/env bash

# Cleanup
set -e
trap 'exit 1' SIGINT

# Source library
LIBDIR="/usr/share/file-scripts/"

for f in "$LIBDIR"/*.sh; do
	source "${f}"
done

BOOT_DIR='/boot'
ETC_DIR='/etc'

# Helper functions
function help() {
	cat <<HELPMESSAGE
$(basename "$0") $MAJOR_VERSION.$MINOR_VERSION.$PATCH_VERSION

Usage: $(basename "$0") [-h|--help] [options] [patterns]

Options
  -h, --help            show this help message and exit
  -b, --boot            edit a file in /boot
  -d DIR, --dir DIR     edit a file in a given directory
  -E, --etc             edit a file in /etc
  -I, --no-ignore       do not respect .(git|fd)ignore files
  -i, --no-ignore-vcs   do not respect .gitignore files

Note that this script uses EDITOR to select an editor
HELPMESSAGE
}

while true; do
	case "${1}" in
	'-b' | '--boot')
		EDIT_BOOT=1
		shift
		continue
		;;
	'-d' | '--dir')
		DIR="${2}"
		case "${DIR}" in
		"")
			exit 1
			;;
		-*)
			exit 1
			;;
		esac
		shift 2
		continue
		;;
	--dir=*)
		DIR="${1#*=}"
		case "${DIR}" in
		"")
			exit 1
			;;
		-*)
			exit 1
			;;
		esac
		shift
		continue
		;;
	'-E' | '--etc')
		EDIT_ETC=1
		shift
		continue
		;;
	'-i' | '--no-ignore-vcs')
		NO_IGNORE_VCS=1
		shift
		continue
		;;
	'-I' | '--no-ignore')
		NO_IGNORE=1
		shift
		continue
		;;
	'-h' | '--help')
		help
		exit
		;;
	--)
		shift
		break
		;;
	-*)
		printf '%s\n' "Unknown option: ${1}" >&2
		exit 1
		;;
	*)
		break
		;;
	esac
done

# Handle -b and -E, they are mutually exclusive
if [[ -n $EDIT_BOOT && -z $EDIT_ETC ]]; then
	DIR="$BOOT_DIR"
elif [[ -z $EDIT_BOOT && -n $EDIT_ETC ]]; then
	DIR="$ETC_DIR"
elif [[ -n $EDIT_BOOT && -n $EDIT_ETC ]]; then
	printf '%s\n' 'Select either --boot or --etc, not both'
	exit 1
elif [[ -z $DIR ]]; then
	DIR='.'
fi

# Handle extra options
declare -a extra_opts

if [[ -n $NO_IGNORE ]]; then
	extra_opts+=('--no-ignore')
elif [[ -n $NO_IGNORE_VCS ]]; then
	extra_opts+=('--no-ignore-vcs')
fi

files="$(find_files $DIR "${extra_opts[@]}")"
selected_file="$(run_fzf "$files")"

if [[ -w "${selected_file}" ]]; then
	"$EDITOR" "$selected_file"
else
	sudo --edit "$selected_file"
fi
