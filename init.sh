#!/bin/bash
echo "----- RUST -----"
cargo run -p wrap_directory
echo "----- Python -----"
python3 ./python_file_generator/convert_dir_to_dict.py
python3 ./python_file_generator/main.py
echo "----- Complete -----"