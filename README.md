# Glare Detection App

This flask app purpose is to return a boolean of whether their is glare in an image given the image metadata.

To install dependencies run:
```
pip install -r requirements.txt
```

The app accepts metadata of images in the following format:

- latitude: a float between -90 to 90 that shows the latitude in which the image was taken
- longitude: a float between -180 to 180 that shows the longitude in which the image was taken
- epoch: Linux epoch in second
- orientation: a float between -180 to 180 the east-ward orientation of car travel from true north. 0 means north. 90 is east and -90 is west


The app has a graphical user interface that can be accessed from any web browser. First, change current directory to project directory and run:

```
cd /project/directory/
python app.py
```

I f you want to use the GUI, use any browser to go to:
```
http://localhost:5000/
```
To run the test for a single image:

```
python single_request latitude longitude epoch orientation
```

Or use a web browser to send a request in the form:
```
http://localhost:5000/<latitude>/<longitude>/<epoch>/<orientation>
```
To run the test for multiple images in a csv:

```
python multiple_requests csv_file
```
Results will be saved to `data_with_responses.csv`.

The code has error handling functionality and won't accept invalid input ranges or types.
