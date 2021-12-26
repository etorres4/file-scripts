class HelperScripts < Formula
  desc "Various scripts for performing file-related operations such as editing and deleting"
  homepage "https://github.com/etorres4/helper-scripts"
  url "https://github.com/etorres4/file-scripts",
    :using => :git
  sha256 "7b6c3f363e3b34787765b5975d87f861a19eeda278612cbf8c5176e3e2732cd9"
  version "0.9.2"

  # No build dependencies
  bottle :unneeded

  def install
    #bin.install "ddusb.py" => "ddusb"
    #bin.install "fless.sh" => "fless"
    #bin.install "lsgroups.sh" => "lsgroups"
    #bin.install "lsusers.sh" => "lsusers"

    # Install completions to zsh/site-functions
    zsh_completion.install Dir["zsh/completions/_*"]
  end
end
