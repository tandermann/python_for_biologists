# python_for_biologists

To run the tutorials of this course, you will need to have python3 installed. The easiest way to install python on any platforms is via the conda installation manager. This will also allow you to install spyder, which is a great Python editor (similar to RStudio for R).

Install the Python3 version of miniconda: https://docs.conda.io/en/latest/miniconda.html

Once miniconda or anaconda is installed you can access it via the command line. If you are using macos or linux you can just open your Terminal app. If you are a windows user you need to use the specific conda powershell that was installed with your miniconda installation (in case you can’t find it after installing miniconda, it could be that you have to download all of anaconda instead, which you can do here: https://www.anaconda.com/products/individual).

Once you are in your terminal or conda powershell execute the following command:

`conda create -n ggbc_course python` (press y when you are asked to do so)

This will create a new environment named ‘ggbc_course’ where python is installed. You can connect to it using:

`conda activate ggbc_course`

and disconnect from it with:

`conda deactivate`

When connected to the virutal environment you can run python by just typing `python` into the command line.

To install **spyder** (python editor) run the following command, while connected to the ggbc_course environment:

`conda install spyder`

Once it's finished, open spyder by just typing `spyder` into your command line.



# Tutorials

[Tutorial 1 - Python introduction](https://github.com/tobiashofmann88/python_for_biologists/blob/master/tutorials/tutorial_1.ipynb)

[Tutorial 2 - Reading data and plotting](https://github.com/tobiashofmann88/python_for_biologists/blob/master/tutorials/tutorial_2.ipynb)

[Tutorial 3 - Functions and creating python programs (on the example of DNA data processing)](https://github.com/tobiashofmann88/python_for_biologists/blob/master/tutorials/tutorial_3.ipynb)


In case the tutorial links don't work or don't properly compile, you can open the tutorials as [pre-compiled pdf versions here](https://github.com/tobiashofmann88/python_for_biologists/tree/master/tutorials/pdf_compiled) (not as pretty, but reliable to work).