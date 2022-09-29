#!/usr/bin/env bash

# Cleanup
set -e
trap 'exit 1' SIGINT

# Source library
LIBDIR="/usr/share/file-scripts/"

for f in "$LIBDIR"/*.sh; do
    source "${f}"
done

DEFAULT_TEMPLATE_DIR="$HOME/Templates"

# Helper functions
function help() {
cat << HELPMESSAGE
$(basename "$0") $MAJOR_VERSION.$MINOR_VERSION.$PATCH_VERSION

Usage: $(basename "$0") [-h] [-d DIR] [-f] dest

Positional arguments:
  dest

options:
  -h, --help            show this help message and exit
  -d DIR, --template-dir DIR
                        choose a template directory (default: ~/Templates)
  -f, --force           overwrite dest if it exists
HELPMESSAGE
}

while true; do
    case "${1}" in
        '-d'|'--dir')
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
        '-f'|'--force')
            FORCE_OVERWRITE='--force'
            shift
            continue
            ;;
        '-h'|'--help')
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

# If directory wasn't overridden
if [[ -z "$DIR" ]]; then
    DIR="$DEFAULT_TEMPLATE_DIR"
fi

# If no target specified
if [[ -z "$1" ]]; then
    printf '%s\n' 'Please specify target name'
    exit 1
fi

# Check if default template directory exists
if ! [[ -d "$DIR" ]]; then
    printf '%s\n' "Template directory doesn't exist, exiting."
    exit 2
fi

files="$(find_files "$DIR")"
selected_file="$(run_fzf "$files")"

# Check if target exists
if [[ -f "$1" && -z "$FORCE_OVERWRITE" ]]; then
    printf '%s\n' 'File already exists, exiting'
    exit 1
elif [[ -f "$1" && -n "$FORCE_OVERWRITE" ]]; then
    cp --verbose --force -- "$selected_file" "$1"
else
    cp --verbose -- "$selected_file" "$1"
fi
