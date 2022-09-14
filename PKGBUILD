# Maintainer: Eric Torres <erictorres4@protonmail.com>
pkgname=file-scripts
pkgver=1.1.3
pkgrel=1
pkgdesc="Various scripts for performing file-related operations such as editing and deleting."
arch=(any)
license=(GPL3)
depends=(fd fzf mlocate python python-termcolor)
makedepends=(git python-setuptools python-sphinx)
checkdepends=(python-hypothesis python-pytest)
source=("${pkgname}::git+file:///home/etorres/Projects/file-scripts")
install=$pkgname.install
sha256sums=('SKIP')

pkgver() {
    cd "${srcdir}/${pkgname}"
    python setup.py --version
}

package() {
    cd "${srcdir}/${pkgname}"

    python setup.py build
    python setup.py install --root="$pkgdir/" --optimize=1

    ## Install zsh completions
    #for completion in zsh; do
    #    install -m644 "${completion}" "${pkgdir}/usr/share/zsh/site-functions/${plugin##*.}"
    #done
}

check() {
    pytest
}
