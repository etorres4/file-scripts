# Maintainer: Eric Torres <erictorres4@protonmail.com>
pkgname=file-scripts
pkgver=1.1.4
pkgrel=2
pkgdesc="Various scripts for performing file-related operations such as editing and deleting."
arch=(any)
license=(GPL3)
depends=(bash fd fzf mlocate python python-termcolor)
makedepends=(git)
makedepends=(git python-setuptools python-sphinx)
checkdepends=(python-hypothesis python-pytest)
source=("${pkgname}::git+file:///home/etorres/Projects/file-scripts")
install=$pkgname.install
sha256sums=('SKIP')

pkgver() {
    cd "${srcdir}/${pkgname}/bash"
    bash version.sh --print
}

package() {
    cd "${srcdir}/${pkgname}"

    for script in bash/bin/*; do
        install -Dm755 "$script" "$pkgdir/usr/bin/$(basename -s '.sh' "$script")"
    done

    for libfile in bash/*.sh; do
        install -Dm644 "$libfile" "$pkgdir/usr/share/file-scripts/$(basename "$libfile")"
    done

    # Install zsh completions
    for completion in zsh/*; do
        install -Dm644 "${completion}" "${pkgdir}/usr/share/zsh/site-functions/$(basename "$completion")"
    done
}

#check() {
#    pytest
#}
