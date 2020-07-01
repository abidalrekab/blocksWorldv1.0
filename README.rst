Copyright (c) 2020 Mohamed Abidalrekab, Dan Petre

The MIT License (MIT)

About This Project
##################

BlocksWorld is a tool for generating simple test images.

Core features
=============

* generate simple test images that contains many adjacent polygons  
* overlapped objects
* can be scaled, Rotated, and translated.
Questions
=========

* How Can images be generated?  

Answer : run RunMe.py with aproperiate settings:
    - the number of images you want [0-100000]
    - whether you want to not allow overlap between objects ( OverlapRemove = False/True ) 
    - is there gap between objects or not.
    - the number of objects in each image [3-10]
    - choose a set of colors that gonna be used

* How can I find where vertices position for every object is saved?  

Answer : when you active Save(data, jsonfile), every generated image going to have another file.json or file.txt assossaited with it. check that file, you will find all info.  

* Does this code generate interpretable images - something like car, a house, boat, etc... - ?  

Answer : No. if you want that capability please check BlocksWorldv2.0\

Supported platforms
===================

* Ubuntu 16.04, Python 3.5+

Might work on other configurations however at this time the focus will be on a single platform until the project matures a bit.

Build from source prerequisites
===============================

* Python 3.5+

.. code-block:: bash

    $ sudo apt install python3-pip
    $ sudo apt install python3-setuptools
    $ pip3 install wheel

Similarly, for those who like to experiment:

* Python 2.7+

.. code-block:: bash

    $ sudo apt install python-setuptools
    $ sudo apt install python-pip
    $ pip install wheel

Build wheel:

`./build.sh`.

Install locally built wheel:

`$ pip install --user dist/*`

or, if your pip doesn't automatically use python3:

`$ python3 -m pip install --user dist/*`

Notice the use of the `--user` option. You can install system wide using `sudo` but the project is still in very early stages so installing as user can keep your system files clean(er).

Resources
=========

* Website:
* Code: https://github.com/abidalrekab/blocksWorldv1.0/ <https://github.com/takanokage/blocksWorldv1.0>`_
* Documentation: Not yet written
* Support: email us at moh29@pdx.edu
* License: `The MIT license <https://opensource.org/licenses/MIT>`_
