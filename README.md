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

[Tutorial 1 - Intro](http://htmlpreview.github.com/?https://github.com/tobiashofmann88/python_for_biologists/blob/master/tutorials/html_compiled_tutorials/tutorial_1.html)

[Tutorial 2 - Phylogenetics](http://htmlpreview.github.com/?https://github.com/tobiashofmann88/python_for_biologists/blob/master/tutorials/html_compiled_tutorials/tutorial_2.html)

[Tutorial 3 - Data Science](http://htmlpreview.github.com/?https://github.com/tobiashofmann88/python_for_biologists/blob/master/tutorials/html_compiled_tutorials/tutorial_3.html)