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
sha512sums=('904507b13c8b300afabb6ec3661cd500e29916e7184789a3e791d928054d3300a9cd14b3d94b060795e5e6baf4612b1c5fb37dda0bc1b5af17a32361ca3be33f')

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
