# Maintainer: Eric Torres <erictorres4@protonmail.com>
pkgname=file-scripts
pkgver=2.0.0
pkgrel=1
pkgdesc="Various scripts for performing file-related operations such as editing and deleting."
arch=(any)
license=(GPL3)
depends=(bash fd fzf)
makedepends=(git)
source=("${pkgname}::git+file:///home/etorres/Projects/file-scripts")
install=$pkgname.install
sha256sums=('SKIP')

package() {
    cd "${srcdir}/${pkgname}"

    for script in bin/*; do
        install -Dm755 "$script" "$pkgdir/usr/bin/$(basename "$script")"
    done

    # Install zsh completions
    for completion in zsh/*; do
        install -Dm644 "${completion}" "${pkgdir}/usr/share/zsh/site-functions/$(basename "$completion")"
    done
}
