# ROBOTS VS DINOSAURS

![](https://tokusatsu.blog.br/wp-content/uploads/2019/03/Godzilla-Vs-MechaGodzilla.jpg)

###Instructions
Use `make run` to execute the application, but dont forget to install the dependencies first.

You can use a swagger to call the apis at `http://127.0.0.1:8000/docs` 

You can create grids, robots and dinossaurs. You can also give commands to the robots to fight the dinossaurs. To do so you need to access the endpoints below

####POST /grid/create/
To create a new grid. It returns a json with the new grid id

####GET /grid/draw/{grid_id}
An preview with the grid and all the robots and dinosaurs

####POST /robot/create/
```json
{
            "grid_id": int,
            "position_x": int,
            "position_y": int,
            "facing": "up"|"down"|"left"|"right"
        }
```
You create a robot in a specific grid, in a specific position and facing an direction. It returns an json with the id of that robot (for that grid)

####POST /robot/instruction
```json
{
            "grid_id": int,
            "robot_id": int,
            "instruction": "move"|"turn"|"attack",
            "direction": "forward"|"backwards"| "left"|"right",
        }
```
You can give an instruction to a robot. that instruction can be:
- attack: destroy any dinosaurs in the adjacent of the robot
- turn: you can turn the direction of your robot is facing
- move: your robot can move forward and backward

####POST /dinosaur/create/
```json
{
            "grid_id": int,
            "position_x": int,
            "position_y": int,
        }
```
You create a dinosaur in a specific grid, in a specific position 
