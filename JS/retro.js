let degx=1
let degy=1
let x=10
let y=10
function moving(){
    let a = document.getElementById("texthey")
    console.log(document.getElementById("texthey").scrollWidth)
    a.setAttribute('cx', x);
    a.setAttribute('cy', y);
    if(x==490 || x==0){
        degy=-degy
    }
    if(y==500 || y==0){
        degx=-degx
    }
    x+=1*degx
    y+=1*degy
    console.log(x,y) 
    setTimeout('moving()',8)
}
function showCoords(event) {
    var x = event.clientX;
    var y = event.clientY;
    console.log(x,y)
}

moving()