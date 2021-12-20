# Maintainer: Eric Torres <erictorres4@protonmail.com>
pkgname=file-scripts
pkgver=0.9.0
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

    install -dm755 "${pkgdir}"/usr/{bin,share/zsh/{plugins/helper-scripts,site-functions}}

    for script in *.{py,sh}; do
        install -m755 "${script}" "${pkgdir}/usr/bin/${script%.*}"
    done

    ## Install /etc/config files
    #install -dm755 "${pkgdir}/etc/helper-scripts"
    #for config in config/*; do
    #    install -m644 "${config}" "${pkgdir}/etc/helper-scripts/${config##*/}"
    #done

    ## Install zsh completions
    #for completion in zsh/completions/*; do
    #    install -m644 "${completion}" "${pkgdir}/usr/share/zsh/site-functions/${plugin##*.}"
    #done

    ## Install zsh plugins
    #for plugin in zsh/plugins/*; do
    #    install -m644 "${plugin}" "${pkgdir}/usr/share/zsh/plugins/helper-scripts/${plugin##*/}"
    #done
}
