#!/bin/bash
echo "----- CREATE DIRECTORY FROM FILE NAME -----"
cargo run -p wrap_directory
echo "----- Python -----"
python3 ./python_file_generator/convert_dir_to_dict.py
python3 ./python_file_generator/wrapper.py
echo "----- Complete -----"