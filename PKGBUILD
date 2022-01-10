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
sha256sums=('e085eb0382f9025ea5d03abeb39148da7a97f40255a6beda79c7a066f8fc0696')
sha512sums=('82932d56c5fd828d4eaaaf6e3d59ac528c38efd23b3e5acdf9391a47bf53b357b492f751598bc23e5e1e503579e9b00704208277eff49dd7c524e7e2405633d9')

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
