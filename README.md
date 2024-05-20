
<h2>Usage Description</h2> 

All files in assets can be generated based on files in `wrap_input`.  Run `bash init.sh` in your terminal from `root` directory to automatically generated JSON scheme in `templates/from_pyvert.json`. All files, then, are designated to their directory based on the following convention: `[course_name: ABC-123]_[skillset: u32]_[skill: u32]_filename.md`.

Run `bash start.sh` in your terminal from `root` directory to start the server.

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