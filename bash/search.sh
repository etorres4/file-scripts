# Utility functions and helpers for searching
DEFAULT_FD_OPTS=('--hidden' '--type' 'symlink' '--threads' "$(nproc)")

# Search and return a string with filenames delimited by \n
# Parameters:
# $1: directory
# $2-n: extra arguments
find_files() {
	if [[ -d "$1" ]]; then
		local directory="$1"
		shift
		fd "${DEFAULT_FD_OPTS[@]}" --type f "$@" -- . "$directory"
	else
		fd "${DEFAULT_FD_OPTS[@]}" --type f "$@"
	fi
}

# Search and return a string with filenames delimited by \n
# Parameters:
# $1: directory
# $2-n: extra arguments
find_directories() {
	if [[ -d "$1" ]]; then
		local directory="$1"
		shift
		fd "${DEFAULT_FD_OPTS[@]}" --type d "$@" -- . "$directory"
	else
		fd "${DEFAULT_FD_OPTS[@]}" --type d "$@"
	fi
}

# Search all files and directories, determine what type of files to search
# Parameters:
# $1: filetype (specific to fd's --type flag)
# $2: directory
# $3-n: extra arguments
find_specific() {
    local type_opt="$1"
    shift
	if [[ -d "$1" ]]; then
		local directory="$1"
		shift
		fd "${DEFAULT_FD_OPTS[@]}" --type "$type_opt" "$@" -- . "$directory"
	else
		fd "${DEFAULT_FD_OPTS[@]}" --type "$type_opt" "$@"
	fi
}
