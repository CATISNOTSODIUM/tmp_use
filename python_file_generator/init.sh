#!/bin/bash
set -euo pipefail

if [ -d "../assets" ]; then
    rm -r "../assets/"*
fi

python3 main.py