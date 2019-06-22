#!/usr/local/env python3
# -*- coding: utf-8 -*-

import os
from pathlib import Path


user_colorschemes = {'ashen', 'coda', 'codepaper', 'colorzone',
                     'kaltex', 'mac_classic', 'abra', 'af',
                     'base', 'blazer', 'darkrobot', 'desertink',
                     'chroma', 'cobalt', 'cobalt2', 'contrastneed',
                     'cyberpunk', 'django', 'doriath', 'jellybeans', 'znake'}

colors_path = Path(Path.cwd(), 'colors')
all_colorschemes = {vimfile.stem for vimfile in colors_path.iterdir()}
shit_colorschemes = all_colorschemes - user_colorschemes

def del_colorschemes(path_to: Path, data_set: set) -> None:
    fmt = "{}/{}.vim"
    fmt_return = "removed files: {}"
    for data in data_set:
        candidate = fmt.format(path_to, data)
        if os.path.isfile(candidate):
            os.remove(candidate)
            print(fmt_return.format(candidate))


if __name__ == '__main__':
    del_colorschemes(colors_path, shit_colorschemes)

