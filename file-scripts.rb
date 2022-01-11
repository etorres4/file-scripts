class FileScripts < Formula
  desc "Various scripts for performing file-related operations"
  homepage "https://github.com/etorres4/file-scripts"
  url "https://github.com/etorres4/file-scripts", :using => :git
  version "1.0.1"
  sha256 "1124f0fabb45341a0daf6ca1f6fc9f7aa13bc921bd2fe25bd6e9744829c7fc96"

  depends_on "fd"
  depends_on "fzf"
  depends_on "python@3.10"

  def install
    system Formula["python@3.10"].opt_bin/"python3", *Language::Python.setup_install_args(prefix)

    # Install completions to zsh/site-functions
    zsh_completion.install Dir["zsh/_*"]
  end
end
