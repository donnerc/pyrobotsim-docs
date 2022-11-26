
# PyRobotSim documentation

## Installing dependencies

The dependencies are managed by `poetry`, which can be installed with following
command:

```{bash}
curl -sSL https://install.python-poetry.org | python3 -
```

The dependencies can then be installed through

```{bash}
poetry install
```

## Build the documentation

## Activating the virtual environment

Most commands from `Makefile` require the `poetry` virtual environment to be
activated. The folloewing command has to be run in the project directory:

```bash
poetry shell
```

### Build the online documentation

To build the documentation and for live development server, use the following
command from the root folder of the project containing the `Makefile` :

```bash
make livehtml
```

### Build the LaTeX (PDF) documentation

To be able to generate the PDF, you must first install LaTeX on your system. On
a Linux system, you just have to issue the commands

```bash
sudo apt update
sudo apt-get install texlive-latex-extra texlive-lang-french texlive-fonts-recommended latexmk
```

To generate the PDF, issue the following command in project root _

```bash
make tmpdf
```

The PDF output is then output to the `build/latex/` folder.

## Live development (HTML preview)

### On a local machine

Then, to view the result, simply visit http://localhost:8000/ in the web
browser.

## Edit online with the gitpod.io cloud IDE

The Gitpod online IDE allows to have complete virtual machines on which to run
the Sphinx / LaTeX on which to run the Sphinx / LaTeX toolchain to write the
documentation of TM projects in computer science.

Here are the steps to follow:

1. Fork the https://github.com/informatiquecsud/sphinx-tm-template/ repository
   into your GitHub account.

2. Open your version of the repository on GitHub and, in the address bar of your
   browser, add `https://gitpod.io#` to the far left of the address of your
   GitHub repository. For this to work, you must have an account on the platform
   https://gitpod.io/.

3. In Gitpod, install the dependencies

4. You can then generate the HTML with

   ```bash
   make livehtml
   ```

5. To generate the PDF, simply run the following command in a terminal.

   ```bash
   make tmpdf
   ```

