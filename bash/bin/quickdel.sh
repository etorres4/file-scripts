#!/usr/bin/env bash

# Cleanup
set -e
trap 'exit 1' SIGINT

# ========== Source library ==========
#LIBDIR="/usr/share/file-scripts/"
LIBDIR="$HOME/Projects/file-scripts/misc"

for f in "$LIBDIR"/*.sh; do
    source "${f}"
done

# ========== Constants ==========
RED=$'\e[1;31m'
GREEN=$'\e[1;32m'
BLUE=$'\e[1;34m'
YELLOW=$'\e[1;33m'

# ========== Helper functions ==========
function help() {
cat << HELPMESSAGE
$(basename "$0") $MAJOR_VERSION.$MINOR_VERSION.$PATCH_VERSION

Usage: $(basename "$0") [-h] [-d] [-e] [-E ext] [-f] [-F] [-I] [-i] [-l] patterns [patterns ...]

positional arguments:
  patterns              file matching patterns

options:
  -h, --help            show this help message and exit
  -d, --directories-only
                        filter results to directories
  -e, --empty-only      filter results to empty files and directories
  -E ext, --extension ext
                        file extension
  -f, --files-only      filter results to files
  -F, --force-directory-delete
                        do not ignore non-empty directories, delete anyways
  -I, --no-ignore-vcs   do not ignore .gitignore
  -i, --no-ignore       do not ignore .gitignore and .fdignore
  -l, --links-only      filter results to symlinks
HELPMESSAGE
}

# $1 is the output string, $2 is the color
function color_output() {
    case "$2" in
        'red')
            printf "$RED%s\n" "$1"
        ;;
        'green')
            printf "$GREEN%s\n" "$1"
        ;;
        'blue')
            printf "$BLUE%s\n" "$1"
        ;;
        'yellow')
            printf "$YELLOW%s\n" "$1"
        ;;
    esac
}

# Color files blue and directories green
function color_path() {
    if [[ -f "$1" ]]; then
        color_output "$1" 'blue'
    elif [[ -f "$1" ]]; then
        color_output "$1" 'green'
    fi
}

while true; do
    case "${1}" in
        '-d'|'--directories-only')
            DIRECTORIES_ONLY=1
            shift
            continue
            ;;
        '-e'|'--empty-only')
            EMPTY_ONLY=1
            shift
            continue
            ;;
        '-e'|'--extension')
            EXT="${2}"
            case "${EXT}" in
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
        --extension=*)
            EXT="${1#*=}"
            case "${EXT}" in
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
        '-f'|'--files-only')
            FILES_ONLY=1
            shift
            continue
            ;;
        '-F'|'--force-directory-delete')
            FORCE_DIR_DELETE=1
            shift
            continue
            ;;
        '-i'|'--no-ignore-vcs')
            NO_IGNORE_VCS=1
            shift
            continue
            ;;
        '-I'|'--no-ignore')
            NO_IGNORE=1
            shift
            continue
            ;;
        '-l'|'--links-only')
            FILTER_SYMLINKS=1
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

echo 'Script not implemented'
exit 1

#for pattern in "$@"; do
#    files+=
#    exit
#done
