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
sha256sums=('1124f0fabb45341a0daf6ca1f6fc9f7aa13bc921bd2fe25bd6e9744829c7fc96')
sha256sums=('9995199d336df02f37af4a5600dfb969a85c64ce54644d95151b4fc1c9b9338940724efa6a037ccc96e3086656cebe7315be7d85de7fb0212aace0a701e32467')

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
