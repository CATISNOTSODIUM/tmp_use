
<h2>Usage Description</h2> 
This program serves as a directory parser to leverage the task of allocating files manually.  All files in assets can be generated based on markdown files in `wrap_input`.  Before starting the program, make sure that all files are named based on this format: `[course_name: ABC-123]_[skillset: u32]_[skill: u32]_filename.md`. This paradigm ensures that each endpoint in the directory tree contains at least one markdown file.  

To start the program, run `bash init.sh` in your terminal from `root` directory to automatically generated JSON/YML scheme in `templates/from_pyvert.json`. All files, then, are designated to their directory based on the convention mentioned above. Run `bash start.sh` in your terminal from `root` directory to start the server.



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

Display all courses in JSON/YML format.

<h4> Schema format</h4> 
<h4> JSON </h4>

```
{
    "ALG-003": {
        "ALG-003_01": {
            "ALG-003_01_14": [
                "ALG-003_01_14_Exercise.md"
            ]
        }
    },
    "ALG-004": {
        "ALG-004_01": {
            "ALG-004_01_14": [
                "ALG-004_01_14_Exercise.md"
            ]
        }
    },
    "ALG-005": {
        "ALG-005_01": {
            "ALG-005_01_14": [
                "ALG-005_01_14_Exercise.md"
            ]
        }
    },
    "LIN-001": {
        "LIN-001_01": {
            "LIN-001_01_13": [
                "LIN-001_01_13_Material.md",
                "LIN-001_01_13_Exercise.md"
            ],
            "LIN-001_01_14": [
                "LIN-001_01_14_Material.md",
                "LIN-001_01_14_Exercise.md"
            ]
        }
    },
    "LIN-002": {
        "LIN-002_01": {
            "LIN-002_01_14": [
                "LIN-002_01_14_Exercise2.md",
                "LIN-002_01_14_Exercise.md"
            ]
        }
    },
    "LIN-003": {
        "LIN-003_01": {
            "LIN-003_01_14": [
                "LIN-003_01_14_Exercise.md"
            ]
        }
    }
}
```

<h4> YAML </h4>

```
---
ALG-003:
  ALG-003_01:
    ALG-003_01_14:
    - ALG-003_01_14_Exercise.md
ALG-004:
  ALG-004_01:
    ALG-004_01_14:
    - ALG-004_01_14_Exercise.md
ALG-005:
  ALG-005_01:
    ALG-005_01_14:
    - ALG-005_01_14_Exercise.md
LIN-001:
  LIN-001_01:
    LIN-001_01_13:
    - LIN-001_01_13_Material.md
    - LIN-001_01_13_Exercise.md
    LIN-001_01_14:
    - LIN-001_01_14_Material.md
    - LIN-001_01_14_Exercise.md
LIN-002:
  LIN-002_01:
    LIN-002_01_14:
    - LIN-002_01_14_Exercise2.md
    - LIN-002_01_14_Exercise.md
LIN-003:
  LIN-003_01:
    LIN-003_01_14:
    - LIN-003_01_14_Exercise.md

```