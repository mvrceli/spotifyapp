var canvas, ctx, container;
canvas = document.createElement( 'canvas' );
ctx = canvas.getContext("2d");
var ball;


// Velocity x
var vx = 5.0;
// Velocity y - randomly set
var vy;

var gravity = 0.5;  
var bounce = 0.7; 
var xFriction = 0.1;

function init(){
setupCanvas();
vy = (Math.random() * -15) + -5;
ball = {x:canvas.width / 2, y:100, radius:20, status: 0,   color:"red"};

}//end init method

function draw() {
ctx.clearRect(0,0,canvas.width, canvas.height); 
//display some text
  ctx.fillStyle = "blue";
  ctx.font = "20px Arial";



    //draw cirlce
   ctx.beginPath();
   ctx.arc(ball.x, ball.y, ball.radius, 0, Math.PI*2, false);
   ctx.fillStyle = ball.color;
   ctx.fill();
   ctx.closePath();

ballMovement();

}

setInterval(draw, 1000/35); 




function ballMovement(){
ball.x += vx;
ball.y += vy;
vy += gravity;

//If either wall is hit, change direction on x axis
if (ball.x + ball.radius > canvas.width || ball.x - ball.radius < 0){
   vx *= -1;
} 

 // Ball hits the floor
if (ball.y + ball.radius > canvas.height){// ||
 
   // Re-positioning on the base
  ball.y = canvas.height - ball.radius;
   //bounce the ball
     vy *= -bounce;
   //do this otherwise, ball never stops bouncing
     if(vy<0 && vy>-2.1)
                vy=0;
   //do this otherwise ball never stops on xaxis
    if(Math.abs(vx)<1.1)
        vx=0;

    xF();
    
}


}

function xF(){
    if(vx>0)
        vx = vx - xFriction;
    if(vx<0)
        vx = vx + xFriction;
}






function setupCanvas() {//setup canvas


container = document.createElement( 'div' );
container.className = "container";

canvas.width = window.innerWidth; 
canvas.height = window.innerHeight; 
document.body.appendChild( container );
container.appendChild(canvas);	

ctx.strokeStyle = "#ffffff";
ctx.lineWidth =2;}