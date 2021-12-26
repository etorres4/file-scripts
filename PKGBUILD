# Maintainer: Eric Torres <erictorres4@protonmail.com>
pkgname=file-scripts
pkgver=0.9.2
pkgrel=0
pkgdesc="Various scripts for performing file-related operations such as editing and deleting."
arch=(any)
license=(GPL3)
depends=(fd fzf python)
makedepends=(git)
source=("${pkgname}::git+file:///home/etorres/Projects/file-scripts")
sha256sums=('SKIP')
sha512sums=('SKIP')

pkgver() {
    cd "$srcdir/${pkgname}"
	printf "%s" "$(git describe --long | sed 's/\([^-]*-\)g/r\1/;s/-/./g')"
}

package() {
    cd "${srcdir}/${pkgname}"

    python setup.py build
    python setup.py --root="$pkgdir" install

    ## Install zsh completions
    #for completion in zsh; do
    #    install -m644 "${completion}" "${pkgdir}/usr/share/zsh/site-functions/${plugin##*.}"
    #done
}

check() {
    pytest
}
