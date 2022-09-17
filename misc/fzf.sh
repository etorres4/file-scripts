## FZF helpers

FZF_OPTS=('--select-1' '--exit-0')

run_fzf() {
    fzf "${FZF_OPTS[@]}" -- <<< "$@" || return 2
}
