# Code for the Coffee Maker Mi5 module

All the source code used is contained in a jupyter (ipython) notebook file.

## Setup

Certain parts of the code will only run on a raspberry pi, specifically:

* The servo controlling code, which uses pigpio
* The camera code, which uses picamera

To install elsewhere, those dependencies should be removed from requirements.txt,
and the camera code modified to use a webcam.

Assuming a rpi is used, install:

* python3-pigpio
* python3-virtualenv
* ipython3
* ipython3-notebook
* virtualenv
* python3-dev
* libzmq-dev

Then:

Create the env and activate it:

    $ mkdir mi5_env
    $ virtualenv -p python3 mi5_env/
    $ source mi5_env/bin/activate
    $ pip install --upgrade setuptools pip
    $ pip install numpy

(Important: All that follows assumes the env is activated!)

Install opencv:

    $ wget https://github.com/Itseez/opencv/archive/3.1.0.zip
    $ unzip 3.1.0.zip
    $ cd opencv-3.1.0
    $ mkdir build
    $ cd build
    $ cmake ..
    $ make -j3
    $ sudo make install
    $ cd

Install pigpio inside the env:

    $ pip install git+https://github.com/joan2937/pigpio.git

Install other stuff:

    $ pip install jupyter
    $ pip install picamera

The computer vision outputs temporary pictures for debugging so that
they can be viewed on a web browser.
We need an http server for that:

    $ sudo su
    # apt install lighttpd
    # mkdir /var/www/images/
    # usermod -a -G www-data pi

Edit /etc/lighttpd/lighttpd.conf and make the documentroot /var/www
(it's /var/www/html by default).

    # systemctl enable lighttpd
    # systemctl start lighttpd

Log out, log in again (to get the new group), and re-activate the env:
    $ source mi5_env/bin/activate

## Usage

You can now start the notebook:

    $ jupyter notebook --ip=0.0.0.0 --port=8890

Access it by pointing your browser at the pi's IP Address, port 8890, eg:

<http://192.168.192.71:8890>

To run headless, you can remove or comment out the test cells,
convert the notebook to a .py file and run it directly:

    $ jupyter nbconvert --to python CoffeeMaker.ipynb
    $ python CoffeeMaker.py

For pigpio, the pigpio daemon must be running in the background:

    # sudo pigpiod -s 1

