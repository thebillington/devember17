// Code to house a simple snake game
// Time started: 21:45
// Time finished: 

// Store the grid size
var gridSize = 20;

// Canvas size
var cSize = 600;

// Pixel size
var pixelSize;

// List to hold the snake
var snake;

// Snake speed
var speed;

// Store the powerup
var powerup;

// Store current direction
var direction;

// Function to return a coordinate
function Coord(x, y) {
    
    // Return the object
    return {"x": x, "y": y};
    
}

// Function to return a Snake
function Snake(x, y, speed, length, active) {
    
    //Create a new snake object
    var body = [];
    
    // Populate the body
    for (var i = 0; i < length; i++) {
        
        // Add to the body
        body.push(Coord(x - i * speed.dx, y - i * speed.dy));
        
    }
    
    // Return the snake
    return {"body": body.slice(), "speed": speed, "active": active}
    
}

// Setup function
function setup() {
    
    // Create a canvas
    createCanvas(cSize, cSize);
    
    // Calculate pixel size
    pixelSize = width / gridSize;
    
    // Create the snake
    snake = Snake(2, 0, {"dx": 1, "dy": 0}, 3, true);
    
    drawSnake();
    
    // Generate a powerup
    powerup = getRandCoord();
    
    // Set the direction
    direction = "right";
    
}

// Render function
function draw() {
    
    // Draw the grid
    drawGrid();
    
    // Draw the powerup
    drawGridSquare(powerup.x * pixelSize, powerup.y * pixelSize, color(255, 0, 0));
    
    // Draw the snake
    drawSnake();
    
    // Update the snake
    updateSnake();
    
    // Check if the powrup was eaten
    eaten();
    
    // Check for death
    death();
    
}

// Function to update the snake
function updateSnake() {
    
    // Move each of the pixels
    for (var i = snake.body.length - 1; i > 0; i--) {
        
        // Move the pixel to the previous location
        snake.body[i] = {"x":snake.body[i - 1].x, "y":snake.body[i - 1].y};
        
    }
    
    // Move the last location by speed
    snake.body[0] = {"x": snake.body[0].x + snake.speed.dx, "y": snake.body[0].y + snake.speed.dy}
    
    // Check if the head has wrapped
    if (snake.body[0].x < 0) {
        snake.body[0].x = gridSize - 1;
    }
        
    if (snake.body[0].x >= gridSize) {
        snake.body[0].x = 0;
    }
    if (snake.body[0].y < 0) {
        snake.body[0].y = gridSize - 1;
    }
        
    if (snake.body[0].y >= gridSize) {
        snake.body[0].y = 0;
    }
    
}

// Function to check if the player has eaten the powerup
function eaten() {
    
    // If the tail has collided with the powerup
    if (snake.body[snake.body.length - 1].x == powerup.x && snake.body[snake.body.length - 1].y == powerup.y) {
        
        // Update the snake
        updateSnake();
        
        // Add to the tail of the snake
        snake.body.push(powerup);
        
        // Generate a new powerup
        powerup = getRandCoord();
        
    }
    
}

// Function to check whether the snakle has died
function death() {
    
    // Check each of the snakes body parts
    for (var i = 1; i < snake.body.length; i++) {
        
        // If the snakes head has collided
        if (snake.body[0].x == snake.body[i].x && snake.body[0].y == snake.body[i].y) {
            
            // DIE
            setup();
            
        }
        
    }
    
}

// Function to draw a gridSquare
function drawGridSquare(x, y, colour) {
    
    // Set the colour
    color(0);
    fill(colour);
    
    // Draw
    quad(x, y, x + pixelSize, y, x + pixelSize, y + pixelSize, x, y + pixelSize);
    
}

// Function to drawe a snake
function drawSnake() {
    
    // Draw each of the pixels
    for (var i = 0; i < snake.body.length; i++) {
        
        // Get the x and y
        var x = snake.body[i].x * pixelSize;
        var y = snake.body[i].y * pixelSize;
        
        // Fill the pixel
        drawGridSquare(x, y, 0);
        
    }
    
}

// Create a function to render the grid
function drawGrid() {
    
    // Loop
    for (var i = 0; i < gridSize; i++) {
        for(var j = 0; j < gridSize; j++) {
            
            // Get x and y
            var x = i * pixelSize;
            var y = j * pixelSize;
            
            // Draw a quad at the correct location
            drawGridSquare(x, y, 255);
            
        }
        
    }
    
}

// Check for key presses
function keyPressed() {
    
    // Check the value
    if (keyCode == LEFT_ARROW && direction !== "right") {
        
        // Set the speed
        snake.speed = {"dx": -1, "dy": 0}
        direction = "left";
    }
    if (keyCode == RIGHT_ARROW && direction !== "left") {
        
        // Set the speed
        snake.speed = {"dx": 1, "dy": 0}
        direction = "right";
    }
    if (keyCode == UP_ARROW && direction !== "down") {
        
        // Set the speed
        snake.speed = {"dx": 0, "dy": -1}
        direction = "up";
    }
    if (keyCode == DOWN_ARROW && direction !== "up") {
        
        // Set the speed
        snake.speed = {"dx": 0, "dy": 1}
        direction = "down";
    }
    
}

// Function to generate a random coordinate
function getRandCoord() {
    
    // Return a random coordinate in the grid
    return {x: Math.floor(Math.random() * (gridSize)), y: Math.floor(Math.random() * (gridSize))}
    
}