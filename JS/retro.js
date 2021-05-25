let degx=1 
let degy=1
let x=150
let y=150
let hell=document.getElementById("hell")
let rightborder= document.getElementById("rightborder1")
let leftborder= document.getElementById("leftborder1")
let a = document.getElementById("texthey")
let Line = document.getElementById("Line2")
console.log(a.style)
function collidesWith (element1, element2) {
    var Element1 = {};
    var Element2 = {};

    Element1.top = $(element1).offset().top;
    Element1.left = $(element1).offset().left;
    Element1.right = Number($(element1).offset().left) + Number($(element1).width());
    Element1.bottom = Number($(element1).offset().top) + Number($(element1).height());

    Element2.top = $(element2).offset().top;
    Element2.left = $(element2).offset().left;
    Element2.right = Number($(element2).offset().left) + Number($(element2).width());
    Element2.bottom = Number($(element2).offset().top) + Number($(element2).height());

    if (Element1.right > Element2.left && Element1.left < Element2.right && Element1.top < Element2.bottom && Element1.bottom > Element2.top) {
        return true
    }
    else{
        return false
    }
}
function moving(){
    a.setAttribute('cx', x);
    a.setAttribute('cy', y);
    if(collidesWith ( a, rightborder ) || collidesWith ( a, leftborder )){
        degx=-degx
    }
    if(!collidesWith ( a, hell )){
        degy=-degy
    }
    x+=1*degx
    y+=1*degy
    
    setTimeout('moving()',0.1)

}
                        //Button to start the game//
document.addEventListener('click',function(R){
    if(R.target.id == 'Button'){
        moving()
        document.getElementById('Button').style.display = 'none'
    }
  }
);

let left_br = document.getElementById("leftborder")

let right_br = document.getElementById("rightborder")

let last_b_pss = left_br.style.top

let last_r_pss = right_br.style.top

let left_br_1 = document.getElementById("leftborder1")

let right_br_1 = document.getElementById("rightborder1")

let last_b_pss_1 = left_br.style.top

let last_r_pss_1 = right_br.style.top

document.addEventListener('keypress',function(e){
    if(e.key == 's'){
        if(last_b_pss == 400){Number(last_b_pss) = 400}
        last_b_pss = Number(last_b_pss) + 10
        left_br.style.top = `${last_b_pss}px` 

        if(last_b_pss_1 == 400){Number(last_b_pss_1) = 400}
        last_b_pss_1 = Number(last_b_pss_1) + 10
        left_br_1.style.top = `${last_b_pss_1}px` 
    }
    else if(e.key == 'w'){
        if(last_b_pss == 0){Number(last_b_pss) = 0}
        last_b_pss = Number(last_b_pss) - 10
        left_br.style.top = `${last_b_pss}px` 

        if(last_b_pss_1 == 0){Number(last_b_pss_1) = 0}
        last_b_pss_1 = Number(last_b_pss_1) - 10
        left_br_1.style.top = `${last_b_pss_1}px` 
    }
    else if(e.key == 'l'){
        if(last_r_pss == 400){Number(last_r_pss) = 400}
        last_r_pss = Number(last_r_pss) + 10
        right_br.style.top = `${last_r_pss}px`

        if(last_r_pss_1 == 400){Number(last_r_pss_1) = 400}
        last_r_pss_1 = Number(last_r_pss_1) + 10
        right_br_1.style.top = `${last_r_pss_1}px`
    }
    else if(e.key == 'o'){
        if(last_r_pss_1 == 0){Number(last_r_pss_1) = 0}
        last_r_pss_1 = Number(last_r_pss_1) - 10
        right_br_1.style.top = `${last_r_pss_1}px`

        if(last_r_pss == 0){Number(last_r_pss) = 0}
        last_r_pss = Number(last_r_pss) - 10
        right_br.style.top = `${last_r_pss}px`
    }
  }
);

/*document.addEventListener('mousemove' , (e)=> {

    console.log(e.clientX,e.clientY)

})*/