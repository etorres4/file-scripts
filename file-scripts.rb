class FileScripts < Formula
  desc "Various scripts for performing file-related operations"
  homepage "https://github.com/etorres4/file-scripts"
  url "https://github.com/etorres4/file-scripts", :using => :git
  version "1.2.0"
  sha256 "fad7da96c72c8bef81f3ec6a2d1cb13b09fb44e084f98b05ba3a7dfd8b41ae12"

  depends_on "fd"
  depends_on "fzf"
  #depends_on "python@3.10"

  def install
    system Formula["python@3.10"].opt_bin/"python3", *Language::Python.setup_install_args(prefix)
    system 

    # Install completions to zsh/site-functions
    zsh_completion.install Dir["zsh/_*"]
  end
end
