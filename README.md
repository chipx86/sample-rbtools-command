Sample RBTools Command
======================

This repository contains the basis for a sample RBTools command. If you
want to create your own, clone this repository and modify it appropriately.

You will want to do the following:

* Rename the `mycommand` directory to a suitable Python module name for your
  command.

* Edit the `command.py` in that directory, rename the class, fill in fields, and
  begin writing your own logic.

* Edit `setup.py` and change the name, entrypoint, and anything else you need. Make
  sure the entrypoint points to your new class.
