
<h2>Usage Description</h2> 

All files in assets can be generated based on `templates/sample*.json` scheme. Run `bash init.sh` from `python_file_generator` directory to automatically generated files based on the provided scheme.

<h3> Endpoints </h3>
<h4>

`/receiver`

</h4>

Files from `assets` will be served on the web server through the route ...`/receiver/?name=[filename].`

Open markdown `LIN-001_1024_27/Exercise.md` <br>

```
http://localhost:3000/receiver/`?name=LIN-001/LIN-001_1024/LIN-001_1024_27/Exercise.md
```

<h4>

`/tree`

</h4>

Display all courses from `index.html`.

<h4>

`/tree_raw`

</h4>

Display all courses in JSON format.