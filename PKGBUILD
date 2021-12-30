# Maintainer: Eric Torres <erictorres4@protonmail.com>
pkgname=file-scripts
pkgver=0.9.2
pkgrel=0
pkgdesc="Various scripts for performing file-related operations such as editing and deleting."
arch=(any)
license=(GPL3)
depends=(fd fzf mlocate 'python>=3.7' python-termcolor)
makedepends=(python-hypothesis python-pytest python-setuptools python-sphinx)
source=("${pkgname}-${pkgver}.tar.gz")
sha256sums=('85ee18f00451c5bcaae18f23600afbbd621514c8fe0b8250c8191698c396c992')
sha512sums=('f5fd0244fef5800f3ae8b34633b412b451cb014eab3206f9f003c1e12d13b034f59c45646a519a9bb2f9342b406714831cdf87cf5656ff2c3605ed4f0fc57ff2')

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
