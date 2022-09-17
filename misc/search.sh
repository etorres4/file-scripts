# Utility functions and helpers for searching
DEFAULT_FD_OPTS=('--hidden' '--type' 'f' '--type' 'l' '--threads' "$(nproc)")

# Parameters:
# $1: directory
# $2-n: extra arguments
find_files() {
    if [[ -d "$1" ]]; then
        local directory="$1"
        shift
        fd "${DEFAULT_FD_OPTS[@]}" "$@" -- . "$directory"
    else
        fd "${DEFAULT_FD_OPTS[@]}" "$@"
    fi
}
