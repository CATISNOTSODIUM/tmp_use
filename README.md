
<h3>Usage Description</h3> 
Files from src/tests will be served on the web server through the route .../receiver/?name=[filename].
<h3>Usage Description</h3>
<h2>/receiver</h2>
Files from `assets` will be served on the web server through the route ...`/receiver/?name=[filename].`
<h4> Example </h4>
Open image src/tests/ferris_the_crab.png: <br>

```
http://localhost:3000/receiver/`?name=ferris_the_crab.png
```


Open markdown LIN-001_1024_27/Exercise.md <br>
http://localhost:3000/receiver/`?name=LIN-001/LIN-001_1024/LIN-001_1024_27/Exercise.md
<h2>/tree</h2>
Display all courses as json.