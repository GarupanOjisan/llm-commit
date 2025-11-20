class LlmCommit < Formula
  include Language::Python::Virtualenv

  desc "A CLI tool to generate commit messages using LLMs"
  homepage "https://github.com/GarupanOjisan/llm-commit"
  url "https://github.com/GarupanOjisan/llm-commit/archive/refs/tags/v0.1.0.tar.gz"
  sha256 "REPLACE_WITH_SHA256_OF_TARBALL"
  license "MIT"

  depends_on "python@3.12"

  def install
    virtualenv_install_with_resources
  end

  test do
    system "#{bin}/llm-commit", "--help"
  end
end
