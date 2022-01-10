# Maintainer: Eric Torres <erictorres4@protonmail.com>
pkgname=file-scripts
pkgver=1.0
pkgrel=0
pkgdesc="Various scripts for performing file-related operations such as editing and deleting."
arch=(any)
license=(GPL3)
depends=(fd fzf mlocate 'python>=3.7' python-termcolor)
makedepends=(python-hypothesis python-pytest python-setuptools python-sphinx)
source=("${pkgname}-${pkgver}.tar.gz")
sha256sums=('89ef58e7b7ff62914570e8747cf9a56d695e7da3e8d27655a6431c64b31d3eb6')
sha512sums=('f7eb56056f9de047b6a4e0531a44863e34e1beb3e620daf219807badefaed186036bc8d06dd102335915fe44ff06e1c132d159f38692043cf96d49649c4371b4')

package() {
    cd "${srcdir}/${pkgname}-${pkgver}"

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
