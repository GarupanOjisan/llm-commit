#!/bin/bash

echo "Installing llm-commit..."

# Check if python3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is not installed."
    exit 1
fi

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "Error: pip3 is not installed."
    exit 1
fi

# Install the package
pip3 install .

if [ $? -eq 0 ]; then
    echo "Successfully installed llm-commit!"
    echo "You can now run 'llm-commit' in your terminal."
else
    echo "Installation failed."
    exit 1
fi
