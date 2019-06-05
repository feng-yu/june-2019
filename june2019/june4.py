"""
[hard]
Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2.
subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1.
subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system.
For example, in the second example above, the longest absolute path is
"dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format,
return the length of the longest absolute path to a file in the abstracted file system.
If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
"""

def find_longest_file_path_length(s):
    longest_file_path_length = 0
    file_list = []
    root_indics = s.find('\n\t')
    if root_indics == -1:
        return longest_file_path_length
    else:
        root_dir = s[:root_indics]
        s = s[root_indics:]

    dot_indics = s.find('.')
    while dot_indics != -1:
        file_end_indics = s.find('\n\t', dot_indics)
        if file_end_indics != -1:
            file_path = s[:file_end_indics]
            s = s[file_end_indics:]
            dot_indics = s.find('.')
        else:
            file_path = s
            dot_indics = -1
        file_list.append(file_path)
    for i in range(len(file_list)):
        file_path_length = len(root_dir + find_file_path(file_list[i]))
        if file_path_length > longest_file_path_length:
            longest_file_path_length = file_path_length
    return longest_file_path_length

def find_file_path(s):
    """s in the format like: \n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext """
    last_t_indics = s.rfind('\t')
    file_name = s[last_t_indics+1:]
    s = s[:last_t_indics+1]
    s = s.replace('\n\t', '/')
    while s.startswith('/\t'):
        s = s[s.find('/', 1):]
    s = s.replace('\t', '')
    return s + file_name

s = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
print(find_longest_file_path_length(s))
