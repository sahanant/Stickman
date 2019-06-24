array_dir=$TASK_DIR/arrays

rm -rf arrays
mkdir arrays

python3 convert_to_array.py -l 'animation' -a 'array_dir'

