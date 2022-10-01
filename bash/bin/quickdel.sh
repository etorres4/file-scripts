#!/usr/bin/env bash

# Cleanup
set -e
trap 'exit 1' SIGINT

# ========== Source library ==========
LIBDIR="/usr/share/file-scripts/"

for f in "$LIBDIR"/*.sh; do
    source "${f}"
done

# ========== Constants ==========
RED=$'\e[1;31m'
GREEN=$'\e[1;32m'
BLUE=$'\e[1;34m'
YELLOW=$'\e[1;33m'
WHITE_BOLD=$'\e[1;37m'
RESET=$'\e[0;0m'

declare -a extra_fd_opts
declare typeopt='file'

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
        'white')
            printf "$WHITE_BOLD%s\n" "$1"
            ;;
        'reset')
            printf "$RESET%s\n" "$1"
            ;;
    esac
}

# Color files blue and directories green
function color_path() {
    if [[ -f "$1" ]]; then
        color_output "$1" 'blue'
    elif [[ -d "$1" ]]; then
        color_output "$1" 'green'
    fi
}

# Delete path using correct command
# Parameters:
#   - $1: path
#   - $2: force delete boolean flag
function delete() {
    exit 1
}

while true; do
    case "${1}" in
        '-d' | '--directories-only')
            typeopt='directory'
            shift
            continue
            ;;
        '-e' | '--empty-only')
            typeopt='empty'
            shift
            continue
            ;;
        '-E' | '--extension')
            EXT="${2}"
            case "${EXT}" in
                "")
                    exit 1
                    ;;
                -*)
                    exit 1
                    ;;
            esac
            extra_fd_opts+=('--extension' "$EXT")
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
            extra_fd_opts+=('--extension' "$EXT")
            shift
            continue
            ;;
        '-f' | '--files-only')
            typeopt='file'
            shift
            continue
            ;;
        '-F' | '--force-directory-delete')
            rm_force='--force'
            shift
            continue
            ;;
        '-i' | '--no-ignore-vcs')
            extra_fd_opts+=('--no-ignore-vcs')
            shift
            continue
            ;;
        '-I' | '--no-ignore')
            extra_fd_opts+=('--no-ignore')
            shift
            continue
            ;;
        '-l' | '--links-only')
            typeopt='symlink'
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

# Interpret options
if [[ -z "$*" ]]; then
    echo 'Please enter patterns of filenames to delete'
    exit 1
fi

declare -a files pattern_results

for pattern in "$@"; do
    readarray -d $'\n' -t pattern_results <<< "$(find_specific "$typeopt" "$pattern" "${extra_fd_opts[@]}")"
    files+=("${pattern_results[@]}")
done

# If nothing was found
if [[ -z "${files[*]}" ]]; then
    color_output 'No files found, exiting' 'yellow'
    exit 1
fi

# Sort list of paths before printing
readarray -t paths < <(printf '%s\n' "${files[@]}" | sort --unique)

# Print list of files found matching criteria
i=1
for p in "${paths[@]}"; do
    printf '%s. %s\n' "$(color_output $i 'white')" "$(color_path "$p")"
    i=$((i + 1))
done

# Padding between files and prompt
#color_output '' reset

read -r -n 1 -p 'Would you like to delete these files? [y/N]: ' user_response
# Padding between prompt and output
echo ''

if [[ "$user_response" =~ (y|Y) ]]; then
    for p in "${paths[@]}"; do
        if [[ -d "$p" ]]; then
            rm --recursive "$rm_force" --verbose -- "$p" || printf '%s %s\n' "$(color_output "Unable to remove path:" 'red')" "$(color_path "$p")"
        else
            rm "$rm_force" --verbose -- "$p" || printf '%s %s\n' "$(color_output "Unable to remove path:" 'red')" "$(color_path "$p")"
        fi
    done
fi
