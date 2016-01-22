# c4bvim
This plugin is an alternative student plugin for use with [Code4Brownies](https://github.com/vtphan/Code4Brownies)
that allows students to submit in-class coding assignments to the instructor through Sublime Text 3. This plugin
contains the same functionality as the Sublime Text 3 plugin, but instead works with Vim.

## Installation

This plugin requires the Python requests library, which can be installed with 
pip. If you do not have pip, see [get-pip](https://pip.pypa.io/en/latest/installing). 
if you do have pip, run `pip install requests` in a terminal to install the library.

After installing requests, use your plugin manager of choice to install:

- [Pathogen](https://github.com/tpope/vim-pathogen)
  - `git clone https://github.com/egoddard/c4bvim ~/.vim/bundle/c4bvim`
- [Vundle](https://github.com/gmarik/vundle)
  - Add `Bundle 'https://github.com/egoddard/c4bvim'` to .vimrc
  - Run `:BundleInstall`
- [NeoBundle](https://github.com/Shougo/neobundle.vim)
  - Add `NeoBundle 'https://github.com/egoddard/c4bvim'` to .vimrc
  - Run `:NeoBundleInstall`
- [vim-plug](https://github.com/junegunn/vim-plug)
  - Add `Plug 'https://github.com/egoddard/c4bvim'` to .vimrc
  - Run `:PlugInstall`

## Setup

After installing the plugin, start vim and use the `:C4bSetInfo` command to set 
your username and server information. The syntax for the command is 
`:C4bSetInfo username server:port`. For example, if your username is 
jdoe and the server is http://127.0.0.1:4030, you would use the 
following command in vim:
```
:C4bSetInfo jdoe http://127.0.0.1:4030
```
To update the info, just rerun the above command with updated name and server/port.

## Usage

This plugin contains only the student functions (share, check points, set info, 
and get info).

To share the current buffer, use `:C4bShare`.

To get the current connection info, use `:C4bGetInfo` (See Setup for set info example).

To check your current points, use `:C4bPoints`.
