# Maintainer: Eric Torres <erictorres4@protonmail.com>
pkgname=file-scripts
pkgver=1.1.4
pkgrel=1
pkgdesc="Various scripts for performing file-related operations such as editing and deleting."
arch=(any)
license=(GPL3)
depends=(bash fd fzf mlocate python python-termcolor)
makedepends=(git)
#makedepends=(git python-setuptools python-sphinx)
#checkdepends=(python-hypothesis python-pytest)
source=("${pkgname}::git+file:///home/etorres/Projects/file-scripts")
install=$pkgname.install
sha256sums=('SKIP')

pkgver() {
    cd "${srcdir}/${pkgname}/bash"
    bash version.sh
}

package() {
    cd "${srcdir}/${pkgname}/bash"

    for script in bin/*; do
        install -Dm755 "$script" "$pkgdir/usr/bin/$(basename -s '.sh' "$script")"
    done

    for libfile in *.sh; do
        install -Dm644 "$libfile" "$pkgdir/usr/share/file-scripts/${libfile##*/}"
    done

    #python setup.py build
    #python setup.py install --root="$pkgdir/" --optimize=1

    ## Install zsh completions
    #for completion in zsh; do
    #    install -m644 "${completion}" "${pkgdir}/usr/share/zsh/site-functions/${plugin##*.}"
    #done
}

#check() {
#    pytest
#}
