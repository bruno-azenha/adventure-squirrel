Hello all!

To start, my code is using the readchar package to deal with key pressed
you can find it here:

https://pypi.python.org/pypi/readchar/0.7

To install it, if you don't have it already, you'll need pip
you can get it with on Ubuntu.

$ sudo apt-get install python-pip

It is a very useful package installer for python that is used for a lot 
of libraries to streamline the installation process.

---------------------
What I've done so far
---------------------

- Created another file named useful.py where I plan to store useful 
  functions that we write.

- Tried to better guide the processes of create a game.

- Added another file named GameStory.py where I am storing all of the
  classes for the story creation mode in order to get some better
  organization all around.

- On the useful.py file, created a function formatLinebreak(string,[Threshold])
  that takes in a string and breaks it in a multiple line string if it is too
  big. Threshhold defaults to 70.

- Now it runs but still on a very poor state, only CREATE ROOM work and
  actually editing the connections does nothing

- It is a MUST to create a function in useful.py to standardize the prompt
  making of the user. Right now it's all around the place, with newlines in
  random places and such thinks.


#-------------------------------------------#
# We should create a Makefile to do all of  #
# the requirements for our program to work. #
#-------------------------------------------#

Possible problems:

- There might be a compatibility issue with the function I'm using to clear
  the screen with Windows. It's  just a matter of search and replace. Let me
  know if it breaks! ;)
