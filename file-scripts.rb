class FileScripts < Formula
  desc "Various scripts for performing file-related operations such as editing and deleting"
  homepage "https://github.com/etorres4/file-scripts"
  url "https://github.com/etorres4/file-scripts",
    :using => :git
  version "0.9.2"

  depends_on "python@3.10"
  depends_on "fd"
  depends_on "fzf"

  def install
    system Formula["python@3.10"].opt_bin/"python3", *Language::Python.setup_install_args(prefix)

    # Install completions to zsh/site-functions
    zsh_completion.install Dir["zsh/_*"]
  end
end
