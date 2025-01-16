# Conway's Game of Life

This is the a little Conway's Game of Life implemented on Python and QtPY.

## Requirements ❗️

- pip
- Python


First, make sure you have Python and pip installed on your system.
Next, navigate to your project directory where the requirements.txt file is located.

It is recommended to create a virtual environment before installing the requirements:

```bash
python -m venv venv
```

Activate the virtual environment:
- On Windows:
```bash
venv\Scripts\activate
```

Now, install the requirements with pip:
```bash
pip install -r requirements.txt
```
This command will install all the dependencies listed in the requirements.txt file.

Finally, run the app executing this command
```bash
python conway_gui.py
```

Remember to set up values properly before pressing "Start Game"
* Rows: Number of rows for the matrix.
* Columns: Number of columns for the matrix.
* Generations: Number of generatios used to refresh the matrix.
* Probability: Probability of alive cells in matrix.

## Project Structure 📦

```bash
conway/
├── conway.py
├── conway_gui.py
├── custom_dialog.py
├── infinity.png
├── readme.md
├── requirements.txt
└── worker.py
```
## Notes
This is a basic implementation of the Conway's Game of Life.
There is room for future features. 
Stick around for further updates!